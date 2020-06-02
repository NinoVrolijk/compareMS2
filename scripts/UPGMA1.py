from ete3 import *
from input_screen import *
import os

class UPGMA1():
    '''
    This class creates a newick file formatted phylogenetic tree. The program requires a MEGA file and processes this file using a UPGMA algorithm.
    The implementation of the UPGMA algorithm in python is created by Lex8Erna and is publicly
    available on Github: https://github.com/lex8erna/UPGMApy/blob/master/UPGMA.py
    License: MIT
    Copyright <2015> <Lex8Erna>
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    '''
    def __init__(self,distance_matrix_file):#,sample_amount):
        #self.sample_amount = sample_amount
        super().__init__()
        self.dmf = distance_matrix_file.strip() #Remove any spaces at the end of filename. This way the space doesnt interfere with string length.
        self.input_gen(self.dmf)
        current_dir = os.getcwd()


    def input_gen(self,dmf):
        ''' Input is a distance matrix file. The file gets translated into a NEWICK formatted tree. This translation is facilitated
        by an UPGMA algorithm.
        Attributes
        ----------
            dmf
                Distance matrix file. The program is developed to specifically deal with MEG format distance matrixes.
        '''
        self.M_labels2 = [] #List that contains labels.
        self.M2 = [[]]      #List where the integers out of the distance matrix file get stored. First element is left empty because that is mandatory in the NEWICK format.
        self.label_count = 0 #Keeps track of the amount of labels that are processed. If this counter is equal to total amount of labels in sample, the analysis is finished.
        with open(dmf, 'r') as f:
            for line in f:
                if line.startswith('#') and line[1].isupper(): #Format of line that contain label.
                    self.M_labels2.append(line[1:].strip()) #Remove \n and #
                    self.label_count += 1
                if line[0].isdigit():
                    if len(line.strip().split(' ')) > 0:#Each distance is seperate item in list. add space and tab
                        l = []                           #Wipes after each iteration of the loop.
                        for i in (line.strip().split(' ')):
                            l.append(float(i))
                            if len(l) == len((line.strip().split(' '))): #If lengths are equal, every distance is acounted for.
                                self.M2.append(l) #append M2 with all distances on line.

        output = self.UPGMA(self.M2, self.M_labels2) #Call the UPGMA algorithm. Returns a NEWICK format tree.
                                                     #Tree is saved in "output" variable
        self.create_tree(output) #Use output to create tree.


    def create_tree(self,output):
        ''' This method visualizes the tree into a .png file. The ETE3 Toolkit is the phylogenetic library that is used to
        create the image.
        Attributes
        ----------
            output
                NEWICK tree created by a UPGMA algorithm.
        '''
        t = Tree(output + ";", format=1)
        label_score = [] #each element is labele with comparison score.
        if self.label_count == 8 : #If self.label_count equals the amount of samples the user has inputted.
            with open (self.dmf, 'r') as x: #open each individual comparison file. This wil be added to the matrix file.
                for line in x:
                    if line.strip().split(" ")[0] == "QC":
                        id = line.strip().split(" ")[2]
                        score = line.strip().split(" ")[-1]
                        label_score.append([id,score]) #Append score (list) with elements that combine the id and score.
                if len(label_score) == self.label_count: # if all labels are present in the label_score list.
                        color = self.color_selector(label_score)
                        for n in t.traverse():
                            if n.is_leaf():
                                for y in color:
                                    if y[0] == n.name:
                                        n.img_style["fgcolor"] = y[2]
        ts = TreeStyle()
        ts.show_leaf_name = True
        t.render("compareMS2_tree.png", w=183, units="mm", tree_style=ts)

    def color_selector(self,label_score):
        '''Method that determines the coloring of the labels present in the tree.
        This is an extra quality control step that is executed after the tree is created.
        Attributes
        ----------
            label_score
                Elements in this list contain a label, and its corresponding quality control value.
        '''
        scores = []
        colors = []
        for y in label_score:
            scores.append(float(y[1])) #filter out quality scores.
        maximal = max(scores)
        minimal = min(scores)
        count = 0
        for x in scores:
            #Maintains relation between index x in scores and index x in label
            factor = (float(x) - minimal) / (maximal - minimal)
            if 1 >= factor > 0.8:
                color = 'Green'
            elif 0.8 > factor > 0.6:
                color = 'LightGreen'
            elif 0.6 > factor > 0.4:
                color = 'Orange'
            elif 0.4 > factor > 0.2:
                color = 'OrangeRed'
            elif 0.2 > factor >= 0.0:
                color = 'Red'
            label_score[count].append(color)
            count +=1

        return label_score

    def lowest_cell(self,table):
        # Set default to infinity
        min_cell = float("inf")
        x, y = -1, -1

        # Go through every cell, looking for the lowest
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] < min_cell:
                    min_cell = table[i][j]
                    x, y = i, j

        # Return the x, y co-ordinate of cell
        return x, y

    # join_labels:
    #   Combines two labels in a list of labels
    def join_labels(self,labels, a, b):
        # Swap if the indices are not ordered
        if b < a:
            a, b = b, a

        # Join the labels in the first index
        labels[a] = "(" + labels[a] + "," + labels[b] + ")"

        # Remove the (now redundant) label in the second index
        del labels[b]

    # join_table:
    #   Joins the entries of a table on the cell (a, b) by averaging their data entries
    def join_table(self,table, a, b):
        # Swap if the indices are not ordered
        if b < a:
            a, b = b, a

        # For the lower index, reconstruct the entire row (A, i), where i < A
        row = []
        for i in range(0, a):
            row.append((table[a][i] + table[b][i])/2)
        table[a] = row

        # Then, reconstruct the entire column (i, A), where i > A
        #   Note: Since the matrix is lower triangular, row b only contains values for indices < b
        for i in range(a+1, b):
            table[i][a] = (table[i][a]+table[b][i])/2

        #   We get the rest of the values from row i
        for i in range(b+1, len(table)):
            table[i][a] = (table[i][a]+table[i][b])/2
            # Remove the (now redundant) second index column entry
            del table[i][b]

        # Remove the (now redundant) second index row
        del table[b]


    # UPGMA:
    #   Runs the UPGMA algorithm on a labelled table
    def UPGMA(self,table, labels):
        # Until all labels have been joined...
        while len(labels) > 1:
            # Locate lowest cell in the table
            x, y = self.lowest_cell(table)
            # Join the table on the cell co-ordinates
            self.join_table(table, x, y)
            # Update the labels accordingly
            self.join_labels(labels, x, y)
        # Return the final label
        return labels[0]

    ## A test using an example calculation from http://www.nmsr.org/upgma.htm



#https://github.com/lex8erna/UPGMApy/blob/master/UPGMA.py
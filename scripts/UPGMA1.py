from ete3 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
    def __init__(self,distance_matrix_file):
        super().__init__()
        dmf = distance_matrix_file.strip() #Remove any spaces at the end of filename.
        self.input_gen(dmf)

    def input_gen(self,dmf):
        ''' Input is a distance matrix file. This file gets processed into lists that serve as input for the UPGMA algorithm.'''
        self.M_labels2 = []
        self.M2 = [[]]
        self.label_count = 0
        self.scoring = []
        with open(dmf, 'r') as f:
            for line in f:
                if line.startswith('#') and line[1].isupper():
                    self.M_labels2.append(line[1:].strip()) #Remove \n and #
                    self.label_count += 1
                if line[0].isdigit():
                    if len(line.strip().split(' ')) > 0:#Each distance is seperate item in list. add space and tab
                        l = []                           #Wipes after each iteration of the loop.
                        for i in (line.strip().split(' ')):
                            l.append(float(i))
                            if len(l) == len((line.strip().split(' '))): #If lengths are equal, every distance is acounted for.
                                self.M2.append(l) #append M2 with all distances on line.
        output = self.UPGMA(self.M2, self.M_labels2) #Call the UPGMA algorithm.
        self.create_tree(output) #Use output to create tree.

    def create_tree(self,output):
        ''' This method visualizes the tree into a .png file.'''
        t = Tree(output + ";", format=1)
        label_score = [] #each element is labele with comparison score.

        if self.label_count == 2: #If self.label_count equals the amount of samples the user has inputted.
            with open ('2019-4-15_BB1.mgf_results.txt','r') as x: #open each individual comparison file.
                for line in x:
                    if line.strip().startswith('dataset'):
                        id = line.strip().split('\t')[1].split(' ')[0] #Has to be seperated by tab in file.
                        score = line.strip().split('\t')[1].split(' ')[-1] #last element of the line has score.
                        id = id.split(':')[1].split('.')[0]
                        label_score.append([id,score])
                if len(label_score) == self.label_count: # if all labels are present in the label_score list.
                    color = self.color_selector(label_score)
                    print (color)
                    print (label_score[0][0])
                    for n in t.traverse():
                        if n.is_leaf() and n.name.startswith(label_score[0][0]):
                            n.img_style["fgcolor"] = color
        ts = TreeStyle()
        ts.show_leaf_name = True
        t.render("test.png", w=183, units="mm", tree_style=ts)

    def color_selector(self,label_score):
        scores = []
        for y in label_score:
            scores.append(y[1])
        maximum = int(max(scores))
        minimum = int(min(scores))
        factor = (maximum-minimum)/(maximum-minimum)
        if 1 >= factor > 0.8:
            color = 'Green'
        elif 0.8 > factor > 0.6:
            color = 'LightGreen'
        elif 0.6 > factor > 0.4:
            color = 'Orange'
        elif 0.4 > factor > 0.2:
            color = 'OrangeRed'
        elif 0.2 > factor > 0:
            color = 'Red'
        return color

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

    # alpha_labels:
    #   Makes labels from a starting letter to an ending letter
    def alpha_labels(start, end):
        labels = []
        for i in range(ord(start), ord(end)+1):
            labels.append(chr(i))
        return labels

#https://github.com/lex8erna/UPGMApy/blob/master/UPGMA.py

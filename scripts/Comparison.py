
from tree_analysis import *
import time

class compareMS2():
    def __init__(self):
        self.input_list = 'output_distane_matrix.meg'
        self.list_mgffiles = self.retrieve_files()
        self.input_list = self.retrieve_input()
        self.dmf = self.input_list[4][0].split(";")[0]
        self.comparisons()

    def retrieve_files(self):
        '''This method is generate a list of all present MGF files in the directory.'''
        list_mgffiles = []
        path = os.getcwd()
        for filename in os.listdir(path):
            if filename.endswith('.mgf'):
                list_mgffiles.append(filename)
        return list_mgffiles

    def retrieve_input(self):
         ''' This method is used to interpret the pre-generated input list derived from the GUI'''
        input_list = []
        with open('ms2compare_input.txt', 'r') as f:
            for line in f:
                input_list.append(line.split())
        return input_list

    def comparisons(self):
        '''This method executes CompareMS2.exe and CompareMS2_to_distance_matrices.exe'''
        cc = 0  # comparisons to be completed
        cc_track = 0  # Completed comparison tracker
        new_index = 1
        label_track = []
        for iteration in range(len(self.list_mgffiles)):  # Loop x amount of times, determined by amount of MGF files.
            cc += iteration
            if iteration == cc and iteration != 0:
                print(self.list_mgffiles[1].split('.')[0], '----', self.list_mgffiles[0].split('.')[0])
                label_track.append(self.list_mgffiles[1])
                label_track.append(self.list_mgffiles[0])
                self.write_labels(label_track)
                arguments = " -1 " + self.list_mgffiles[1] + " -2 " + self.list_mgffiles[
                    0] + " -w" + self.input_list[1][0].split(";")[0] + '-p' + self.input_list[2][0].split(";")[0] + \
                            ' -c' + self.input_list[5][0].split(";")[0] + " -MGF -o " \
                           + self.list_mgffiles[1] + "_vs_" + self.list_mgffiles[0] + "_results.txt"
                command = "compareMS2.exe"
                os.system(command + arguments)
                os.system('dir /b *_results.txt> all_comparisons.txt ')
                command = "compareMS2_to_distance_matrices.exe"
                arguments = ' -i all_comparisons.txt -o ' + self.input_list[4][0].split(";")[0] + ' -x ' + self.input_list[3][0].split(";")[0] + ' -m'  # -M because of MEG matrix.
                os.system(command + arguments)
                cc_track += 1
                new_index += 1
                #self.write_labels(label_track)
                time.sleep(10)
            else:
                for y in range(cc):
                    cc_track += 1  # Compare new item to al its previous indexes. Lets say item index = 2 compare to 0 and 1.
                    print(self.list_mgffiles[new_index].split('.')[0], '----', self.list_mgffiles[y].split('.')[0])
                    label_track.append(self.list_mgffiles[new_index])
                    label_track.append(self.list_mgffiles[y])
                    arguments = " -1 " + self.list_mgffiles[new_index] + " -2 " + self.list_mgffiles[y] + " -w" + self.input_list[1][0].split(";")[0] + '-p' +self.input_list[2][0].split(";")[0]  + \
                                ' -c' + self.input_list[5][0].split(";")[0] + " -MGF -o " \
                                + self.list_mgffiles[new_index] + "_vs_" + self.list_mgffiles[y] + "_results.txt"
                    command = "compareMS2.exe"
                    os.system(command + arguments)
                    os.system('dir /b *_results.txt> all_comparisons.txt ')
                        #command = "compareMS2_to_distance_matrices.exe"
                        #arguments = ' -i all_comparisons.txt -o ' + self.input_list[4][0].split(";")[0] + ' -x ' + self.input_list[3][0].split(";")[0] + ' -m'  # -M because of MEG matrix.
                        #os.system(command + arguments)
                        #print (command+arguments)
                    if cc == cc_track:
                        # update tree
                        #print('Completed comp', cc_track, 'Na :', iteration,
                              'runs') 
                        command = "compareMS2_to_distance_matrices.exe"
                        arguments = ' -i all_comparisons.txt -o ' + self.input_list[4][0].split(";")[0] + ' -x ' + self.input_list[3][0].split(";")[0] + ' -m'  # -M because of MEG matrix.
                        os.system(command + arguments)
                        new_index += 1
                        self.write_labels(label_track)
                        time.sleep(10)
                        break


    def write_labels(self,label_track):
        '''Writes labels to text file. These labels are used to create the phylogenetic tree.'''
        sample_to_species = []
        with open(self.input_list[3][0].split(";")[0], 'r') as w:
            for x in w:
                sample_to_species.append([x.split('\t')[0],x.split('\t')[-1].strip()])
        title_list = list(set(label_track))
        with open ('labels','w') as f:
            for title in sample_to_species:
                if title[0] in title_list:
                    #print (title[1])
                    f.write(title[1])
                    f.write('\n')

if __name__ == "__main__":
    compareMS2()



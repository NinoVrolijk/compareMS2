from comparems2gui import *
from tree_analysis import *
import sys

class functional (Gui):
    '''
    A class used to adds functional properties to:
        Tree analysis screen.
        Central input screen.
    Furthermore this is the main script to run the CompareMS2Gui pipeline.
    ...
    Parent class
    -----------
    Gui
        This class creates the central input screen (non functional) of the CompareMS2Gui.
    Attributes
    ---------
    X
    Methods
    -------
    write_checkbox(self):
        Method that appends checkbox status to saved file.
        Attributes
        ----------
        f
            Filename, this is the file that is being used in save_trigger.
    openFileDialog1(self):
        Open filedialog to upload input files into text box1.
    openFileDialog2(self):
        Open filedialog to upload input files into text box4.
    functional_toolbar(self)
        Adds functional properties to the toolbar present in the central input screen of the CompareMS2Gui.
        Multiple shortcuts for saving,loading and terminating the program are created.
    functional_buttons(self):
        Adds functional properties to all buttons present in the central input screen of the CompareMS2Gui
    Quit_trigger(self)
        Terminates program after connection of pushbutton.
    save_trigger(self):
        Allows the user to save input specified in the central input screen. .txt file is created.
    load_trigger(selF)
        Allows the user to upload previously specified inputs into to the central input screen. (Uploads .txt files)
    new_trigger(self)
        Wipes input specifications and return default values.
    submitmethod(self)
        Checks and sumbits specified input after connection of submit pushbutton. If all inputs have been approved, the program continues to the tree_analysis screen.
        Additional pop_up screens provide the user with the sumbit status.
    tree_processing(self)
        After connection of the submit method, the tree analysis screen is shown. This method adds functional properties to the progress bar and present buttons.
    return_gui(self)
        Adds function to the return button. Allows user to go back to the central input screen and rerun the program without terminating it completely.
    '''
    def __init__(self):
        super().__init__()
        self.functional_toolbar()
        self.functional_buttons()

    def openFileDialog1(self):
        '''Open filedialog to upload input files into text box1.
        '''
        self.filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "MGF file or mzML file (*.MGF *.mzML)") #Add more extensions.
        self.filepath = self.filename[0] #Filepath is present in first elemant of the retrieved filename.
        self.text_box1.setText(self.filepath) #Set text box1 with uploaded file.

    def openFileDialog2(self):
        ''' Open filedialog to upload input files into text box4.
        '''
        self.filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "MGF file or mzML file (*.MGF *.mzML)") #Add more extensions.
        self.filepath = self.filename[0]
        self.text_box4.setText(self.filepath) #Set text box 4 with uploaded file.

    def functional_toolbar(self):
        '''Adds functional properties to toolbar present in the main GUI screen.
        Multiple shortcuts for saving,loading and terminating the program are created.
        '''
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        quit_action = QAction('Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        load_action = QAction('Load options',self)
        load_action.setShortcut('Ctrl+L')
        self.file.addAction(load_action)
        self.file.addAction(save_action)
        self.file.addAction(quit_action)
        self.file.addAction(new_action)
        quit_action.triggered.connect(self.quit_trigger)
        new_action.triggered.connect(self.new_trigger)
        save_action.triggered.connect(self.save_trigger)
        load_action.triggered.connect(self.load_trigger)

    def functional_buttons(self):
        '''Adds functional properties to all buttons present in the central input screen of the CompareMS2Gui.
        '''
        self.cancel_button.clicked.connect(self.quit_trigger)
        self.submit_button.clicked.connect(self.submitmethod)
        self.browse_button1.clicked.connect(self.openFileDialog2)
        self.browse_button0.clicked.connect(self.openFileDialog1)

    def quit_trigger(self):
        ''' Terminates program after connection of pushbutton.
        '''
        qApp.quit() #Terminates screen

    def save_trigger(self,orientation):
        '''Allows the user to save input specified in the central input screen.
        When not inputs have been specified, the program ask the user to specify every input.
        '''
        if orientation == False:
            self.save_name = QFileDialog.getSaveFileName(self,'Save file',"compareMS2options","Text file(*.txt)")
            f = open(self.save_name[0], 'w')
        elif orientation == 1:
            f = open('ms2compare_input.txt','w')
        if all([len(self.text_box1.text()) > 0, len(self.text_box2.text()) > 0, len(self.text_box3.text()) > 0,len(self.text_box4.text()) > 0,
                len(self.text_box5.text()) > 0,len(self.text_box6.text()) > 0]): #Checks if all text boxes have been filled.
            f.write(self.text_box1.text() + ";Directory\n")
            f.write(self.text_box2.text() + ";Maximum precursor\n")
            f.write(self.text_box3.text() + ";Chromatic peak width\n")
            f.write(self.text_box4.text() + ";Table with samples\n")
            f.write(self.text_box5.text() + ";output filename\n")
            f.write(self.text_box6.text() + ";Score (cosine) cutoff\n")
            self.write_checkbox(f)
            f.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error saving input")
            msg.setText("Not all inputs have been specified! Try again")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()  # Shows message box

    def write_checkbox(self,f):
        ''' Method that appends checkbox status to saved file.
        Attributes
        ----------
        f
            Filename, this is the file that is being used in save_trigger.
        '''
        if self.check_capture_log.isChecked():
            f.write('+;capture_log\n')
        else:
            f.write('-;capture_log\n')
        if self.check_rich_output.isChecked():
            f.write('+;rich_output\n')
        else:
            f.write('-;rich_output\n')
        if self.avcps.isChecked():
            f.write('+;average comparisons\n')
        else:
            f.write('-;average comparisons\n')
        if self.check_nexus_output.isChecked():
            f.write('+;Nexus output\n')
        else:
            f.write('-;Nexus output\n')
        if self.check_NEELY_output.isChecked():
            f.write('+;Neely output\n')
        else:
            f.write('-;Neely output\n')
        if self.check_MEGA_output.isChecked():
            f.write('+;MEG output\n')
        else:
            f.write('-;MEG output\n')
        if self.check_missing_values.isChecked():
            f.write('+;Missing values\n')
        else:
            f.write('-;Missing values\n')

    def load_trigger(self):
        '''Allows the user to upload previously specified inputs into to the central input screen. (Uploads .txt file)
        '''
        self.options_file = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '', "txt file (*.txt )")
        with open(self.options_file[0], "r") as f: #Opens filename as read only.
            file = f.readlines()                   #Read seperate lines of file.
            directory = file[0].split(';')
            self.text_box1.setText(directory[0])
            mp = file[1].split(';')
            self.text_box2.setText(mp[0])
            cpw = file[2].split(';')
            self.text_box3.setText(cpw[0])
            tws = file[3].split(';')
            self.text_box4.setText(tws[0])
            ofn = file[4].split(';')
            self.text_box5.setText(ofn[0])
            cutoff = file[5].split(';')
            self.text_box6.setText(cutoff[0])
            capture_log = file[6].split(';')
            rich_log = file[7].split(';')
            average_comparison = file[8].split(';')
            nexus_box = file[9].split(';')
            neely_box = file[10].split(';')
            MEG_box = file[11].split(';')
            missing_values = file[12].split(';')
            if capture_log[0] == "+":
                self.check_capture_log.setChecked(True)
            else:
                self.check_capture_log.setChecked(False)
            if rich_log[0] == "+":
                self.check_rich_output.setChecked(True)
            else:
                self.check_rich_output.setChecked(False)
            if average_comparison[0] == "+":
                self.avcps.setChecked(True)
            else:
                self.avcps.setChecked(False)
            if nexus_box[0] == "+":
                self.check_nexus_output.setChecked(True)
            else:
                self.check_nexus_output.setChecked(False)
            if neely_box[0] == "+":
                self.check_NEELY_output.setChecked(True)
            else:
                self.check_NEELY_output.setChecked(False)
            if MEG_box[0] == "+":
                self.check_MEGA_output.setChecked(True)
            else:
                self.check_MEGA_output.setChecked(False)
            if missing_values[0] == "+":
                self.check_missing_values.setChecked(True)
            else:
                self.check_missing_values.setChecked(False)

    def new_trigger(self):
        '''Wipes input specifications and return default values.
        '''
        self.text_box1.setText(':c')
        self.text_box2.setText('2.05')
        self.text_box3.setText('1500')
        self.text_box4.setText('')
        self.text_box5.setText('')
        self.text_box6.setText('')
        self.check_capture_log.setChecked(True)
        self.check_rich_output.setChecked(False)
        self.avcps.setChecked(False)
        self.check_nexus_output.setChecked(False)
        self.check_MEGA_output.setChecked(False)
        self.check_NEELY_output.setChecked(False)
        self.check_missing_values.setChecked(False)

    def submitmethod(self):
        '''Checks and sumbits specified input after connection of submit pushbutton. If all inputs have been approved, the program continues to the tree_analysis screen.
        Additional pop_up screens provide the user with the sumbit status.
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Submit status")
        directory_file = self.text_box1.text()
        if len(directory_file) == 0 and len(self.filepath) > 0: #check if there is a directory file provided
            self.text_box1.setText(self.filepath)
        fp = self.text_box1.text() #Filepath is saved into variable.
        if len(fp) > len("c:") and len(self.text_box5.text()) > 1: #this determines whether a complete file path has been submitted.
            msg.setText("Congratulations, your input has been succesfully submitted. The tree is being generated")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_() #Shows message box
            self.hide() #Hide input screen.
            self.distance_matrix_file = self.text_box5.text()
            self.save_trigger(1)
            while True: #While loop used to update the tree image.
                self.tree_processing(self.distance_matrix_file) #Creates new image each iteration of loop.
                QtTest.QTest.qWait(10000) #Wait every X amount of miliseconds after each iteration.
        elif len(fp) <= len("c:") or len(self.text_box5.text()) == 0: #Checks if there is a file provided.
            msg.setText("Not all inputs have been specified! Try again")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()  # Shows message box
            self.new_trigger() #Wipes the screen.

    def tree_processing(self,distance_matrix_file):
        '''Displays the tree analysis screen. Adds functionality to buttons and updates progressbar.
        '''
        self.tree = tree_analysis(distance_matrix_file) #Calls tree screen and passes the distance matrix file.
        percentual_progress = (self.tree.upgma_result.label_count / 118) * 100  # Divide with amount of samples present in input file. 100 is generic number used to test.
        self.tree.progress.setValue(percentual_progress)
        self.tree.return_button.clicked.connect(self.return_gui) #Adds functional property to return button.
        self.tree.show() #Show tree analysis screen.

    def return_gui(self):
        '''Adds function to the return button. Allows user to go back to the central input screen and rerun the program without terminating it completely.
        '''
        self.tree.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = functional()
    sys.exit(app.exec_())


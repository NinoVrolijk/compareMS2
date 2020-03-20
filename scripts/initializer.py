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

    def save_trigger(self):
        '''Allows the user to save input specified in the central input screen.
        '''
        self.save_name = QFileDialog.getSaveFileName(self,'Save file',"compareMS2options","Text file(*.txt)")
        f = open(self.save_name[0], 'w')
        f.write(self.text_box1.text()+"\n")
        f.write(self.text_box2.text()+"\n")
        f.write(self.text_box3.text()+"\n")
        f.write(self.text_box4.text()+"\n")
        f.write(self.text_box5.text()+"\n")
        f.write(self.text_box6.text()+"\n")
        f.close()
        #To do! Add default options when the text_box is left empty. And add checkbox parameters.

    def load_trigger(self):
        '''Allows the user to upload previously specified inputs into to the central input screen. (Uploads .txt file)
        '''
        self.options_file = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '', "txt file (*.txt )")
        with open(self.options_file[0], "r") as f: #Opens filename as read only.
            file = f.readlines()                   #Read seperate lines of file.
            self.text_box1.setText(file[0])
            self.text_box2.setText(file[1])
            self.text_box3.setText(file[2])
            self.text_box4.setText(file[3])
            self.text_box5.setText(file[4])
            self.text_box6.setText(file[5])

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


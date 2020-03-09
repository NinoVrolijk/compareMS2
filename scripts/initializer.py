from comparems2gui import *
from UPGMA1 import *
from tree_analysis import *
import sys

class functional (Gui):
    def __init__(self):
        super().__init__()
        self.functional_toolbar()
        self.functional_buttons()

    def openFileDialog1(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "MGF file or mzML file (*.MGF *.mzML)") #Add more extensions.
        self.filepath = self.filename[0]
        self.text_box1.setText(self.filepath)

    def openFileDialog2(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "MGF file or mzML file (*.MGF *.mzML)") #Add more extensions.
        self.filepath = self.filename[0]
        self.text_box4.setText(self.filepath)

    def functional_toolbar(self):
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
        quit_action.triggered.connect(self.quit_trigger)  # triggers termination proces.
        new_action.triggered.connect(self.new_trigger)
        save_action.triggered.connect(self.save_trigger)
        load_action.triggered.connect(self.load_trigger)

    def functional_buttons(self):
        self.cancel_button.clicked.connect(self.quit_trigger)
        self.submit_button.clicked.connect(self.submitmethod)
        self.browse_button1.clicked.connect(self.openFileDialog2)
        self.browse_button0.clicked.connect(self.openFileDialog1)

    def quit_trigger(self):
        qApp.quit()

    def save_trigger(self):
        self.save_name = QFileDialog.getSaveFileName(self,'Save file',"compareMS2options","Text file(*.txt)")
        f = open(self.save_name[0], 'w')
        f.write(self.text_box1.text()+"\n")
        f.write(self.text_box2.text()+"\n")
        f.write(self.text_box3.text()+"\n")
        f.write(self.text_box4.text()+"\n")
        f.write(self.text_box5.text()+"\n")
        f.write(self.text_box6.text()+"\n")
        f.close()

    def load_trigger(self):
        self.options_file = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '', "txt file (*.txt )")
        with open(self.options_file[0], "r") as f:
            file = f.readlines()
            self.text_box1.setText(file[0])
            self.text_box2.setText(file[1])
            self.text_box3.setText(file[2])
            self.text_box4.setText(file[3])
            self.text_box5.setText(file[4])
            self.text_box6.setText(file[5])

    def new_trigger(self):
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

        msg = QMessageBox()
        msg.setWindowTitle("Submit status")
        directory_file = self.text_box1.text()
        if len(directory_file) == 0 and len(self.filepath) > 0:
            self.text_box1.setText(self.filepath)
        fp = self.text_box1.text()
        if len(fp) > len("c:") and len(self.text_box5.text()) > 1: #this determines whether a complete file path has been submitted.
            msg.setText("Congratulations, your input has been succesfully submitted. The tree is being generated")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_() #Shows message box
            self.hide()
            distance_matrix_file = self.text_box5.text()
            self.upgma_result = UPGMA1(distance_matrix_file)# The Distance matrix and labels are input to this method. It returns a completed tree.
            self.show_tree()

        elif len(fp) <= len("c:") or len(self.text_box5.text()) == 0:
            msg.setText("Not all inputs have been specified! Try again")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()  # Shows message box
            self.new_trigger() #Wipes the screen.

    def show_tree(self):
        '''Importing and displaying tree screen.'''
        self.ta_screen = tree_analysis()
        self.ta_screen.show()

        percentual_progress = (self.upgma_result.label_count / 100) * 100 #Divide with amount of samples present in input file. 100 is generic number used to test.
        self.ta_screen.progress.setValue(percentual_progress)
        self.ta_screen.return_button.clicked.connect(self.return_GUItrigger)

    def return_GUItrigger(self):
        self.ta_screen.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = functional()
    sys.exit(app.exec_())


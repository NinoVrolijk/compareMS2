import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Gui(QMainWindow, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.window_specs()
        self.menubar()
        self.text_box()
        self.button_creator()
        self.text_labels()
        self.checkbox()
        self.reveal() #final method.

    def checkbox(self):
        self.check_capture_log = QCheckBox("Capture log", self)
        self.check_rich_output = QCheckBox("Rich output", self)
        self.avcps = QCheckBox("Average all comparisons per species", self)
        self.check_nexus_output = QCheckBox("NEXUS output", self)
        self.check_MEGA_output = QCheckBox("MEGA output", self)
        self.check_NEELY_output = QCheckBox("NEELY output", self)
        self.check_missing_values = QCheckBox("Impute missing values", self)
        self.check_capture_log.move(10,250)
        self.check_rich_output.move(150, 250)
        self.checkbox_orientation(self.check_nexus_output,10)
        self.checkbox_orientation(self.check_MEGA_output, 150)
        self.checkbox_orientation(self.check_NEELY_output, 290)
        self.checkbox_orientation(self.check_missing_values,440)

    def checkbox_orientation(self,checkbox,orientation):
        checkbox.resize(250,30)
        checkbox.move(orientation,520)
        self.check_capture_log.move(10, 250)
        self.check_rich_output.move(150, 250)
        self.avcps.resize(250, 30)
        self.avcps.move(10, 480)
        self.check_capture_log.setChecked(True)

    def text_box(self):
        self.text_box1 = QLineEdit(self)
        self.text_box2 = QLineEdit(self)
        self.text_box3 = QLineEdit(self)
        self.text_box4 = QLineEdit(self)
        self.text_box5 = QLineEdit(self)
        self.text_box6 = QLineEdit(self)
        self.text_box_orientation(self.text_box1,110)
        self.text_box_orientation(self.text_box2,160)
        self.text_box_orientation(self.text_box3,210)
        self.text_box_orientation(self.text_box4,350)
        self.text_box_orientation(self.text_box5,400)
        self.text_box_orientation(self.text_box6,450)

    def text_box_orientation(self,text_box,orientation):
        text_box.move(300, orientation)
        text_box.resize(400, 30)
        self.text_box2.setText('2.05')
        self.text_box3.setText('1500')

    def window_specs(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        app_icon = QIcon("path_to_file")
        #app.setWindowIcon(app_icon)

    def text_labels(self):
        self.text_label1 = QLabel(self)
        self.text_label2 = QLabel(self)
        self.text_label3 = QLabel(self)
        self.text_label4 = QLabel(self)
        self.text_label5 = QLabel(self)
        self.text_label6 = QLabel(self)
        self.text_label7 = QLabel(self)
        self.text_label8 = QLabel(self)
        self.text_label9 = QLabel(self)
        self.text_label10 = QLabel(self)
        self.text_label1.setText('Specify inputs to compareMS2:')
        self.text_label2.setText('Directory of MGF or mzML file:')
        self.text_label3.setText('Maximum precursor mass difference:')
        self.text_label4.setText('Maximum chromatographic peak width:')
        self.text_label5.setText('(in m/z units)')
        self.text_label6.setText('(in scans)')
        self.text_label7.setText('Specify inputs for distance matrix calculation:')
        self.text_label8.setText('Table with sample to species relationships:')
        self.text_label9.setText('Output filename root')
        self.text_label10.setText('Score (cosine) cutoff')
        self.text_label1.move(5, 10)
        self.text_label5.move(750, 160)
        self.text_label6.move(750, 210)
        self.text_label7.move(5, 270)
        self.text_label1.resize(300, 100)
        self.text_label7.resize(500, 100)
        self.label_style(self.text_label2, 100)
        self.label_style(self.text_label3, 150)
        self.label_style(self.text_label4, 200)
        self.label_style(self.text_label8, 340)
        self.label_style(self.text_label9, 390)
        self.label_style(self.text_label10, 440)

    def label_style(self,text_label,orientation):
        text_label.move(5, orientation)
        text_label.resize(300, 50)
        font = QFont("Arial",9)
        text_label.setFont(font)
        self.head_font = QFont("Arial", 11,QFont.Bold)
        self.text_label1.setFont(self.head_font)
        self.text_label7.setFont(self.head_font)
        self.font_cursive = QFont("Arial", 8, QFont.Cursive)
        self.text_label5.setFont(self.font_cursive)
        self.text_label6.setFont(self.font_cursive)

    def button_creator(self):
        self.browse_button0 = QPushButton('Browse File',self)
        self.browse_button0.clicked.connect(self.openFileDialog)
        self.browse_button1 = QPushButton('Browse File',self)
        self.browse_button1.clicked.connect(self.openFileDialog)
        self.button_style(self.browse_button0,110) #initiates button style function.
        self.button_style(self.browse_button1,350)
        self.submit_button = QPushButton('Submit', self)
        self.cancel_button = QPushButton('Cancel', self)
        self.submit_button.clicked.connect(self.submitmethod)
        self.cancel_button.clicked.connect(self.quit_trigger)
        self.submit_button.move(10, 570)
        self.cancel_button.move(160, 570)
        self.submit_button.setStyleSheet("border: 2px solid ;font: bold; background-color: darkblue; color: white")
        self.cancel_button.setStyleSheet("border: 2px solid ;font: bold; background-color: darkblue; color: white")

    def button_style(self,button,orientantion):
        button.setStyleSheet("border: 2px solid ;font: bold; background-color: darkblue; color: white")
        button.resize(100, 30)
        button.move(750,orientantion)

    def openFileDialog(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "MGF file or mzML file (*.MGF *.mzML)")
        self.filepath = self.filename[0]

    def menubar(self):
        #create menubar
        bar = self.menuBar()
        #Create root Menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')
        toolbar = bar.addMenu('Toolbar')
        help = bar.addMenu('Help')
        #Create actions for menu
        save_action = QAction('Save',self)
        save_action.setShortcut('Ctrl+S')
        new_action = QAction('New',self)
        new_action.setShortcut('Ctrl+N')
        quit_action = QAction('Quit',self)
        quit_action.setShortcut('Ctrl+Q')
        #Add actions to Menus
        file.addAction(save_action)
        file.addAction(quit_action)
        file.addAction(new_action)
        #Event actions
        quit_action.triggered.connect(self.quit_trigger) #triggers termination proces.

    def quit_trigger(self):
        qApp.quit()

    def submitmethod(self):
        directory_file = self.text_box1.text()
        if len(directory_file) == 0 and len(self.filepath) > 0:
            directory_file = self.filepath
            self.text_box1.setText(self.filepath)
        else:
            pass
        max_precursor = self.text_box2.text()
        max_chromatographic_peak = self.text_box3.text()
        msg = QMessageBox()
        msg.setWindowTitle("Submit status")
        msg.setText("Congratulations, your input has been succesfully submitted.")
        msg.setIcon(QMessageBox.Question)
        x = msg.exec_() #Shows message box

    def reveal(self):
        self.setWindowTitle('CompareMS2Gui')
        self.setGeometry(500,300,150,150) #Orientation of screen
        self.resize(1000,620)             #Size of screen
        self.show()                      #show screen

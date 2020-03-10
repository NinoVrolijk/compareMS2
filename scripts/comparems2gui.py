from introduction import * #Imports the PYQT modules from introduction.

class Gui(QMainWindow, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.introduction()
        self.window_specs()
        self.menubar()
        self.text_box()
        self.button_creator()
        self.text_labels()
        self.checkbox()
    def introduction(self):
        '''Importing introduction screen and hide GUI.'''
        self.intro_screen = Introduction()
        self.intro_screen.show()
        self.intro_screen.continue_button.clicked.connect(self.reveal)
        self.hide()

    def checkbox(self):
        '''Creating all checkboxes present on the GUI screen'''
        self.check_capture_log = QCheckBox("Capture log", self)
        self.check_rich_output = QCheckBox("Rich output", self)
        self.avcps = QCheckBox("Average all comparisons per species", self)
        self.check_nexus_output = QCheckBox("NEXUS output", self)
        self.check_MEGA_output = QCheckBox("MEGA output", self)
        self.check_NEELY_output = QCheckBox("NEELY output", self)
        self.check_missing_values = QCheckBox("Impute missing values", self)
        self.checkbox_orientation(self.check_nexus_output,30)
        self.checkbox_orientation(self.check_MEGA_output, 170)
        self.checkbox_orientation(self.check_NEELY_output, 310)
        self.checkbox_orientation(self.check_missing_values,460)

    def checkbox_orientation(self,checkbox,orientation):
        checkbox.resize(250,30)
        checkbox.move(orientation,520)
        self.check_capture_log.move(30, 250)
        self.check_rich_output.move(170, 250)
        self.avcps.resize(250, 30)
        self.avcps.move(30, 480)
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
        text_box.move(340, orientation)
        text_box.resize(400, 30)
        self.text_box1.setText('c:')
        self.text_box2.setText('2.05')
        self.text_box3.setText('1500')

    def window_specs(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint) #cancels out maximize optio
        app_icon = QIcon("ms2compare.png")
        self.setWindowTitle('CompareMS2Gui')
        self.setGeometry(500,300,150,150) #Orientation of screen
        self.resize(1000,620)             #Size of screen
        self.setWindowIcon(app_icon)

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
        self.text_label1.move(15, 10)
        self.text_label5.move(770, 160)
        self.text_label6.move(770, 210)
        self.text_label7.move(15, 270)
        self.text_label1.resize(300, 100)
        self.text_label7.resize(500, 100)
        self.label_style(self.text_label2, 100)
        self.label_style(self.text_label3, 150)
        self.label_style(self.text_label4, 200)
        self.label_style(self.text_label8, 340)
        self.label_style(self.text_label9, 390)
        self.label_style(self.text_label10, 440)

    def label_style(self,text_label,orientation):
        text_label.move(30, orientation)
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
        self.browse_button1 = QPushButton('Browse File',self)
        self.button_style(self.browse_button0,110) #initiates button style function.
        self.button_style(self.browse_button1,350)
        self.submit_button = QPushButton('Submit', self)
        self.cancel_button = QPushButton('Exit', self)

        self.submit_button.move(30, 570)
        self.cancel_button.move(180, 570)
        self.submit_button.resize(100, 33)
        self.cancel_button.resize(100,33)
        self.submit_button.setStyleSheet("border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;")
        self.cancel_button.setStyleSheet("border-radius: 7px;border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;")

    def button_style(self,button,orientantion):
        button.setStyleSheet("border-radius: 7px;border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;")
        button.resize(100, 33)
        button.move(770,orientantion)

    def menubar(self):
        #create menubar
        self.bar = self.menuBar()
        #Create root Menus
        self.file = self.bar.addMenu('File')
        self.edit = self.bar.addMenu('Edit')
        self.toolbar = self.bar.addMenu('Toolbar')
        self.help = self.bar.addMenu('Help')

    def reveal(self):
        self.intro_screen.hide()          #hides intro screen and shows the actual GUI.
        self.show()                      #show screen

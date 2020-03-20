from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Introduction(QMainWindow, QWidget):
    '''
    A class that creates the CompareMS2Gui introduction screen. This screen relevant information about the CompareMS2 algorithm and GUI.
    ...
    Parent classes
    -----------
    QMainWindow, QWidget.
        Both classes provide PyQT5 properties used to create the introduction screen of the CompareMS2Gui pipeline.

    Attributes
    ---------
    X
    Methods
    -------
    setimage(self)
        Creates the image label. This image is placed in the center of the screen.
    buttons(self)
        A method to create the required buttons present in the CompareMS2Gui introdcution screen.
    popup(self)
        Reveal popup information window after connection of information button.
    window_specs(self)
        Additional window spefications.
            Removed maximize button.
            Set logo.
    text_labels(self)
        Method that creates all required text_labels.
    reveal(self)
        Reveal screen.

    '''
    def __init__(self):
        super().__init__()
        self.setimage()
        self.text_labels()
        self.buttons()
        self.window_specs()
        self.reveal()

    def setimage(self):
        ''' Creates the image label. This image is placed in the center of the screen.
        '''
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('ms2compare.png'))
        self.image.setGeometry(380,180,500,200)

    def buttons(self):
        '''A method to create the required buttons present in the CompareMS2Gui introdcution screen.
        '''
        self.continue_button = QPushButton('Continue', self)
        self.info_button = QPushButton('Information', self)
        self.continue_button.setStyleSheet(
            "border-radius: 7px;border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;")
        self.info_button.setStyleSheet(
            "border-radius: 7px;border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;") #Extensive CSS stylesheets.
        self.continue_button.resize(150,50)
        self.info_button.resize(150, 50)
        self.continue_button.move(325,450)
        self.info_button.move(475, 450)
        self.info_button.clicked.connect(self.popup) #Initiates popup window.


    def popup(self):
        ''' Reveal popup information window after connection of information button.
        '''
        info = QMessageBox()
        info.setWindowTitle("compareMS2 information")
        info.setText(" Authors,version,date,organization etc.\n Whatever information u want here.")
        info.setIcon(QMessageBox.Information)
        info.setWindowIcon(self.app_icon)
        x = info.exec_()  # Shows message box

    def window_specs(self):
        '''
        Additional window spefications.
            Removed maximize button.
            Set logo.
        '''
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint) #cancels out maximize option
        self.app_icon = QIcon("ms2compare.png")
        self.setWindowIcon(self.app_icon)
        self.setWindowTitle('compareMS2Gui')
        self.setGeometry(500, 300, 150, 150)  # Orientation of screen
        self.resize(1000, 620)  # Size of screen

    def text_labels(self):
        ''' Method that creates all required text_labels.
        '''
        self.text_header = QLabel(self)
        self.text_subtitle = QLabel(self)
        self.text_author = QLabel(self)
        self.text_header.setText('compareMS2Gui')
        self.text_subtitle.setText('Molecular phylogenetics analyses based on mass spectrometry')
        self.text_author.setText('© LUMC 2020')
        self.text_header.move(380,50)
        self.text_subtitle.move(310,90)
        self.text_header.resize(300, 50)
        self.text_subtitle.resize(500,50)
        self.text_author.move(900,580)
        font = QFont("Arial", 15,QFont.ExtraBold)
        font2 = QFont("Arial",7,QFont.Cursive)
        font3 = QFont("Arial",7,QFont.ExtraBold)
        self.text_header.setFont(font)
        self.text_subtitle.setFont(font2)
        self.text_author.setFont(font3)

    def reveal(self):
        '''Reveal screen.
        '''
        self.show()  # show screen

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    window = Introduction()
#    sys.exit(app.exec_())
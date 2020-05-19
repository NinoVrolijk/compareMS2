import sys
from initializer import *
from PyQt5.QtWidgets import *
from PyQt5 import QtTest
from UPGMA1 import *


class tree_analysis(QDialog):
    '''
    A class used to create a screen that visualizes progression in phylogenetic analysis.
    ...
    Attributes
    ---------
    distance_matrix
        MEGA distance matrix file.
    Methods
    -------
    image_generator(self,distance_matrix):
        Induces UPGMA algorithm and saves newick tree format.
        Attributes
        ----------
            distance_matrix
    layout_image(self):
        Creates groupbox. This vertical groupbox contains the tree image and a progress bar.
    layout_buttons(self):
        Create a horizontal groupbox that contains a termination and return button.
    quit_trigger(self):
        Terminates program after connection of pushbutton.
    InitWindow(self):
         Initializes window.
    '''
    def __init__(self,distance_matrix):
        super().__init__()
        self.title = 'compareMS2Gui'
        self.left = 600
        self.top = 250
        self.width = 700
        self.height = 650
        self.app_icon = QIcon("ms2compare.png")
        self.setWindowIcon(self.app_icon)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  # cancels out maximize option
        self.image_generator(distance_matrix)

    def image_generator(self,distance_matrix):
        '''Calls UPGMA algorithm and saves the tree in newick format.'''
        self.upgma_result = UPGMA1(distance_matrix)
        self.InitWindow() #Call window initializer

    def layout_image(self):
        '''Creates groupbox. This vertical groupbox contains the tree image and a progress bar.'''
        self.groupBox1 = QGroupBox("Tree analysis")
        self.groupBox1.setStyleSheet("QGroupBox { font-weight: bold; font-size: 18px } ")
        vbox = QVBoxLayout()
        tree_image = QLabel(self)
        tree_image.setPixmap(QPixmap('test.png'))
        scrollArea = QScrollArea()
        scrollArea.setWidget(tree_image)
        self.progress = QProgressBar(self)
        self.progress.setMaximum(100)
        vbox.addWidget(scrollArea)
        vbox.addWidget(self.progress)
        self.groupBox1.setLayout(vbox)

    def layout_buttons(self):
        '''Create a horizontal groupbox that contains a termination and return button.'''
        self.button_row = QGroupBox()
        filler_label = QLabel(self) #Empty label to scale buttons.
        hbox = QHBoxLayout()
        exit_button = QPushButton('Terminate', self)
        self.return_button = QPushButton('Return', self)
        exit_button.setMaximumWidth(100)
        self.return_button.setMaximumWidth(100)
        exit_button.setStyleSheet(
            "border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;"
        )
        self.return_button.setStyleSheet(
            "border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;"
        )
        hbox.addWidget(exit_button)
        hbox.addWidget(self.return_button)
        hbox.addWidget(filler_label)
        exit_button.clicked.connect(self.quit_trigger)
        self.button_row.setLayout(hbox)
        
    def quit_trigger(self):
        sys.exit()

    def InitWindow(self):
        '''' Initializes window.'''
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color:white;")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout_image()
        self.layout_buttons()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox1)
        vbox.addWidget(self.button_row)
        self.setLayout(vbox)
        #self.show()

#if __name__ == "__main__":
#    App = QApplication(sys.argv)
#    Window = tree_analysis()
#    sys.exit(App.exec())
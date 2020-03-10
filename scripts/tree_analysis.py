import sys
from initializer import *
from PyQt5.QtWidgets import *
from UPGMA1 import *
import time

class tree_analysis(QDialog):
    def __init__(self,distance_matrix): #add distance_matrix
        super().__init__()
        self.title = 'ms2compare'
        self.left = 600
        self.top = 250
        self.width = 650
        self.height = 550
        self.app_icon = QIcon("ms2compare.png")
        self.setWindowIcon(self.app_icon)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  # cancels out maximize option
        self.image_generator(distance_matrix)
    def image_generator(self,distance_matrix):
        self.upgma_result = UPGMA1(distance_matrix)
        self.InitWindow()

    def layout_image(self):
        self.groupBox1 = QGroupBox("Tree analysis")
        self.groupBox1.setStyleSheet("QGroupBox { font-weight: bold; font-size: 18px } ")
        vbox = QVBoxLayout()
        tree_image = QLabel(self)
        tree_image.setPixmap(QPixmap('test.png'))
        tree_image.setMaximumWidth(650)
        tree_image.setMaximumHeight(550)
        tree_image.setMinimumWidth(650)
        tree_image.setMinimumHeight(550)
        self.progress = QProgressBar(self)
        self.progress.setMaximum(100)
        vbox.addWidget(tree_image)
        vbox.addWidget(self.progress)
        self.groupBox1.setLayout(vbox)

    def layout_buttons(self):
        self.button_row = QGroupBox()
        filler_label = QLabel(self)
        hbox = QHBoxLayout()
        exit_button = QPushButton('Terminate', self)
        self.refresh_button = QPushButton('Refresh', self)
        exit_button.setMaximumWidth(100)
        self.refresh_button.setMaximumWidth(100)
        exit_button.setStyleSheet(
            "border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;"
        )
        self.refresh_button.setStyleSheet(
            "border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;"
        )
        hbox.addWidget(exit_button)
        hbox.addWidget(self.refresh_button)
        hbox.addWidget(filler_label)
        exit_button.clicked.connect(self.quit_trigger)
        self.button_row.setLayout(hbox)
        
    def quit_trigger(self):
        sys.exit()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color:white;")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout_image()
        self.layout_buttons()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox1)
        vbox.addWidget(self.button_row)
        self.setLayout(vbox)


#if __name__ == "__main__":
#    App = QApplication(sys.argv)
#    Window = tree_analysis()
#    sys.exit(App.exec())
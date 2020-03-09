import sys
from initializer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect

class tree_analysis(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'ms2compare tree analysis'
        self.left = 600
        self.top = 250
        self.width = 650
        self.height = 550
        self.app_icon = QIcon("ms2compare.png")
        self.setWindowIcon(self.app_icon)
        self.setWindowTitle('ms2compare: Introduction')
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  # cancels out maximize option
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
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout_image()
        self.layout_buttons()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox1)
        vbox.addWidget(self.button_row)
        self.setLayout(vbox)
        self.show()

#if __name__ == "__main__":
#    App = QApplication(sys.argv)
#    Window = tree_analysis()
#    sys.exit(App.exec())
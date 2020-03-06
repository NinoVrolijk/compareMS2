
from initializer import *
from PyQt5.QtWidgets import *
import sys


class Tree_analysis (QMainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.window_specs()
        self.image_placement()
        self.create_button()
        self.reveal()


    def window_specs(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint) #cancels out maximize option
        self.app_icon = QIcon("ms2compare.png")
        self.setStyleSheet('background-color: white;')
        self.setWindowIcon(self.app_icon)

    def image_placement(self):
        self.tree_image = QLabel(self)
        self.tree_image.setPixmap(QPixmap('test.png'))
        self.tree_image.resize(1000,620)
        self.tree_image.move (200,10)

    def create_button(self):
        self.exit_button = QPushButton('Exit', self)
        self.return_button = QPushButton('Return', self)
        self.progress = QProgressBar(self)
        self.progress.move(250,550)
        self.progress.resize(600,30)
        self.progress.setMaximum(100)
        self.exit_button.setStyleSheet(
            "border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;"
        )
        self.return_button.setStyleSheet(
            "border-radius:7px; border: 2px solid ;font: bold; background-color: darkblue; color: white;border-color: white;"
        )
        self.return_button.move(130,550)
        self.exit_button.move(30,550)
        self.exit_button.clicked.connect(self.quit_trigger)

    def quit_trigger(self):
        sys.exit()


    def reveal(self):
        self.setWindowTitle('ms2compare: tree analysis')
        self.setGeometry(500, 300, 150, 150)  # Orientation of screen
        self.resize(1000, 620)  # Size of screen
        self.show()  # show screen


#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    window = Tree_analysis()
#    sys.exit(app.exec_())
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys


class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()

        self.image = QPushButton("non available")
        self.pixmap = QPixmap()
        self.pixmap.load("image.png")

        self.song_name = QLineEdit("Afraid of everyone")
        self.song_artist = QLineEdit("The national")
        self.song_album = QLineEdit("High Violet")

        self.song_1 = QLineEdit("1. Terrible Love")
        self.song_2 = QLineEdit("2. Sorrow")
        self.song_3 = QLineEdit("3. Anyone's Ghost")
        self.song_4 = QLineEdit("4. Little Faith")
        self.song_5 = QLineEdit("1. Arfraid of Evryone")
        self.song_6 = QLineEdit("6. Bloodbuzz Ohio")

        self.but_skip = QPushButton(">>")
        self.but_play = QPushButton(">")
        self.but_restart = QPushButton("<<")
        self.but_sound = QPushButton("mute")
        self.but_buy = QPushButton("BUY")
    

        layout_button = QHBoxLayout()
        layout_button.addWidget(self.but_skip)
        layout_button.addWidget(self.but_play)
        layout_button.addWidget(self.but_restart)


        slayout1 = QVBoxLayout()
        slayout1.addWidget(self.image)

        slayout2 = QVBoxLayout()
        slayout2.addWidget(self.song_name)
        slayout2.addWidget(self.but_sound)
        slayout2.addWidget(self.but_buy)
        self.but_sound.resize(1,1)
        self.but_sound.move(200,200)
        slayout2.addWidget(self.song_artist)
        slayout2.addWidget(self.song_album)
        slayout2.addLayout(layout_button)
    

        slayout3 = QVBoxLayout()
        slayout3.addWidget(self.song_1)
        slayout3.addWidget(self.song_2)
        slayout3.addWidget(self.song_3)
        slayout3.addWidget(self.song_4)
        slayout3.addWidget(self.song_5)
        slayout3.addWidget(self.song_6)



        layout = QHBoxLayout()
        layout.addLayout(slayout1)
        layout.addLayout(slayout2)
        layout.addLayout(slayout3)

        self.setLayout(layout)







if __name__ == '__main__' :


    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.move(600,400)
    widget.resize(500,200)
    widget.setMinimumWidth(150)
    widget.setMaximumWidth(1000)
    widget.setMinimumHeight(150)
    widget.setMaximumHeight(1000)
    widget.setWindowTitle("musique")
    widget.show()

    app.exec_() 

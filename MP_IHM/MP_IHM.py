import PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys


class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()

        #self.dark = "#3B3A44"

        self.image = QPushButton("non available")
        self.image.setFixedSize(100,100)
        self.pixmap = QPixmap()
        self.pixmap.load("image.png")

        self.song_name = QLabel("Afraid of everyone")
        self.song_artist = QLabel("The national")
        self.song_album = QLabel("High Violet")

        self.song_1 = QLabel("1. Terrible Love")
        self.song_2 = QLabel("2. Sorrow")
        self.song_3 = QLabel("3. Anyone's Ghost")
        self.song_4 = QLabel("4. Little Faith")
        self.song_5 = QLabel("1. Arfraid of Evryone")
        self.song_6 = QLabel("6. Bloodbuzz Ohio")
        self.rating = QLabel("Rating : 4/5")

        #self.scrolling = QScrollArea()
        #self.scrolling.setWidget(self.song1)
        #self.scrolling.setWidget(self.song2)
        #self.scrolling.setWidget(self.song3)
        #self.scrolling.setWidget(self.song4)
        #self.scrolling.setWidget(self.song5)
        #self.scrolling.setWidget(self.song6)

        self.but_skip = QPushButton(">>")
        self.but_play = QPushButton(">")
        self.but_restart = QPushButton("<<")
        self.but_sound = QPushButton("mute")
        self.but_sound.setFixedSize(40,20)
        self.but_buy = QPushButton("BUY")
        self.but_buy.setFixedSize(50,20)

        self.slider = QScrollBar()
    

        layout25 = QHBoxLayout()
        layout25.addWidget(self.but_skip)
        layout25.addWidget(self.but_play)
        layout25.addWidget(self.but_restart)
        layout25.setContentsMargins(0,0,100,0)

        layout21 = QHBoxLayout()
        layout21.addWidget(self.song_name)
        layout21.addWidget(self.but_sound)
        layout21.setSpacing(0)

        layout24 = QHBoxLayout()
        layout24.addWidget(self.rating)
        layout24.addWidget(self.but_buy)
        layout24.setSpacing(0)


        layout1 = QVBoxLayout()
        layout1.addWidget(self.image)
        layout1.setContentsMargins(5,0,10,10)

        layout2 = QVBoxLayout()
        layout2.addLayout(layout21)
        layout2.addWidget(self.song_artist)
        layout2.addWidget(self.song_album)
        layout2.addLayout(layout24)
        layout2.addLayout(layout25)
        layout2.setSpacing(0)
    

        layout3 = QVBoxLayout()
        layout3.addWidget(self.song_1)
        layout3.addWidget(self.song_2)
        layout3.addWidget(self.song_3)
        layout3.addWidget(self.song_4)
        layout3.addWidget(self.song_5)
        layout3.addWidget(self.song_6)
        layout3.addWidget(self.slider)
        layout3.setSpacing(0)



        layout = QHBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)

        self.setLayout(layout)

    def paintEvent(self, event: QPaintEvent):

        painter = QPainter(self)
        #painter.drawPixmap(0.0,self.pixmap)
        #painter.setBrush(QBrush(QColor(self.dark)))







if __name__ == '__main__' :


    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.move(600,400)
    widget.resize(500,200)
    widget.setFixedSize(500,120)
    widget.setWindowTitle("musique")
    widget.show()

    app.exec_() 

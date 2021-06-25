import PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys


class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()

        #blue = QColor()
        #blue.setNamedColor("blue")

        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pixmap = QPixmap()
        self.pixmap.load("C:/Users/maxim/Pictures/Saved Pictures/Tigre")
        self.pixmap = self.pixmap.scaled(100,100)

        self.song_name = QLabel("Afraid of everyone")
        self.song_artist = QLabel("The national")
        self.song_album = QLabel("High Violet")

        self.i = 3

        self.song_1 = QPushButton("1. Terrible Love")
        self.song_2 = QPushButton("2. Sorrow")
        self.song_3 = QPushButton("3. Anyone's Ghost")
        self.song_4 = QPushButton("4. Little Faith")
        self.song_5 = QPushButton("5. Arfraid of Evryone")
        self.song_6 = QPushButton("6. Bloodbuzz Ohio")
        self.rating = QLabel("Rating : 4/5")

        self.songs = QListWidget()
        self.songs.addItem("1. Terrible Love")
        self.songs.addItem("2. Sorrow")
        self.songs.addItem("3. Anyone's Ghost")
        self.songs.addItem("4. Little Faith")
        self.songs.addItem("5. Arfraid of Evryone")
        self.songs.addItem("6. Bloodbuzz Ohio")
        self.songs.setItemWidget(self.songs.item(0), self.song_1)
        self.songs.setItemWidget(self.songs.item(1), self.song_2)
        self.songs.setItemWidget(self.songs.item(2), self.song_3)
        self.songs.setItemWidget(self.songs.item(3), self.song_4)
        self.songs.setItemWidget(self.songs.item(4), self.song_5)
        self.songs.setItemWidget(self.songs.item(5), self.song_6)
        self.songs.setFixedSize(150,100)


        self.but_skip = QPushButton(">>")
        self.but_play = QPushButton(">")
        self.but_restart = QPushButton("<<")
        self.but_sound = QPushButton("mute")
        self.but_sound.setFixedSize(40,20)
        self.but_buy = QPushButton("BUY")
        self.but_buy.setFixedSize(50,20)

        layout11 = QHBoxLayout()
        layout11.addWidget(self.song_name)
        layout11.addWidget(self.but_sound)
        layout11.setSpacing(0)

        layout14 = QHBoxLayout()
        layout14.addWidget(self.rating)
        layout14.addWidget(self.but_buy)
        layout14.setSpacing(0)

        layout15 = QHBoxLayout()
        layout15.addWidget(self.but_restart)
        layout15.addWidget(self.but_play)
        layout15.addWidget(self.but_skip)
        layout15.setContentsMargins(0,0,100,0)

        layout1 = QVBoxLayout()
        layout1.addLayout(layout11)
        layout1.addWidget(self.song_artist)
        layout1.addWidget(self.song_album)
        layout1.addLayout(layout14)
        layout1.addLayout(layout15)
        layout1.setSpacing(0)
        layout1.setContentsMargins(110,0,0,0)

        layout2 = QVBoxLayout()
        layout2.addWidget(self.songs)
        layout2.setSpacing(0)

        layout = QHBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setLayout(layout)

        #Actions boutons

        self.song_1.clicked.connect(self.setSong_1)
        self.song_2.clicked.connect(self.setSong_2)
        self.song_3.clicked.connect(self.setSong_3)
        self.song_4.clicked.connect(self.setSong_4)
        self.song_5.clicked.connect(self.setSong_5)
        self.song_6.clicked.connect(self.setSong_6)
        self.but_skip.clicked.connect(self.NextSong)
        
        # Méthodes
    def NextSong(self):
        self.i = self.i+1
        self.song_name.setText(self.songs.item(self.i%6).text())
    
    def setSong_1 (self):
        self.i = 0
        self.song_name.setText(self.song_1.text())

    def setSong_2 (self):
        self.i = 1
        self.song_name.setText(self.song_2.text())

    def setSong_3 (self):
        self.i = 2
        self.song_name.setText(self.song_3.text())

    def setSong_4 (self):
        self.i = 3
        self.song_name.setText(self.song_5.text())

    def setSong_5 (self):
        self.i = 4
        self.song_name.setText(self.song_5.text())

    def setSong_6 (self):
        self.i = 5
        self.song_name.setText(self.song_6.text())
        

    def paintEvent(self, event : QPaintEvent) :

        painter = QPainter(self)
        painter.drawPixmap(10,10,self.pixmap)
        #pen_blue = QPen()
        #pen_blue.setColor(blue)
    
    #def mousePressEvent(self, event : QMouseEvent) :
        #print("hello")
        






if __name__ == '__main__' :


    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.move(500,400) #center
    #widget.move(1400,30) # High-right corner
    widget.resize(500,200)
    widget.setFixedSize(500,120)
    widget.setWindowTitle("musique")
    widget.show()

    app.exec_() 

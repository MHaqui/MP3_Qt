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

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pixmap = QPixmap()
        self.pixmap.load("C:/Users/maxim/Pictures/Saved Pictures/Tigre")
        self.pixmap = self.pixmap.scaled(100,100)

        self.song_name = QLabel("2. Sorrow")
        self.song_artist = QLabel("The national")
        self.song_album = QLabel("High Violet")
        self.rating = QLabel("Rating : 4/5")

        self.ind = 1
        self.run = True

        self.song_1 = QPushButton("1. Terrible Love")
        self.song_2 = QPushButton("2. Sorrow")
        self.song_3 = QPushButton("3. Anyone's Ghost")
        self.song_4 = QPushButton("4. Little Faith")
        self.song_5 = QPushButton("5. Arfraid of Evryone")
        self.song_6 = QPushButton("6. Bloodbuzz Ohio")
        
        self.list_songs = []
        self.list_songs.append(self.song_1)
        self.list_songs.append(self.song_2)
        self.list_songs.append(self.song_3)
        self.list_songs.append(self.song_4)
        self.list_songs.append(self.song_5)
        self.list_songs.append(self.song_6)

        self.Wsongs = QListWidget()
        for i in range(6):
            self.Wsongs.addItem(self.list_songs[i].text())
            self.Wsongs.setItemWidget(self.Wsongs.item(i), self.list_songs[i])
            self.list_songs[i].setStyleSheet("background-color : white")    
        self.Wsongs.setFixedSize(150,100)
        self.list_songs[self.ind].setStyleSheet("background-color : grey")

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
        layout2.addWidget(self.Wsongs)
        layout2.setSpacing(0)

        layout = QHBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setLayout(layout)
        x = 0

        #Actions boutons

        self.list_songs[0].clicked.connect(self.setSong_1)
        self.song_2.clicked.connect(self.setSong_2)
        self.song_3.clicked.connect(self.setSong_3)
        self.song_4.clicked.connect(self.setSong_4)
        self.song_5.clicked.connect(self.setSong_5)
        self.song_6.clicked.connect(self.setSong_6)
        self.but_skip.clicked.connect(self.NextSong)
        self.but_restart.clicked.connect(self.BefSong)  
        self.but_play.clicked.connect(self.Play)

        #Loading songs 
        #playlist = QMediaPlaylist()
        #playlist.addMedia(QUrl = FromLocalFile("C:/Users/maxim/Documents/Musique/MC_Solaar/MC Solaar/1. 11ème commandement.mp3"))
        #playlist.setCurrentIndex(1)

        #player = QMediaPlayer()
        #player.setPlaylist(playlist)

        #player.play();
        # Méthodes

    def Play(self):
        if self.run :
            self.run = False
            print("Stop")
        else:
            self.run = True
            print("Play")

    def BefSong(self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = (self.ind-1)%6
        self.song_name.setText(self.Wsongs.item(self.ind).text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")
        
    def NextSong(self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = (self.ind+1)%6
        self.song_name.setText(self.Wsongs.item(self.ind).text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")
    
    def setSong_1(self, x):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 0
        self.song_name.setText(self.list_songs[self.ind].text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")

    def setSong_2 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 1
        self.song_name.setText(self.song_2.text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")

    def setSong_3 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 2
        self.song_name.setText(self.song_3.text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")

    def setSong_4 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 3
        self.song_name.setText(self.song_4.text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")

    def setSong_5 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 4
        self.song_name.setText(self.song_5.text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")

    def setSong_6 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 5
        self.song_name.setText(self.song_6.text())
        self.list_songs[self.ind].setStyleSheet("background-color : grey")
        

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

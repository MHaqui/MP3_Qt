import PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtMultimedia import *
import sys


class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()

        folder = "C:/Users/maxim/Documents/Musique/MC_Solaar/MC Solaar/"
        self.ind = 0
        self.run = True

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pixmap = QPixmap()
        self.pixmap.load("C:/Users/maxim/Documents/Musique/MC_Solaar/MC Solaar/Cover Album MC Solaar")
        self.pixmap = self.pixmap.scaled(100,100)

        self.song_1 = QPushButton("1. 11ème commandement")
        self.song_2 = QPushButton("2. Galaktika")
        self.song_3 = QPushButton("3. La 5ème saison")
        self.song_4 = QPushButton("4. Perfect")
        self.song_5 = QPushButton("5. Les songes")
        self.song_6 = QPushButton("6. La vie n'est qu'un moment")
        
        self.list_songs = []
        self.list_songs.append(self.song_1)
        self.list_songs.append(self.song_2)
        self.list_songs.append(self.song_3)
        self.list_songs.append(self.song_4)
        self.list_songs.append(self.song_5)
        self.list_songs.append(self.song_6)

        self.Wsongs = QListWidget()
        for i in range(len(self.list_songs)):
            self.Wsongs.addItem(self.list_songs[i].text())
            self.Wsongs.setItemWidget(self.Wsongs.item(i), self.list_songs[i])
            self.list_songs[i].setStyleSheet("background-color : white")    
        self.Wsongs.setFixedSize(150,100)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

        self.song_name = QLabel(self.list_songs[self.ind].text())
        self.song_artist = QLabel("MC Solaar")
        self.song_album = QLabel("MC Solaar")
        self.rating = QLabel("Rating : 4.5/5")

        self.but_skip = QPushButton(">>")
        self.but_play = QPushButton(">")
        self.but_restart = QPushButton("<<")
        self.but_sound = QPushButton("mute")
        self.but_sound.setFixedSize(40,20)
        self.but_buy = QPushButton("BUY")
        self.but_buy.setFixedSize(50,20)

        #layout
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

        layout0 = QHBoxLayout()
        layout0.addLayout(layout1)
        layout0.addLayout(layout1)
        layout0.addLayout(layout2)

        self.setLayout(layout0)
        x = 0

        #Actions boutons

        self.list_songs[0].clicked.connect(self.setSong_1)
        self.list_songs[1].clicked.connect(self.setSong_2)
        self.list_songs[2].clicked.connect(self.setSong_3)
        self.list_songs[3].clicked.connect(self.setSong_4)
        self.list_songs[4].clicked.connect(self.setSong_5)
        self.list_songs[5].clicked.connect(self.setSong_6)
        self.but_skip.clicked.connect(self.NextSong)
        self.but_restart.clicked.connect(self.BefSong)  
        self.but_play.clicked.connect(self.Play)
        self.but_sound.clicked.connect(self.Mute)

        #Loading songs 
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QUrl(folder + "1. 11ème commandement.mp3"))
        self.playlist.addMedia(QUrl(folder + "2. galaktika.mp3"))
        self.playlist.addMedia(QUrl(folder + "3. La 5ème saison.mp3"))
        self.playlist.addMedia(QUrl(folder + "4. Perfect.mp3"))
        self.playlist.addMedia(QUrl(folder + "5. Les songes.mp3"))
        self.playlist.addMedia(QUrl(folder + "6. La vie n'est qu'un moment.mp3"))
        self.playlist.setCurrentIndex(self.ind)

        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play();

        # Méthodes

    def Play(self):
        if self.run :
            self.run = False
            self.player.pause()
            self.but_play.setText("||")
            print("Stop")
            
        else:
            self.run = True
            self.player.play()
            self.but_play.setText(">")
            print("Play")

    def BefSong(self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = (self.ind-1)%6
        self.song_name.setText(self.Wsongs.item(self.ind).text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")
        
    def NextSong(self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = (self.ind+1)%6
        self.song_name.setText(self.Wsongs.item(self.ind).text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")
    
    def setSong_1(self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 0
        self.song_name.setText(self.list_songs[self.ind].text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

    def setSong_2 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 1
        self.song_name.setText(self.song_2.text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

    def setSong_3 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 2
        self.song_name.setText(self.song_3.text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

    def setSong_4 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 3
        self.song_name.setText(self.song_4.text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

    def setSong_5 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 4
        self.song_name.setText(self.song_5.text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

    def setSong_6 (self):
        self.list_songs[self.ind].setStyleSheet("background-color : white")
        self.ind = 5
        self.song_name.setText(self.song_6.text())
        self.playlist.setCurrentIndex(self.ind)
        self.list_songs[self.ind].setStyleSheet("background-color : beige")

    def Mute(self):
        self.player.setMuted(not(self.player.isMuted()))
        
        #Paint event

    def paintEvent(self, event : QPaintEvent) :

        painter = QPainter(self)
        painter.drawPixmap(10,10,self.pixmap)
        
if __name__ == '__main__' :


    app = QApplication(sys.argv)

    widget = MyWidget()
    #widget.move(500,400) #center
    widget.move(1400,30) # High-right corner
    widget.resize(500,200)
    widget.setFixedSize(500,120)
    widget.setWindowTitle("musique")
    widget.show()

    app.exec_() 

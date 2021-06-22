import PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys

if __name__ == '__main__' :


    app = QApplication(sys.argv)

    image = QPushButton("non available")

    song_name = QLineEdit("Afraid of everyone")
    song_artist = QLineEdit("The national")
    song_album = QLineEdit("High Violet")

    song_1 = QLineEdit("1. Terrible Love")
    song_2 = QLineEdit("2. Sorrow")
    song_3 = QLineEdit("3. Anyone's Ghost")
    song_4 = QLineEdit("4. Little Faith")
    song_5 = QLineEdit("1. Arfraid of Evryone")
    song_6 = QLineEdit("6. Bloodbuzz Ohio")

    but_skip = QPushButton(">>")
    but_play = QPushButton(">")
    but_restart = QPushButton("<<")
    but_sound = QPushButton("mute")

    layout_button = QHBoxLayout()
    layout_button.addWidget(but_skip)
    layout_button.addWidget(but_play)
    layout_button.addWidget(but_restart)


    slayout1 = QVBoxLayout()
    slayout1.addWidget(image)

    slayout2 = QVBoxLayout()
    slayout2.addWidget(song_name)
    slayout2.addWidget(but_sound)
    slayout2.addWidget(song_artist)
    slayout2.addWidget(song_album)
    slayout2.addLayout(layout_button)
    

    slayout3 = QVBoxLayout()
    slayout3.addWidget(song_1)
    slayout3.addWidget(song_2)
    slayout3.addWidget(song_3)
    slayout3.addWidget(song_4)
    slayout3.addWidget(song_5)
    slayout3.addWidget(song_6)



    layout = QHBoxLayout()
    layout.addLayout(slayout1)
    layout.addLayout(slayout2)
    layout.addLayout(slayout3)
    

    widget = QWidget()
    widget.setLayout(layout)
    widget.move(600,400)
    widget.resize(500,200)
    widget.setMinimumWidth(150)
    widget.setMaximumWidth(1000)
    widget.setMinimumHeight(150)
    widget.setMaximumHeight(1000)
    widget.setWindowTitle("musique")

    widget.show()
    app.exec_() 

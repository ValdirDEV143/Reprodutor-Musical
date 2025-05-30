import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from play import Ui_MainWindow


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        self.player = QMediaPlayer(self)
        self.ui.pushButton_play1.clicked.connect(self.play)
        self.ui.pushButton_parar1.clicked.connect(self.parar)
        self.ui.pushButton_play2.clicked.connect(self.play2)
        self.ui.pushButton_parar2.clicked.connect(self.parar)
        self.ui.pushButton_play3.clicked.connect(self.play3)
        self.ui.pushButton_parar3.clicked.connect(self.parar)


    def play (self):
        caminho_musica = os.path.abspath("musicas/Aqui No Mar Yuri Chesman, Cast - The Little Mermaid - (De A Pequena Sereia).mp3")
        print("local da musica:", caminho_musica)
        

        url = QUrl.fromLocalFile(caminho_musica)

        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...")
        else:
            print("Erro: Caminho do arquivo inválido.")

    
    def play2 (self):
        caminho_musica = os.path.abspath("musicas/Faroeste Caboclo.mp3")
        print("local da musica:", caminho_musica)
        

        url = QUrl.fromLocalFile(caminho_musica)

        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...")
        else:
            print("Erro: Caminho do arquivo inválido.")

    def play3 (self):
            caminho_musica = os.path.abspath("musicas/Good luck babe.mp3")
            print("local da musica:", caminho_musica)
            

            url = QUrl.fromLocalFile(caminho_musica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")
            else:
                print("Erro: Caminho do arquivo inválido.")
    def parar (self):
        self.player.stop()
        print("A musica parou!")

        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())
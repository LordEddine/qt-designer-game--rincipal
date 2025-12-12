import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QMainWindow, QApplication 
from PyQt6.QtGui import QMovie


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("ui/PagePrincipale.ui",self)
        #self.setFixedSize(self.size())
        self.movie = QMovie("assets/bg1.gif")
        self.bglabel.setMovie(self.movie)


        self.movie.frameChanged.connect(self.taille_fenetre)
        self.movie.start()
        

        

        self.startGame.clicked.connect(lambda : print("Start Game"))
        self.quitterBtn.clicked.connect(self.close)
    
    def taille_fenetre(self):
        size = self.movie.currentPixmap().size()
        self.bglabel.setFixedSize(size)
        self.adjustSize()
        print(size)
        self.setFixedSize(size)

        layout_widget = self.verticalLayoutWidget
        layout_width = layout_widget.width()
        layout_height = layout_widget.height()
    
        center_x = (size.width() - layout_width) // 2
        center_y = (size.height() - layout_height) // 2
        
        layout_widget.move(center_x, center_y)

        self.movie.frameChanged.disconnect(self.taille_fenetre)

def load_qss(path:str) -> str:
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(load_qss("styles/style.qss"))
    window = HomePage()
    window.show()
    sys.exit(app.exec())
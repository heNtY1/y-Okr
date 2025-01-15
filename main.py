import sys
from random import randint
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Git(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.sps = []

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        if self.flag:
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.flag = False

    def draw_flag(self, qp):
        x, y = randint(0, 560), randint(0, 420)
        r = randint(0, 200)
        self.sps.append((x, y, r))
        qp.setBrush(QColor(255, 255, 0))
        for i in self.sps:
            qp.drawEllipse(i[0], i[1], i[2], i[2])

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Git()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

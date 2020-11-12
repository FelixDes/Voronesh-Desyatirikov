import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWIdget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.test = None
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.test = True
        self.update()

    def paintEvent(self, event):
        if self.test:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        self.radius = randint(0, self.height())
        self.x, self.y = randint(0, self.width()), randint(0, self.height())
        qp.drawEllipse(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.test = None


app = QApplication(sys.argv)
ex = MyWIdget()
ex.show()
sys.exit(app.exec())

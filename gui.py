# coding:utf-8

import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class Preview(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 初期化
    def initUI(self):
        btn1 = QPushButton("Preview", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Stop", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonPreviewClicked)
        btn2.clicked.connect(self.buttonStopClicked)

        self.statusBar()

        self.setWindowTitle('Player')
        self.show()

    def buttonPreviewClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Push Button01')

    def buttonStopClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Push Button02')

class ImageWidget(QtWidgets.QWidget):
  def __init__(self, image):
    super(ImageWidget, self).__init__()
    self.image = image

  def paintEvent(self, event):
    painter = QtGui.QPainter(self)
    if self.image is None:
      painter.setPen(QtCore.Qt.black)
      painter.setBrush(QtCore.Qt.black)
      painter.drawRect(0, 0, self.width(), self.height())
      return
    pixmap = create_QPixmap(self.image)
    painter.drawPixmap(0, 0, self.image.shape[1], self.image.shape[0], pixmap)

  def set_image(self, image):
    self.image = image
    self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Preview()
    win.resize(640, 480)
    sys.exit(app.exec_())
from PySide2.QtGui import QPixmap, QIcon, QFont, QDoubleValidator, QValidator, QImage
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QDesktopWidget, QPushButton, QLineEdit, QComboBox
from PySide2 import QtWidgets
import sys
import time
import pytesseract
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


class MyWindow (QMainWindow):

    def __init__(self):
        super (MyWindow, self).__init__ ()

        self.init_ui ()

    def init_ui(self):
        self.title = "Task2"
        self.setWindowTitle (self.title)
        self.setGeometry (300, 200, 250, 250)
        self.setFixedSize (750, 750)

        self.label1 = QtWidgets.QLabel (self)
        pixmap = QPixmap ('macro.jpg')
        self.label1.setPixmap (pixmap)
        self.label1.setGeometry (50, -300, 1000, 800)

        self.label2 = QtWidgets.QLabel (self)
        pixmap = QPixmap ('schem.JPG')
        self.label2.setPixmap (pixmap)
        self.label2.setGeometry (130, 30, 500, 700)

        self.choose_button = QtWidgets.QPushButton (self)
        self.choose_button.setText ("choose")
        self.choose_button.setFont (QFont ('Arial', 10))
        self.choose_button.setGeometry (560, 600, 120, 30)
        self.choose_button.setStyleSheet ("background-color: white")
        self.choose_button.clicked.connect (self.btn_click)

        self.combo = QComboBox (self)
        self.combo.setWindowTitle ("enter")
        self.combo.setGeometry (130, 600, 120, 40)
        self.combo.setFont (QFont ('Arial', 10))
        self.combo.addItems (["M1", "M2", "M3", "M4", "M5"])

        self.textError = QtWidgets.QLabel (self)
        self.textError.setFont (QFont ('Times', 12))
        self.textError.setGeometry (560, 550, 120, 30)
        self.textError.setStyleSheet ("color: red")

        self.setIcon ()
        self.center ()

    def setIcon(self):
        appIcon = QIcon ("macro.JPG")
        self.setWindowIcon (appIcon)

    def center(self):

        qReact = self.frameGeometry ()
        centerpoint = QDesktopWidget ().availableGeometry ().center ()
        qReact.moveCenter (centerpoint)
        self.move (qReact.topLeft ())

    def btn_click(self):

        text = self.combo.currentText ()
        filtered_image = self.image_correct ("schem.JPG")
        h, w, _ = filtered_image.shape  # assumes color image
        boxes = pytesseract.image_to_boxes (filtered_image)

        if text == "M1":
            img = cv2.rectangle (filtered_image, (214, 155), (250, 175),
                                 (0, 255, 0), 2)
            img = cv2.rectangle (filtered_image, (175, 155), (214, 175),
                                 (0, 255, 0), 2)


        elif text == "M2":

            img = cv2.rectangle (filtered_image, (25, 245), (66, 265),
                                 (0, 255, 0), 2)
            img = cv2.rectangle (filtered_image, (360, 245), (400, 265),
                                 (0, 255, 0), 2)


        elif text == "M3":
            img = cv2.rectangle (filtered_image, (25, 187), (66, 207),
                                 (0, 255, 0), 2)
            img = cv2.rectangle (filtered_image, (360, 187), (400, 207),
                                 (0, 255, 0), 2)


        elif text == "M4":
            img = cv2.rectangle (filtered_image, (25, 107), (66, 127),
                                 (0, 255, 0), 2)
            img = cv2.rectangle (filtered_image, (360, 107), (400, 127),
                                 (0, 255, 0), 2)


        elif text == "M5":
            img = cv2.rectangle (filtered_image, (25, 62), (66, 82),
                                 (0, 255, 0), 2)
            img = cv2.rectangle (filtered_image, (360, 62), (400, 82),
                                 (0, 255, 0), 2)




        rgb_array = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_array.shape
        bytesPerLine = ch * w
        qImg = QImage (rgb_array.data, w, h, bytesPerLine, QImage.Format_RGB888)
        self.label2.clear ()
        self.label2.setPixmap (QPixmap.fromImage (qImg))
        self.label2.setGeometry (130, 30, 500, 700)

    def image_correct(self, string):

        img = cv2.imread (string)
        h, w, _ = img.shape  # assumes color image
        sharpening_filter = np.array ([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened_imag = cv2.filter2D (img, -1, sharpening_filter)

        return sharpened_imag


app = QApplication (sys.argv)
w = MyWindow ()
w.show ()
time.sleep (5)
w.resize (700, 700)
sys.exit (app.exec_ ())

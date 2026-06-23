import random as ran
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSpinBox, QLineEdit
from PyQt5.QtGui import *

def create_label(window, text, font, width, height, x, y):
    lbl = QLabel(window)
    lbl.setText(text)
    lbl.setFont(font)
    lbl.resize(width, height)
    lbl.move(x, y)
    lbl.show()
    return lbl

def create_button(window, text, font, width, height, x, y, function):
    btn = QPushButton(window)
    btn.setText(text)
    btn.setFont(font)
    btn.resize(width, height)
    btn.move(x, y)
    btn.clicked.connect(function)
    btn.show()
    return btn

def create_spinbox(window, font, width, height, x, y, range_bottom, range_top, value_start):
    spb = QSpinBox(window)
    spb.setFont(font)
    spb.move(x, y)
    spb.resize(width, height)
    spb.setRange(range_bottom, range_top)
    spb.setValue(value_start)
    spb.show()
    return spb

def create_inputbox(window, placeholder_text, font, width, height, x, y):
    ipb = QLineEdit(window)
    ipb.setPlaceholderText(placeholder_text)
    ipb.setFont(font)
    ipb.move(x, y)
    ipb.resize(width, height)
    ipb.show()
    return ipb

def ee(self):
    pass 

def main():
    global win, health
    health = 100
    app = QApplication(sys.argv) 
    win = QMainWindow()           
    win.setGeometry(600, 400, 700, 450) 
    win.setWindowTitle("Что-то") 
    health_label = create_label(win, f"Здоровье: {health}/100", QFont('Arial', 14), 200, 30, 100, 100)
    but = create_button(win, "Кнопка", QFont('Arial', 14), 100, 100, 200, 200, ee)
    but.setIcon(QIcon('image.jpg'))
    win.show()        
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()             

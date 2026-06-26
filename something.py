import random as ran
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSpinBox, QLineEdit, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize
import servants_list as s_l

your_servant = s_l.summon()

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

def attack(self):
    global mana, mana_label
    mana -= your_servant.mana_consumption
    if mana % 1 == 0:
        mana = int(mana)
    mana_label.hide()
    mana_label = create_label(win, f"Мана:{mana}/1000", QFont('Arial', 16), 175, 40, 300, 500)

def a(self):
    global win
    new_win = QDialog(win)
    new_win.setWindowTitle("Параметры слуги")
    new_win.resize(350, 550)
    new_win.move(1300, 270)
    label = create_label(new_win, f"Имя: {your_servant.name}", QFont('Arial', 16), 350, 40, 0, 0)
    label = create_label(new_win, f"Сила: {your_servant.convert_back(your_servant.strength)}", QFont('Arial', 16), 350, 40, 0, 40)
    label = create_label(new_win, f"Выносливость: {your_servant.convert_back(your_servant.endurance)}", QFont('Arial', 16), 350, 40, 0, 80)
    label = create_label(new_win, f"Ловкость: {your_servant.convert_back(your_servant.agility)}", QFont('Arial', 16), 350, 40, 0, 120)
    label = create_label(new_win, f"Мана: {your_servant.convert_back(your_servant.mana)}", QFont('Arial', 16), 350, 40, 0, 160)
    label = create_label(new_win, f"Удача: {your_servant.convert_back(your_servant.luck)}", QFont('Arial', 16), 350, 40, 0, 200)
    label = create_label(new_win, f"Фантазм: {your_servant.convert_back(your_servant.np)}", QFont('Arial', 16), 350, 40, 0, 240)
    label = create_label(new_win, f"Навыки: {your_servant.class_skill_1} {your_servant.convert_back(your_servant.class_skill_1_rank)}", QFont('Arial', 16), 350, 40, 0, 280)
    label = create_label(new_win, f"{your_servant.class_skill_2} {your_servant.convert_back(your_servant.class_skill_2_rank)}", QFont('Arial', 16), 350, 40, 85, 320)
    label = create_label(new_win, "Текст", QFont('Arial', 16), 200, 40, 0, 360)
    new_win.show()

def main():
    global app, win, health, mana, mana_label
    current_health = your_servant.health
    mana = 1000
    app = QApplication(sys.argv) 
    win = QMainWindow()           
    win.setGeometry(500, 300, 800, 550) 
    win.setWindowTitle("Что-то") 
    health_label = create_label(win, f"Здоровье слуги: {current_health}/{your_servant.health}", QFont('Arial', 16), 300, 40, 0, 500)
    mana_label = create_label(win, f"Мана:{mana}/1000", QFont('Arial', 16), 175, 40, 300, 500)
    stats_button = create_button(win, "Характеристики слуги", QFont('Arial', 16), 250, 40, 475, 500, a)
    but = create_button(win, "", QFont('Arial', 14), 100, 100, 0, 400, attack)
    but.setIcon(QIcon('Attack.png'))
    but.setIconSize(QSize(100, 100))
    win.show()        
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()             

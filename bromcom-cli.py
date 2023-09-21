#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from bs4 import BeautifulSoup
from os import system
import sys

system("curl -s 'https://www.bromcomvle.com/Homework'")
page = open("page.txt")
soup = BeautifulSoup(page.read(), "html.parser")

table = soup.find(id="HomeworkTable")
items = table.find_all("td")
homework = [[" " for column in range(8)] for row in range(len(items) // 10)]
for i in range(len(items) // 10):
    for j in range(8):
        homework[i][j] = items[j + (i * 10)].text.strip()
for row in homework:
    row.pop(1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        table = QTableWidget()
        table.setRowCount(len(homework))
        table.setColumnCount(len(homework[0]))
        table.setColumnWidth(1, 300)
        table.setColumnWidth(6, 200)

        for i, row in enumerate(homework):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                table.setItem(i, j, item)

        self.setWindowIcon(QIcon("/opt/bromcom/favicon.jpg"))
        self.setWindowTitle("My Homework")
        self.resize(1021, 500)
        self.setCentralWidget(table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())

import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class EspressoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.titles = [elem[0] for elem in cur.description]
        for i, elem in enumerate(data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    espresso_window = EspressoWindow()
    espresso_window.show()
    sys.exit(app.exec())

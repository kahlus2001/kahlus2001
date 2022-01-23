"""Graphical calculator program: the main entry point.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""
from gui import GUI
from PyQt5 import QtWidgets
import sys

# Don't execute this if file is imported
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec_()



"""Graphical calculator program: the GUI.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
from math_functions import *
from PyQt5 import QtCore


class GraphInputWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        """Initializer of the GraphWindow class."""
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        # label printing possible errors and graph plotting status
        self.status_label = QtWidgets.QLabel("Graph status", self)
        layout.addWidget(self.status_label)
        self.status_label.setGeometry(10, 20, 390, 40)
        self.status_label.setFont(QFont('Arial', 10))
        self.status_label.setStyleSheet("QLabel { background-color : black; color : white; }")

        # input fields for user parameters
        self.input_label = QtWidgets.QLabel("y = ", self)
        layout.addWidget(self.input_label)
        self.input_label.setGeometry(10, 70, 50, 40)
        self.input_function = QLineEdit("Input function, use numpy notation", self)
        layout.addWidget(self.input_function)
        self.input_lower = QLineEdit("Input lower x-bound", self)
        layout.addWidget(self.input_lower)
        self.input_upper = QLineEdit("Input upper x-bound", self)
        layout.addWidget(self.input_upper)

        # input geometry
        self.input_function.setGeometry(40, 70, 220, 40)
        self.input_lower.setGeometry(10, 110, 125, 40)
        self.input_upper.setGeometry(135, 110, 125, 40)

        # confirm button
        confirm_button = QtWidgets.QPushButton('Confirm', self)
        layout.addWidget(confirm_button)
        confirm_button.clicked.connect(self.draw_graph)
        confirm_button.setGeometry(280, 80, 120, 60)

        self.setWindowTitle('Function Plotter')

    def draw_graph(self) -> None:
        """Draw graph from user input."""
        try:
            message = plot(self.input_function.text(), float(self.input_lower.text()), float(self.input_upper.text()))
            self.status_label.setText(message)
        except Exception:
            self.status_label.setText('Cannot plot function. Invalid input. Please try again.')


class QuadraticWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        """Initializer of the QuadraticWindow class."""
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        # result and message window
        self.roots_label = QtWidgets.QLabel("Solve quadratic equation in the form 0=a*x^2+b*x+c:", self)
        layout.addWidget(self.roots_label)
        self.roots_label.setGeometry(5, 10, 400, 30)
        self.roots_label.setFont(QFont('Arial', 10))
        self.roots_label.setStyleSheet("QLabel { background-color : black; color : white; }")

        # user input fields
        self.zero = QtWidgets.QLabel("0 = ", self)
        layout.addWidget(self.zero)
        self.a = QLineEdit("a", self)
        layout.addWidget(self.a)
        self.xSquared = QtWidgets.QLabel("x^2+ ", self)
        layout.addWidget(self.xSquared)
        self.b = QLineEdit("b", self)
        layout.addWidget(self.b)
        self.x = QtWidgets.QLabel("x+ ", self)
        layout.addWidget(self.x)
        self.c = QLineEdit("c", self)
        layout.addWidget(self.c)

        # geometry
        self.zero.setGeometry(100, 50, 20, 20)
        self.a.setGeometry(120, 50, 50, 20)
        self.xSquared.setGeometry(175, 50, 30, 20)
        self.b.setGeometry(210, 50, 50, 20)
        self.x.setGeometry(265, 50, 20, 20)
        self.c.setGeometry(285, 50, 50, 20)

        # confirm button
        solve_button = QtWidgets.QPushButton('Solve equation', self)
        layout.addWidget(solve_button)
        solve_button.clicked.connect(self.solve)
        solve_button.setGeometry(160, 80, 90, 25)

        self.setWindowTitle('Solve Quadratic Equation')

    def solve(self) -> None:
        """Call find_roots function."""
        try:
            roots = find_roots(float(self.a.text()), float(self.b.text()), float(self.c.text()))
            self.roots_label.setText(roots)
        except Exception:
            self.roots_label.setText(' Invalid input. Cannot solve. Try again.')


class GUI(QtWidgets.QMainWindow):
    """A class where Graphical User Interface is made using PyQt5 module."""

    def __init__(self) -> None:
        """Initializer of the GUI class"""
        super().__init__()
        main = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        # create buttons in grid pattern
        names = ['C', 'AC', '(', ')', 'graph',
                 '7', '8', '9', '/', 'solve_quad',
                 '4', '5', '6', '*', 'mod',
                 '1', '2', '3', '^', 'sqrt',
                 '0', '.', '-', '+', '=']

        positions = [(i, j) for i in range(2, 7) for j in range(5)]
        button = []
        count = 0

        for position, name in zip(positions, names):
            if name == '':
                continue
            button.append(name)
            button[count] = QtWidgets.QPushButton(name, self)
            layout.addWidget(button[count], *position)
            count += 1

        # assign methods to buttons
        functions = [self.undo, self.clear_all, lambda: self.add('('), lambda: self.add(')'), self.graph,
                     lambda: self.add('7'), lambda: self.add('8'),
                     lambda: self.add('9'), lambda: self.add('/'), self.solve_quad, lambda: self.add('4'),
                     lambda: self.add('5'), lambda: self.add('6'), lambda: self.add('*'),
                     lambda: self.add('%'), lambda: self.add('1'), lambda: self.add('2'),
                     lambda: self.add('3'), lambda: self.add('**'), lambda: self.add('**0.5'), lambda: self.add('0'),
                     lambda: self.add('.'), lambda: self.add('-'), lambda: self.add('+'), self.equals]

        for index, function in enumerate(functions):
            button[index].clicked.connect(function)

        # stored values:
        self.expression = ''
        self.result = ''
        self.check = False

        # create displays as label
        self.previous = QtWidgets.QLabel('', self)
        layout.addWidget(self.previous, 0, 0, 1, 5)
        self.previous.setFont(QFont('Arial', 20))
        self.previous.setStyleSheet("QLabel { background-color : black; color : white; }")

        self.display = QtWidgets.QLabel('', self)
        layout.addWidget(self.display, 1, 0, 1, 5)
        self.display.setFont(QFont('Arial', 20))
        self.display.setStyleSheet("QLabel { background-color : black; color : white; }")
        self.display.setAlignment(QtCore.Qt.AlignRight)

        # position window on screen, set title, show window.
        self.move(300, 150)
        self.setWindowTitle('Graphical Calculator')
        self.show()

    def update(self) -> None:
        """Update display of calculator.
        """

        self.previous.setText(self.expression)
        self.display.setText(self.result)
        if self.check:
            self.expression = self.result
            self.check = False
        if self.result == "Invalid Input":
            self.result, self.expression = '', ''


    def graph(self) -> None:
        """Initialize graph window.
        """
        self.graph = GraphInputWindow()
        self.graph.show()

    def solve_quad(self) -> None:
        """Initialize quadratic solver window.
        """
        self.solve_quad = QuadraticWindow()
        self.solve_quad.show()

    def add(self, x: str) -> None:
        """Concatenate symbol on button to expression.
        """
        self.expression = self.expression + x
        self.update()

    def equals(self) -> None:
        """Call evaluate() to numerically solve expression.
        """
        new_expression = evaluate(self.expression, self.result)
        # safety if else statement.
        if new_expression == 'invalid input':
            self.expression = ''
        else:
            self.result = str(new_expression)
            self.check = True
            self.update()

    def clear_all(self) -> None:
        """Clear expression input.
        """
        self.expression = ''
        self.result = ''
        self.update()

    def undo(self) -> None:
        """Remove last character from expression.
        """
        self.expression = self.expression[:-1]
        self.update()

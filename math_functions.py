"""Graphical calculator program: the math functions.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""

from typing import Any
import math
import numpy as np
import matplotlib.pyplot as plt


def evaluate(expression: str, result: str) -> Any:
    """Evaluate mathematical expression provided by user when '=' button clicked.
    >>> evaluate('2*3', '')
    6
    >>> evaluate('3/3', '')
    1.0
    >>> evaluate('1/0', '')
    'Invalid Input'
    """
    try:
        return eval(expression)
    except Exception:
        result = 'Invalid Input'
        return result


def plot(formula: str, x1: float, x2: float) -> Any:
    """Plot graph using user input function using matplotlib and numpy.
    """
    i = True
    while i:
        try:
            x = np.arange(x1, x2+0.1, 0.1)
            y = eval(formula)
            plt.plot(x, y)
            plt.title(f"graph of y={formula}")
            plt.show()
            i = False
            return 'Graph plotted!'
        except Exception:
            i = False
            return 'Cannot plot function. Invalid input. Please try again.'


def find_roots(a: float, b: float, c: float) -> str:
    """Find roots of quadratic polynomial.

    :examples:
    >>> find_roots(1, 4, 2)
    'Roots: x=-3.414213562373095 and x=-0.5857864376269049'
    >>> find_roots(1, 4, 4)
    'Double root: x=-2.0'
    >>> find_roots(2, 2, 2)
    'No real roots.'
    >>> find_roots(0, 2, 2)
    'Equation is not quadratic. Try again.'
    """
    delta = b ** 2 - 4 * a * c
    if int(a) == 0:
        return str('Equation is not quadratic. Try again.')
    if delta > 0:
        x1 = (- b - math.sqrt(delta)) / 2 * a
        x2 = (- b + math.sqrt(delta)) / 2 * a
        roots = [x1, x2]
        return str(f'Roots: x={roots[0]} and x={roots[1]}')
    if delta == 0:
        x = - b / 2 * a
        roots = [x]
        return str(f'Double root: x={roots[0]}')
    else:
        return 'No real roots.'





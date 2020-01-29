# Problem One
""" Quadratic Equation Problem
Details: Have a while loop, prompt user for values a,b, check for valid float numbers, generate x1 and x2 as below:
if b**2 - 4ac < 0 then no real sol
if  = 0 then one solution, display x1 (exclusive)
if > 0 then two sol, display x1,x2
quit by type a key
after generate x1 and x2
display graph using matplotlib.pyplot module"""
import math
import numpy as np
import matplotlib.pyplot as plt

start = True
while start:
    # read coefficents from the terminal
    a = input('Enter a: ')
    if a == '':
        break
    b = input('Enter b: ')
    c = input('Enter c: ')
    if b == '' or c == '':
        b = 0
        c = 0
        pass
    # convert back
    a = float(a)
    b = float(b)
    c = float(c)

    # calculate
    formula_one = (b ** 2) - (4 * a * c)
    x1 = (-b - math.sqrt(abs(formula_one))) / (2 * a)
    x2 = (-b + math.sqrt(abs(formula_one))) / (2 * a)
    # if formula_one < 0 there are complex number => no real solutions
    if formula_one < 0:
        print('no real solutions')
        x_opt = - b / (2 * a)
        n = 150
        x_range = np.linspace(x_opt - 5, x_opt + 5, n)
        y_range = (a * (pow(x_range, 2))) + (b * x_range) + c   # plot every numbers of x_range list to calculate y_range
        plt.plot(x_range, y_range, 'bx-')
        plt.axhline(linewidth=1, color='k')
        plt.axvline(linewidth=1, color='k')
        plt.xlim(x_opt - 6, x_opt + 6)
        plt.ylim(0,)
        print('Please close the graph to continue')
        plt.show()
    elif formula_one > 0:
        print('two solutions: x1 = {0}, x2 = {1}'.format(x1, x2))
        # graph
        x_min = x1 - 5
        x_max = x2 + 5
        n = 150
        x_range = np.linspace(x_min, x_max, n)
        y_range = (a * (pow(x_range, 2))) + (b * x_range) + c
        plt.plot(x_range, y_range, 'bx-')
        plt.axhline(linewidth=1, color='k')
        plt.axvline(linewidth=1, color='k')
        plt.xlim(x_min - 1, x_max + 1)
        print('Please close the graph to continue')
        plt.show()
    else:
        print('one solution: {}'.format(x1))
        # graph
        n = 150
        x_range = np.linspace(x1 - 5, x1 + 5, n)
        y_range = (a * (pow(x_range, 2))) + (b * x_range) + c
        plt.plot(x_range, y_range, 'bx-')
        plt.axhline(linewidth=1, color='k')
        plt.axvline(linewidth=1, color='k')
        plt.xlim(x1 - 6, x1 + 6)
        print('Please close the graph to continue')
        plt.show()

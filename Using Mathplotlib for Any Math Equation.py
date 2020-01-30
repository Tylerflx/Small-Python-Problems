"""Problem 4 using mathplotlib to graph an interactive function from user input
 , sample number, xmin, xmax
 using eval() function to calculate string as equation"""
import matplotlib.pyplot as plt
import numpy as np
import math


def plot_function(fun_str, x_min, x_max, ns):
    xs = np.linspace(x_min, x_max, ns)
    ys = []
    print('{:>5} {:>15}'.format('x', 'y'))
    print('_________________________')
    for each_x in xs:
        x = round(float(each_x), 4)
        y = round(eval(fun_str), 4)
        ys.append(y)
        # display the table
        if x >= 0:
            x = '{:+.4f}'.format(x)
        else:
            x = '{:-.4f}'.format(x)
        if y >= 0:
            y = '{:+.4f}'.format(y)
        else:
            y = '{:-.4f}'.format(y)

        print('{0}\t\t\t{1}'.format(x, y))

    # display graph
    plt.title('{}'.format(fun_str))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(x_min, x_max)
    plt.plot(xs, ys, 'bo-')
    plt.show()


input_str = input('Enter function with variable x: ')
num = int(input('Enter number of samples: '))
xs_min = float(input('Enter xmin: '))
xs_max = float(input('Enter xmax: '))
plot_function(input_str, xs_min, xs_max, num)

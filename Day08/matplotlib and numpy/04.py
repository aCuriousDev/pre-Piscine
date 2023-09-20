import numpy as np
import matplotlib.pyplot as plt
import math


def plot_fct(func, start, end, title):
    # Generate x values
    x = np.linspace(start, end, 400)

    # Compute y values using the provided function
    y = [func(i) for i in x]

    # Create a new figure window
    plt.figure()

    # Plot the function
    plt.plot(x, y)

    # Add title, labels, and grid
    plt.title(title)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)

# Example usage


def f(x):
    return x**2 + x*3 + 2


plot_fct(math.sin, 0, 50, 'sin(x)')
plot_fct(f, -100, 200, 'x^2 + 3x + 2')
plot_fct(lambda x: x**2, -10, 10, 'x^2')
plot_fct(lambda x: 1/x, -100, 100, '1/x')

# Display all the plots
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import math


def plot_fct(func, start, end):
    # Generate x values
    x = np.linspace(start, end, 400)

    # Compute y values using the provided function
    y = [func(i) for i in x]

    # Plot the function
    plt.plot(x, y)

    # Add title, labels, and grid
    plt.title('Function Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)

    # Display the plot
    plt.show()

# Example usage


def f(x):
    return x**2 + x*3 + 2


plot_fct(math.sin, 0, 50)
plot_fct(f, -100, 200)
plot_fct(lambda x: x**2, -10, 10)
plot_fct(lambda x: 1/x, -100, 100)

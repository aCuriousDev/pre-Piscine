import numpy as np
import matplotlib.pyplot as plt

def display_points(points):
    # Extracting x and y coordinates from the points
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])

    # Create the plot
    plt.scatter(x, y, color='red', label='Data Points')  # Using scatter for displaying individual points

    # Add title and labels
    plt.title('Data Points Chart')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()

    # Display the grid
    plt.grid(True)

    # Display the plot
    plt.show()

# Example usage:
points = [(0, 12), (1, 32), (2, 42), (3, 52)]
display_points(points)

import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([0, 1, 2, 3])
y = np.array([12, 32, 42, 52])

# Create the plot
plt.plot(x, y, 'o', label='Data Points', color='red')

# Add title and labels
plt.title('Data Point Chart')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()

# Display the grid
plt.grid(True)

# Display the plot
plt.show()

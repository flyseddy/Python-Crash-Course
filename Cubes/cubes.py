"""
Author: Sedrick Thomas
Created: April 2020
Excercise 15-1: Cubes
"""
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Sets the title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubed Values", fontsize=14)

# Sets the range for each axis.
ax.axis([0, 5100, 0, 125000000000])

plt.show()

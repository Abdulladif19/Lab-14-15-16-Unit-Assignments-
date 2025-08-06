"""
Program Name: Lab14_abdulladif.py
Author: Abdulladif
Purpose: This program plots the graph of the function sin(h)/h, sine and then uses matplotlib to visualize the function.
Date: 8/6/2025

"""

import math
import matplotlib.pyplot as plt

# Generate x values
x_values = [x * 0.1 for x in range(-100, 101)]  

# Calculate y = sin(h)/h
y_values = []
for h in x_values:
    if h == 0:
        y = 1  
    else:
        y = math.sin(h) / h
    y_values.append(y)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='sin(h)/h', color='purple', linewidth=2, linestyle='--')
plt.title("Plot of sin(h)/h (Sinc Function)")
plt.xlabel("h")
plt.ylabel("sin(h)/h")
plt.grid(True)
plt.legend()
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.show()

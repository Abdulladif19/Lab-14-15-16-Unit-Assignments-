"""
Program Name: Lab15_abdulladif.py
Author: Abdulladif
Purpose: The program reads the national unemployment data from a CSV file called 'OHUR.csv', analyzes the header using enumerate(),
         and plots the unemployment rate over time using matplotlib.
Date: 2025-08-08
"""

import pandas as pd
import matplotlib.pyplot as plt

filename = 'OHUR.csv'

with open(filename) as file:
    for i, line in enumerate(file):
        print(f"Line {i}: {line.strip()}")
        if i == 4:
            break

df = pd.read_csv(filename)


print("Columns:", df.columns)


df['DATE'] = pd.to_datetime(df['DATE'])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['DATE'], df['OHUR'], color='blue', linewidth=1.5)
plt.title('US Unemployment Rate')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

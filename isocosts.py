import numpy as np
import matplotlib.pyplot as plt

# Define parameters
w = 10  # Wage rate
r = 20  # Rental rate of capital
C_values = [50, 100, 150]  # Different total cost levels

# Define range of inputs (labor and capital)
L_range = np.linspace(1, 10, 100)  # Labor input range
K_range = np.linspace(1, 10, 100)  # Capital input range

# Calculate isocost lines for different levels of total cost
isocosts = []
for C in C_values:
    isocost = (C / w) - (r / w) * K_range
    isocosts.append(isocost)

# Plotting
plt.figure(figsize=(8, 6))

for i, isocost in enumerate(isocosts):
    plt.plot(K_range, isocost, label=f'Isocost C={C_values[i]}')

plt.xlabel('Capital (K)')
plt.ylabel('Labor (L)')
plt.title('Isocost Lines')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the Cobb-Douglas production function
alpha = 0.5  # Output elasticity of labor
beta = 0.3   # Output elasticity of capital
A = 1        # Constant factor

# Define range of inputs (labor and capital)
L_range = np.linspace(1, 10, 100)  # Labor input range
K_range = np.linspace(1, 10, 100)  # Capital input range

# Calculate isoquants for different levels of output
output_levels = [2, 4, 6]  # Different output levels
isoquants = []
for Q in output_levels:
    isoquant = (Q / A) ** (1 / alpha) / K_range ** (beta / alpha)
    isoquants.append(isoquant)

# Plotting
plt.figure(figsize=(8, 6))

for i, isoquant in enumerate(isoquants):
    plt.plot(K_range, isoquant, label=f'Isoquant {output_levels[i]}')

plt.xlabel('Capital (K)')
plt.ylabel('Labor (L)')
plt.title('Isoquants')
plt.legend()
plt.grid(True)
plt.show()

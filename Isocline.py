import numpy as np
import matplotlib.pyplot as plt

# Define the functions f(x, y) and g(x, y) that describe the dynamics of the system
def f(x, y):
    return x - x**3 - y

def g(x, y):
    return x + y - y**3

# Define the range of x and y values
x_range = np.linspace(-2, 2, 100)
y_range = np.linspace(-2, 2, 100)

# Calculate the isoclines by setting the derivatives equal to zero
isocline_x = np.zeros_like(y_range)
isocline_y = np.zeros_like(x_range)

for i, y in enumerate(y_range):
    isocline_x[i] = x_range[np.argmin(np.abs(f(x_range, y)))]

for i, x in enumerate(x_range):
    isocline_y[i] = y_range[np.argmin(np.abs(g(x, y_range)))]

# Plotting
plt.figure(figsize=(8, 6))

plt.plot(isocline_x, y_range, label='Isocline for dx/dt = 0', color='blue')
plt.plot(x_range, isocline_y, label='Isocline for dy/dt = 0', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Isoclines for Autonomous 2-State System')
plt.legend()
plt.grid(True)
plt.show()

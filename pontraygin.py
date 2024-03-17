from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# Define the dynamics of the system
def dynamics(t, x, u):
    x1_dot = x[1]  # First state derivative
    x2_dot = u      # Second state derivative (control input)
    return [x1_dot, x2_dot]

# Define the cost function to be minimized
def cost_function(u):
    t_span = [0, 1]  # Time span for integration
    x0 = [0, 0]      # Initial state
    sol = solve_ivp(lambda t, x: dynamics(t, x, u), t_span, x0, method='RK45')
    x_final = sol.y[:, -1]  # Final state
    return np.dot(x_final, x_final) + 0.1 * u**2  # Objective function to minimize

# Initial guess for control input
u_guess = 0

# Optimize the control input using the minimize function
result = minimize(cost_function, u_guess, method='SLSQP')

# Extract the optimal control input
u_opt = result.x[0]

# Simulate the system with the optimal control input
t_span = np.linspace(0, 1, 100)
x0 = [0, 0]
sol = solve_ivp(lambda t, x: dynamics(t, x, u_opt), [0, 1], x0, method='RK45')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='State x1')
plt.plot(sol.t, sol.y[1], label='State x2')
plt.xlabel('Time')
plt.ylabel('State')
plt.title("Optimal Control using Pontryagin's Maximum Principle")
plt.legend()
plt.grid(True)
plt.show()

print(f"Optimal control input: {u_opt}")

import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_wealth = 10  # Initial wealth of the player
num_rounds = 100  # Number of rounds to play

# Generate random coin toss outcomes (1 for heads, -1 for tails)
np.random.seed(42)
coin_tosses = np.random.choice([-1, 1], size=num_rounds)

# Initialize arrays to store wealth at each round and running expectations
wealth_values = np.zeros(num_rounds + 1)
running_expectations = np.zeros(num_rounds + 1)
wealth_values[0] = initial_wealth
running_expectations[0] = initial_wealth

# Simulate the coin toss game and compute running expectations
for t in range(1, num_rounds + 1):
    wealth_values[t] = wealth_values[t - 1] + coin_tosses[t - 1]
    running_expectations[t] = running_expectations[0]  # Martingale property

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(num_rounds + 1), wealth_values, label='Player Wealth')
plt.plot(range(num_rounds + 1), running_expectations, label='Running Expectation', linestyle='--')
plt.xlabel('Rounds')
plt.ylabel('Wealth')
plt.title('Discrete-Time Martingale: Coin Toss Game')
plt.legend()
plt.grid(True)
plt.show()

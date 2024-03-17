import numpy as np

def black_scholes_discrete(S, K, r, sigma, T, N):
    dt = T / N  # Time step
    discount_factor = np.exp(-r * dt)  # Discount factor for each time step

    # Initialize arrays to store stock prices and option values at each time step
    S_values = np.zeros(N+1)
    option_values = np.zeros(N+1)

    # Calculate stock prices and option values at each time step using the discrete Black-Scholes formula
    for i in range(N+1):
        t = i * dt  # Current time
        S_t = S * np.exp((r - 0.5 * sigma**2) * t + sigma * np.sqrt(t) * np.random.normal(0, 1))
        S_values[i] = S_t
        option_values[i] = np.maximum(S_t - K, 0) * discount_factor**(N - i)

    return S_values, option_values

# Parameters
S0 = 100  # Initial stock price
K = 110   # Strike price
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility
T = 1.0  # Time to maturity
N = 100  # Number of time steps

# Run the discrete Black-Scholes model
stock_prices, option_values = black_scholes_discrete(S0, K, r, sigma, T, N)

# Print the results
print("Stock Prices at Each Time Step:", stock_prices)
print("Option Values at Each Time Step:", option_values)

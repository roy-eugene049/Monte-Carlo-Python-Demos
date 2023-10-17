import numpy as np

def monte_carlo_option_pricing(S, K, r, T, volatility, num_simulations):
    dt = T / 252  # Assuming 252 trading days in a year
    num_periods = int(T / dt)

    option_prices = []

    for _ in range(num_simulations):
        prices = [S]
        for _ in range(num_periods):
            z = np.random.normal(0, 1)
            price = prices[-1] * np.exp((r - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z)
            prices.append(price)

        option_payoff = max(0, prices[-1] - K)
        option_prices.append(option_payoff)

    option_price = np.exp(-r * T) * np.mean(option_prices)
    return option_price

S = 100  # Current stock price
K = 105  # Strike price
r = 0.05  # Risk-free interest rate
T = 1.0  # Time to expiration (in years)
volatility = 0.2  # Annual volatility
num_simulations = 10000

option_price = monte_carlo_option_pricing(S, K, r, T, volatility, num_simulations)
print(f"Estimated option price: {option_price}")

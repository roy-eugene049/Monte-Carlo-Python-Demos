import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4

num_samples = 1000000
estimated_pi = monte_carlo_pi(num_samples)
print(f"Estimated π with {num_samples} samples: {estimated_pi}")

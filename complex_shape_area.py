import random

def monte_carlo_integration(num_samples):
    inside_area = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if y <= f(x):
            inside_area += 1

    area_estimate = inside_area / num_samples
    return area_estimate

def f(x):
    # Define your own function here
    return x**2

num_samples = 100000
estimated_area = monte_carlo_integration(num_samples)
print(f"Estimated area with {num_samples} samples: {estimated_area}")

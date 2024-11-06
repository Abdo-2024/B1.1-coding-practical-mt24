import numpy as np
import matplotlib.pyplot as plt
import multiprocessing

# Function to estimate Pi for a single batch
def estimate_batch(batch_size):
    x = np.random.random(batch_size)
    y = np.random.random(batch_size)
    inside_circle = np.sum(x**2 + y**2 <= 1)
    return inside_circle

def estimate_pi_parallel(num_points, batch_size=10000):
    """Estimate π using Monte Carlo method with parallelized batches."""
    # Determine number of batches
    num_batches = num_points // batch_size
    estimates = []
    inside_circle_total = 0

    # Create pool of workers
    with multiprocessing.Pool() as pool:
        for i in range(1, num_batches + 1):
            results = pool.apply(estimate_batch, args=(batch_size,))
            inside_circle_total += results

            # Estimate Pi based on the total points processed so far
            pi_estimate = (inside_circle_total / (i * batch_size)) * 4
            estimates.append(pi_estimate)

    return estimates

# Number of samples for Monte Carlo simulation (e.g., 10^8 for a decent estimate)
num_samples = 10**7  # Reduce number of samples for faster processing
batch_size = 10000    # Process in batches of 10,000 points

# Estimate π using the parallelized Monte Carlo method
estimates = estimate_pi_parallel(num_samples, batch_size)

# Plot the convergence of π estimate
plt.figure(figsize=(10, 6))
plt.plot(estimates, label="Estimated π", color="blue")
plt.axhline(y=np.pi, color="red", linestyle="--", label="Actual π")
plt.xlabel("Number of Points (in batches of 10,000)")
plt.ylabel("Estimate of π")
plt.title("Convergence of Monte Carlo Estimate of π")
plt.legend()
plt.grid(True)
plt.show()

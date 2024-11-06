import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_points, batch_size=10000):
    """Estimate the value of π using Monte Carlo method with num_points random points in batches."""
    # Initialize variables
    inside_circle = 0
    estimates = []
    
    # Process the points in batches for efficiency
    for i in range(batch_size, num_points + 1, batch_size):
        # Generate random points in a batch
        x = np.random.random(batch_size)
        y = np.random.random(batch_size)
        
        # Count points inside the unit circle
        inside_circle += np.sum(x**2 + y**2 <= 1)
        
        # Update the estimate of π based on the current batch
        pi_estimate = (inside_circle / i) * 4
        estimates.append(pi_estimate)
    
    # Return estimates
    return estimates

# Example usage
num_samples = 10**10  # 10 billion samples
batch_size = 10000    # Process in batches of 10,000 points

estimates = estimate_pi(num_samples, batch_size)

# Plot the convergence
plt.plot(estimates, label="Estimated π")
plt.axhline(y=np.pi, color="r", linestyle="--", label="Actual π")
plt.xlabel("Number of Points (in batches of 10,000)")
plt.ylabel("Estimate of π")
plt.legend()
plt.title("Convergence of Monte Carlo Estimate of π")
plt.show()

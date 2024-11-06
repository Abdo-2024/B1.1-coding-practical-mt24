import matplotlib.pyplot as plt
import numpy as np  
from monte_carlo import estimate_pi

# def plot_convergence(max_points, step):
    #"""Plot the convergence of π estimates as the number of points increases."""
    #estimates = []
    #variances = []
    #points = range(step, max_points + 1, step)
    
    #for num_points in points:
     #   pi_estimate, variance = estimate_pi(num_points)
      #  estimates.append(pi_estimate)
       # variances.append(variance)
    
    #plt.figure(figsize=(10, 6))
    #plt.plot(points, estimates, label="Estimated π")
    #plt.axhline(y=np.pi, color="r", linestyle="--", label="Actual π")
    #plt.errorbar(points, estimates, yerr=np.sqrt(variances), label='Error Estimate', fmt='o', capsize=5)
    #plt.xlabel("Number of Points")
    #plt.ylabel("Estimate of π")
    #plt.legend()
    #plt.title("Convergence of Monte Carlo π Estimate with Error Bars")
    #plt.show()


def plot_convergence_and_error(max_points, step):
    """Plot the convergence of π estimates and a separate plot of error reduction."""
    estimates = []
    errors = []
    points = range(step, max_points + 1, step)
    
    for num_points in points:
        pi_estimate, variance = estimate_pi(num_points)
        estimates.append(pi_estimate)
        error = np.abs(pi_estimate - np.pi)  # Calculate the absolute error
        errors.append(error)
    
    # Plot convergence of π estimates
    plt.figure(figsize=(10, 6))
    plt.plot(points, estimates, label="Estimated π")
    plt.axhline(y=np.pi, color="r", linestyle="--", label="Actual π")
    plt.errorbar(points, estimates, yerr=np.sqrt(variance), fmt='o', capsize=5, label='Error Estimate')
    plt.xlabel("Number of Points")
    plt.ylabel("Estimate of π")
    plt.legend()
    plt.title("Convergence of Monte Carlo π Estimate with Error Bars")
    plt.show()
    
    # Plot error reduction
    plt.figure(figsize=(10, 6))
    plt.plot(points, errors, label="Error in π Estimate", color="purple")
    plt.xlabel("Number of Points")
    plt.ylabel("Absolute Error")
    plt.title("Error Reduction in Monte Carlo π Estimate")
    plt.legend()
    plt.show()


#def plot_error_reduction(max_points, step):
    """Plot the reduction of error as the number of points increases."""
    errors = []
    points = range(step, max_points + 1, step)
    
    for num_points in points:
        pi_estimate, variance = estimate_pi(num_points)
        error = abs(pi_estimate - np.pi)  # Calculate the absolute error
        errors.append(error)
    
    plt.figure(figsize=(10, 6))
    plt.plot(points, errors, label="Absolute Error")
    plt.xlabel("Number of Points")
    plt.ylabel("Error")
    plt.yscale('log')  # Optional: Use logarithmic scale if errors decrease exponentially
    plt.legend()
    plt.title("Error Reduction in Monte Carlo π Estimate")
    plt.show()

def plot_error_reduction(max_points, step, average_runs=5):
    """Plot the reduction of error as the number of points increases, with optional averaging."""
    errors = []
    points = range(step, max_points + 1, step)
    
    for num_points in points:
        run_errors = []
        for _ in range(average_runs):
            pi_estimate, _ = estimate_pi(num_points)
            run_errors.append(abs(pi_estimate - np.pi))
        avg_error = np.mean(run_errors)
        errors.append(avg_error)
    
    plt.figure(figsize=(10, 6))
    plt.plot(points, errors, label="Average Absolute Error")
    plt.xlabel("Number of Points")
    plt.ylabel("Error")
    plt.yscale('log')  # Logarithmic scale to highlight exponential-like decay
    plt.legend()
    plt.title("Error Reduction in Monte Carlo π Estimate")
    plt.show()
 
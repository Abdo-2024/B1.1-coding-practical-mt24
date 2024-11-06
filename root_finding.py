import math
import matplotlib.pyplot as plt
import numpy as np
from monte_carlo import estimate_pi as estimate_pi_monte_carlo
from utils import calculate_error
from utils import estimate_pi_nilakantha
from utils import estimate_pi_gauss_legendre

def f(x):
    """Define the function for which we want to find roots."""
    return math.sin(x)  # Example function with root at π

def bisection_method(a, b, tol=1e-5):
    """Bisection method to find a root of f in [a, b]."""
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint  # Found exact root
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2.0

#def estimate_pi_root_finding(tol=1e-6, max_iter=100):
    """Estimate π using the root-finding method (e.g., bisection)."""
    low, high = 3, 4
    pi_estimates = []

    for _ in range(max_iter):
        midpoint = (low + high) / 2
        pi_estimates.append(midpoint)  # Save each midpoint as an intermediate estimate of π

        if abs(midpoint - 3.141592653589793) < tol:
            break
        elif midpoint**2 > 3.141592653589793**2:
            high = midpoint
        else:
            low = midpoint

    return pi_estimates  # Return the list of estimates

def bisection_method(a, b, tol=1e-5):
    """Bisection method to find a root of f in [a, b]."""
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint  # Found exact root
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2.0

def estimate_pi_root_finding(tol=1e-6, max_iter=100):
    """Estimate π using the root-finding method (e.g., bisection)."""
    low, high = 3, 4
    pi_estimates = []

    for _ in range(max_iter):
        midpoint = (low + high) / 2
        pi_estimates.append(midpoint)  # Save each midpoint as an intermediate estimate of π

        if abs(midpoint - np.pi) < tol:
            break
        elif midpoint**2 > np.pi**2:
            high = midpoint
        else:
            low = midpoint

    return pi_estimates  # Return the list of estimates

def plot_error_comparison(max_iterations, step):
    """Plot the error reduction for various methods of estimating π."""
    points = range(step, max_iterations + 1, step)
    errors_monte_carlo = []
    errors_root_finding = []
    errors_nilakantha = []
    errors_gauss_legendre = []

    for num_points in points:
        # Monte Carlo Method
        pi_estimate_mc, _ = estimate_pi_monte_carlo(num_points)
        error_mc = abs(pi_estimate_mc - np.pi)
        errors_monte_carlo.append(error_mc)

        # Root-Finding Method
        pi_estimate_rf = estimate_pi_root_finding(tol=1e-6, max_iter=num_points)
        error_rf = abs(pi_estimate_rf[-1] - np.pi)  # Use the last estimate
        errors_root_finding.append(error_rf)

        # Nilakantha Series
        pi_estimate_nil = estimate_pi_nilakantha(num_points)
        error_nil = abs(pi_estimate_nil[-1] - np.pi)  # Use the last estimate
        errors_nilakantha.append(error_nil)

        # Gauss-Legendre Algorithm
        pi_estimate_gl = estimate_pi_gauss_legendre(num_points)
        error_gl = abs(pi_estimate_gl[-1] - np.pi)  # Use the last estimate
        errors_gauss_legendre.append(error_gl)

    # Plot the error reduction for each method
    plt.figure(figsize=(10, 6))
    plt.plot(points, errors_monte_carlo, label="Monte Carlo", marker='o')
    plt.plot(points, errors_root_finding, label="Root-Finding", marker='s')
    plt.plot(points, errors_nilakantha, label="Nilakantha Series", marker='^')
    plt.plot(points, errors_gauss_legendre, label="Gauss-Legendre", marker='x')

    plt.yscale('log')  # Use logarithmic scale for y-axis to highlight exponential-like decay
    plt.xlabel("Number of Iterations / Points")
    plt.ylabel("Absolute Error")
    plt.title("Error Reduction in π Estimation Methods")
    plt.legend()
    plt.show()

def estimate_pi(tol=1e-6, max_iter=100):
    low, high = 3, 4
    pi_estimates = []
    
    for _ in range(max_iter):
        midpoint = (low + high) / 2
        pi_estimates.append(midpoint)  # Save each midpoint as an intermediate estimate of π

        if abs(midpoint - np.pi) < tol:
            break
        elif midpoint**2 > np.pi**2:
            high = midpoint
        else:
            low = midpoint

    return pi_estimates  # Return the list of estimates


import matplotlib.pyplot as plt
from monte_carlo import estimate_pi
from plot_convergence import plot_convergence
from root_finding import estimate_pi_root_finding
from utils import time_function, calculate_error
import math

#def main():
#    print("Estimating π using Monte Carlo")
#    pi_estimate, variance = time_function(estimate_pi, 10000)
#    error = calculate_error(pi_estimate, math.pi)
#    print(f"Monte Carlo estimate of π: {pi_estimate}, Error: {error}, Variance: {variance}")

#    print("Plotting convergence")
#    plot_convergence(100000, 1000)

#    print("Estimating π using root-finding method")
#    pi_root = time_function(estimate_pi_root_finding)
#    error_root = calculate_error(pi_root, math.pi)
#    print(f"Root-finding method estimate of π: {pi_root}, Error: {error_root}")

#if __name__ == "__main__":
#    main()

def main():
    print("Select a method to estimate π:")
    print("1 - Monte Carlo")
    print("2 - Root-Finding")
    print("3 - Nilakantha Series (optional)")
    print("4 - Gauss-Legendre Algorithm (optional)")
    choice = input("Enter the number of the method you want to run (1-4): ")

    results = {}

    if choice == "1":
        pi_estimates, variance = estimate_pi(10000)  # Assume this returns a list of estimates and final variance
        pi_estimate = pi_estimates[-1]
        error = calculate_error(pi_estimate, math.pi)
        results['Monte Carlo'] = {'Estimate': pi_estimate, 'Error': error, 'Variance': variance}
        print(f"Monte Carlo estimate of π: {pi_estimate}, Error: {error}, Variance: {variance}")
        plot_convergence(pi_estimates, "Monte Carlo")

    elif choice == "2":
        pi_estimates = estimate_pi_root_finding()  # Assume this returns a list of estimates
        pi_estimate = pi_estimates[-1]
        error = calculate_error(pi_estimate, math.pi)
        results['Root-Finding'] = {'Estimate': pi_estimate, 'Error': error}
        print(f"Root-Finding method estimate of π: {pi_estimate}, Error: {error}")
        plot_convergence(pi_estimates, "Root-Finding")

    elif choice == "3":
        from utils import estimate_pi_nilakantha
        pi_estimates = estimate_pi_nilakantha(1000)  # Assume it returns a list of estimates
        pi_estimate = pi_estimates[-1]
        error = calculate_error(pi_estimate, math.pi)
        results['Nilakantha'] = {'Estimate': pi_estimate, 'Error': error}
        print(f"Nilakantha Series estimate of π: {pi_estimate}, Error: {error}")
        plot_convergence(pi_estimates, "Nilakantha Series")

    elif choice == "4":
        from utils import estimate_pi_gauss_legendre
        pi_estimates = estimate_pi_gauss_legendre(10)  # Assume it returns a list of estimates
        pi_estimate = pi_estimates[-1]
        error = calculate_error(pi_estimate, math.pi)
        results['Gauss-Legendre'] = {'Estimate': pi_estimate, 'Error': error}
        print(f"Gauss-Legendre Algorithm estimate of π: {pi_estimate}, Error: {error}")
        plot_convergence(pi_estimates, "Gauss-Legendre")

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        return

    print("\nSummary of Results:")
    for method, result in results.items():
        print(f"{method}: Estimate = {result['Estimate']}, Error = {result['Error']}, Variance = {result.get('Variance', 'N/A')}")

if __name__ == "__main__":
    main()


π Estimation Project
Description

This project provides various methods to estimate the mathematical constant π (Pi) through computational approaches. It includes methods such as the Monte Carlo method, root-finding algorithms, Nilakantha series, and the Gauss-Legendre algorithm. The project also includes functionality to visualize the convergence of the estimation methods and compare the error reductions as the number of iterations increases.

Project Structure
/home/a/Desktop/Comp B1.1/
├── main.py               # Main script for running π estimation methods
├── monte_carlo.py        # Monte Carlo method for estimating π
├── pi_estimation.ipynb   # Jupyter Notebook with Monte Carlo implementation and error visualization
├── plot_convergence.py   # Functions for plotting convergence and error reduction
├── root_finding.py       # Root-finding method for estimating π
└── utils.py              # Utility functions for error calculation, timing, and additional methods


Requirements

    Python 3.x
    numpy
    matplotlib

To install the required packages, you can run the following: pip install numpy matplotlib


How to Use
Running the Project

    Main Script:
        The main.py file contains the interactive menu to select the estimation method.
        You can run this file directly by executing python main.py from the command line.
        You will be prompted to choose between the following methods to estimate π:
            Monte Carlo - Estimates π using the Monte Carlo method.
            Root-Finding - Estimates π using a root-finding method.
            Nilakantha Series (optional) - Uses the Nilakantha series for π estimation.
            Gauss-Legendre Algorithm (optional) - Estimates π using the Gauss-Legendre algorithm.

    Jupyter Notebook:
        The pi_estimation.ipynb Jupyter Notebook provides an interactive way to explore the Monte Carlo method in more depth.
        It includes visualizations of the convergence and error reduction of the Monte Carlo method.
        Open it in a Jupyter environment (e.g., jupyter notebook pi_estimation.ipynb) to run and visualize results interactively.

Functions

    Monte Carlo Method (monte_carlo.py):
        estimate_pi(num_points, batch_size=10000):
            Estimates π by randomly generating points inside a unit square and calculating the ratio of points inside a unit circle.
            The function returns a list of estimates as the number of points increases.

    Root-Finding Method (root_finding.py):
        estimate_pi_root_finding():
            Estimates π using a root-finding approach (e.g., Newton's method).
            Returns a list of estimates as iterations proceed.

    Utility Functions (utils.py):
        time_function(func, *args):
            Times the execution of a given function.
        calculate_error(estimate, actual_value):
            Computes the absolute error between the estimated value of π and the true value (math.pi).
        estimate_pi_nilakantha(n) (optional) - Implements the Nilakantha series to estimate π.
        estimate_pi_gauss_legendre(n) (optional) - Implements the Gauss-Legendre algorithm to estimate π.

    Plotting Functions (plot_convergence.py):
        plot_convergence_and_error(max_points, step):
            Plots the convergence of the π estimates as the number of points increases, alongside the reduction in error.
        plot_error_comparison(max_iterations, step):
            Plots the error reduction for various estimation methods to compare their performance.

            examples:

Example 1: Running the Monte Carlo Method
from monte_carlo import estimate_pi
import matplotlib.pyplot as plt

# Estimate π using Monte Carlo method
estimates = estimate_pi(10000)  # 10,000 points
plt.plot(estimates, label="Monte Carlo estimate")
plt.axhline(y=np.pi, color='r', linestyle='--', label="Actual π")
plt.legend()
plt.show()

Example 2: Plotting Convergence
from plot_convergence import plot_convergence_and_error

# Plot convergence for the Monte Carlo method with 100,000 points in steps of 1,000
plot_convergence_and_error(100000, 1000)

Notes

    The project includes optional methods such as Nilakantha series and Gauss-Legendre, which can be accessed within the main.py script or the Jupyter Notebook.
    The code is designed for flexibility in terms of the number of points or iterations used for the estimation. Adjust the parameters as needed to control the precision and performance of the estimation.

Future Improvements

    Add more estimation methods (e.g., Leibniz series).
    Implement parallel processing for Monte Carlo estimation to improve performance for large numbers of samples.

    License

This project is licensed under the MIT License - see the LICENSE file for details.# B1.1-coding-practical-mt24

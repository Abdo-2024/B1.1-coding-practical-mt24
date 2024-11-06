# utils.py

import time
import math

def time_function(func, *args):
    """A utility to time how long a function takes to execute."""
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"Execution time for {func.__name__}: {end - start:.4f} seconds")
    return result

def calculate_error(estimated_value, true_value):
    """Calculates the absolute error."""
    return abs(estimated_value - true_value)

# This was the first implementation of the Nilakantha series and its output is also in the .ipynb file 
# so if you want to run that to see how this worked makes sure to uncomment it and comment the new 
# implementation of the Nilakantha series
# def estimate_pi_nilakantha(iterations):
    pi_estimate = 3.0
    sign = 1  # To alternate between addition and subtraction
    for i in range(2, 2 + 2 * iterations, 2):
        term = 4 / (i * (i + 1) * (i + 2))
        pi_estimate += sign * term
        sign *= -1  # Alternate sign for each term
    return pi_estimate

def estimate_pi_nilakantha(iterations):
    pi_estimate = 3.0
    sign = 1  # To alternate between addition and subtraction
    estimates = [pi_estimate]  # List to store estimates at each step

    for i in range(2, 2 + 2 * iterations, 2):
        term = 4 / (i * (i + 1) * (i + 2))
        pi_estimate += sign * term
        sign *= -1  # Alternate sign for each term
        estimates.append(pi_estimate)  # Store the current estimate

    return estimates

def estimate_pi_gauss_legendre(iterations):
    a = 1.0
    b = 1 / math.sqrt(2)
    t = 0.25
    p = 1.0
    estimates = []

    for _ in range(iterations):
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2
        pi_estimate = ((a + b) ** 2) / (4 * t)
        estimates.append(pi_estimate)

    return estimates

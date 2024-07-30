import sys
from statistics import mean, pstdev

def read_population_data(filename):
    """This function reads population data from a text file."""
    try:
        with open(filename) as file:
            population_data = [float(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        sys.exit(1)
    except ValueError as err:
        print(f"Error: {err}. File should contain only numbers.")
        sys.exit(1)
    except Exception as err:
        print(f"Exception error occurred: {err}.")
        sys.exit(1)

    return population_data

def calculate_covariance(x, y):
    """Calculate the covariance between two variables."""
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    cov_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    return cov_xy / n

def calculate_linear_regression(x, y):
    """Calculate the linear regression line (y = mx + b)."""
    cov_xy = calculate_covariance(x, y)
    std_dev_x = pstdev(x)
    m = cov_xy / std_dev_x ** 2
    b = mean(y) - m * mean(x)
    return m, b

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 linear_stat.py <filename.txt>")
        sys.exit(1)

    population_data = read_population_data(sys.argv[1])
    x_values = population_data  # Replace with your actual x values
    y_values = population_data  # Replace with your actual y values

    slope, intercept = calculate_linear_regression(x_values, y_values)
    print(f"Linear Regression Line: y = {slope:.6f}x + {intercept:.6f}")

    # Example: Calculate Pearson Correlation Coefficient
    correlation_coefficient = calculate_covariance(x_values, y_values) / (std_dev_x * pstdev(y_values))
    print(f"Pearson Correlation Coefficient: {correlation_coefficient:.10f}")

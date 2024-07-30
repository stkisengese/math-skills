# Statistical Calculations: Linear Regression and Pearson Correlation

This project demonstrates how to calculate the Linear Regression Line and the Pearson Correlation Coefficient using data from a file. Both of these statistical measures are essential for understanding relationships between variables.

## Features

### 1. Linear Regression Line

The Linear Regression Line is a straight line that best fits a set of data points. It helps us predict the value of one variable (dependent variable) based on the value of another variable (independent variable). Here are the key features:

- **Equation**: The linear regression line has the form:
  $$y = mx + b$$
  - Where:
    - $$y$$ represents the dependent variable (e.g., actual numbers).
    - $$x$$ represents the independent variable (e.g., line numbers).
    - $$m$$ is the slope (coefficient of $$x$$).
    - $$b$$ is the y-intercept.
- **Calculation Steps**:
  1. Calculate the mean (average) of $$x$$ and $$y$$ values.
  2. Compute the covariance between $$x$$ and $$y$$.
  3. Calculate the variance of $$x$$.
  4. Compute the slope: $$m = \frac{{\text{{covariance}}(x, y)}}{{\text{{variance}}(x)}}$$
  5. Calculate the y-intercept: $$b = \text{{mean}}(y) - m \cdot \text{{mean}}(x)$$
- **Usage**: The linear regression line helps us make predictions or understand trends in data.

### 2. Pearson Correlation Coefficient

The Pearson Correlation Coefficient (often denoted as $$r$$) quantifies the linear relationship between two variables. It ranges from -1 (perfect negative correlation) to 1 (perfect positive correlation). Key features include:

- **Equation**:
  $$r = \frac{{\text{{covariance}}(x, y)}}{{\text{{std\_dev}}(x) \cdot \text{{std\_dev}}(y)}}$$
  - Where:
    - $$x$$ and $$y$$ are the variables being compared.
    - $$\text{{covariance}}(x, y)$$ is the covariance between $$x$$ and $$y$$.
    - $$\text{{std\_dev}}(x)$$ and $$\text{{std\_dev}}(y)$$ are the standard deviations of $$x$$ and $$y$$, respectively.
- **Interpretation**:
  - $$r > 0$$: Positive correlation (as $$x$$ increases, $$y$$ tends to increase).
  - $$r < 0$$: Negative correlation (as $$x$$ increases, $$y$$ tends to decrease).
  - $$r = 0$$: No linear correlation.
- **Usage**: Assessing the strength and direction of linear association between variables.

## Usage

1. Clone this repository.
2. Run the program at root directory with the data file as an argument:
   ```
   $ python3 linear_stat.py data.txt
   ```

## Example Output

```
Linear Regression Line: y = 0.123456x + 42.987654
Pearson Correlation Coefficient: 0.8765432101
```

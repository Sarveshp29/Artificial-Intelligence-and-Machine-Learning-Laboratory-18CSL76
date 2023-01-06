### Program 9
# Implement the non-parametric Locally Weighted Regression algorithm in order to fit data points.  Select appropriate data set for your experiment and draw graphs

- Regression analysis help us to understand how the value of the dependent variable is changing corresponding to the independent variable.
- It’s a supervised learning technique which helps in predicting the dependent variable based on the independent variable.
- Linear regression algorithm shows a linear relationship between a dependent variable and one or more independent variables.
- But this algorithm cannot be used for non linear relationships between dependent and independent variables. In such cases, locally weighted regression algorithm is used.
- Locally weighted regression is a non-parametric algorithm, that is, it doesn’t not learn a fixed set of parameters. Rather, the parameter theta are computed individually for each query point. While computing theta, a higher preference is given to the points in the training set lying in the vicinity of query point.

### Algorithm
**Step 1** <br />
```
Read the given data sample to X and the curve to Y 
```
**Step 2** <br />
```
Set the value for the smoothening parameter on Free parameter
```
**Step 3** <br />
```
Set the bias, set ${x}_{0}$ which is a subset of X
```
**Step 4** <br />
```
Determine the weight matrix using
```
```math
w(x,x_{0}) = {e}^{\frac{(-(x - x_{0})^2}{(2\uptau)^2)}}
```

**Step 5**
```
Determine the value of model term parameter \beta using
```
```math
\beta (x_{0}) = {{X}^{T}WX}^{-1} {X}^{T}WY
```
**Step 6** <br />
```
Predication
```
```math
x_{0} * \beta
```

### Program
```python

import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    x0 = [1, x0]
    X = [[1, i] for i in X]
    X = np.asarray(X)
    xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau))
    theta = np.linalg.pinv(xw @ X) @ xw @ Y @ x0
    return theta

def draw(tau):
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
    plt.plot(X, Y, 'o', color='black')
    plt.plot(domain, prediction, color='red')
    plt.show()

X = np.linspace(-3, 3, num=1000)
domain = X
Y = np.log(np.abs(X ** 2 - 1) + .5)

draw(10)
draw(1)
draw(0.0001)
```

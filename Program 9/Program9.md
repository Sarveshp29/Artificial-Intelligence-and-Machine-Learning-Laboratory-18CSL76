# Implement the non-parametric Locally Weighted Regression algorithm in order to fit data points.  Select appropriate data set for your experiment and draw graphs

Regression analysis help us to understand how the value of the dependent variable is changing corresponding to the independent variable.

It’s a supervised learning technique which helps in predicting the dependent variable based on the independent variable.

Linear regression algorithm shows a linear relationship between a dependent variable and one or more independent variables.

But this algorithm cannot be used for non linear relationships between dependent and independent variables. In such cases, locally weighted regression algorithm is used.

Locally weighted regression is a non-parametric algorithm, that is, it doesn’t not learn a fixed set of parameters. Rather, the parameter theta are computed individually for each query point. While computing theta, a higher preference is given to the points in the training set lying in the vicinity of query point.

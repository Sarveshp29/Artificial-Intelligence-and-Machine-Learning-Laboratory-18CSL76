### Program 5
# Build an Artificial Neural Network by implementing the Back propagation algorithm and test the same using appropriate data sets

### Algorithm
1) Input X , arrive through the pre connected path
2) the input are modeled using true weights W. Weights are usually chosen randomly.
3) Calculate the output for every neuron from the input layer, to the hidden layer, to the output layer.
4) Calculate the errors in the outputs
```
Error = Ached Output - Desired Output
```
5) Travel but from the output layer to the hidden layer to adjust the weight such that error is deceased.

### Program
```python
import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([.92], [.82], [.89]), dtype=float)
X = X / np.amax(X, axis=0)
y = y / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def der_sigmoid(x):
    return x * (1 - x)

epoch = 5000
lr = 0.01
neurons_i = 2
neurons_h = 3
neurons_o = 1
weight_h = np.random.uniform(size=(neurons_i, neurons_h))
bias_h = np.random.uniform(size=(1, neurons_h))
weight_o = np.random.uniform(size=(neurons_h, neurons_o))
bias_o = np.random.uniform(size=(1, neurons_o))

for i in range(epoch):
    inp_h = np.dot(X, weight_h) + bias_h
    out_h = sigmoid(inp_h)
    inp_o = np.dot(out_h, weight_o) + bias_o
    out_o = sigmoid(inp_o)
    err_o = y - out_o
    grad_o = der_sigmoid(out_o)
    delta_o = err_o * grad_o
    err_h = delta_o.dot(weight_o.T)
    grad_h = der_sigmoid(out_h)
    delta_h = err_h * grad_h
    weight_o += out_h.T.dot(delta_o) * lr
    weight_h += X.T.dot(delta_h) * lr

print('Input:\n', X)
print('Actual:\n', y)
print('Predicated:\n', out_o)
```

### Result
```
Input:
 [[0.66666667 1.        ]
 [0.33333333 0.55555556]
 [1.         0.66666667]]
Actual:
 [[0.0092]
 [0.0082]
 [0.0089]]
Predicated:
 [[0.04487103]
 [0.06064437]
 [0.04416926]]
 ```

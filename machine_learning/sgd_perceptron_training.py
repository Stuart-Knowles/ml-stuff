"""
This is a really simple hand-rolled backpropagation trained Perceptron to distinguish between
Two hand written digits.

It's ugly, but it works, and is a nice POC of how simple this technique can be at its core.
"""

# %% Load
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

eta = 0.0005  # learning rate
n_iter = 1000

digits = datasets.load_digits(n_class=2)  # binary classification
data = digits.images.reshape((digits.images.shape[0], -1))

# %% Train

# split the data into train and test
# and normalize the targets to +-1 for easier binary classification
X_train, X_test, y_train, y_test = train_test_split(
    data, (digits.target - 0.5) * 2, train_size=0.5, shuffle=True
)

# Randomise the array initially
# We choose to initialise the weights to small numbers rather than normalise the input
# just because it's easier
weights = [
    (np.random.rand(64, 100) - 0.5) / 256,
    np.random.rand(100) * 2 - 1,
]


# logistic cost funciton
def cost(target, y):
    return np.log(1 + np.exp(-target * y))


# Derivative of the cost function with respect to output.
def dC_dy(target, y):
    return -target * np.exp(-target * y) / (1 + np.exp(-target * y))


# Stochastic gradient descent
# This is dumb learning, it doesn't vary learning rate or test for convergence
# it just iterates a bunch then hopes
for _ in range(n_iter):
    for x, target in zip(X_train, y_train):
        # Forward pass
        layer_1 = np.tanh(np.matmul(x, weights[0]))
        y = np.dot(layer_1, weights[1])

        # backward pass to calculate weight shifts

        # dC/dw1 = dC/df * df/dw1
        delta_weights_1 = dC_dy(target, y) * layer_1

        # dC/dw0 = dC/dw1 * dw1/dw0
        delta_weights_0 = delta_weights_1 * weights[0] / np.cosh(weights[1]) ** 2

        weights[0] -= eta * delta_weights_0
        weights[1] -= eta * delta_weights_1


# %% Test
def apply(x):
    layer_1 = np.tanh(np.matmul(x, weights[0]))
    out = np.dot(layer_1, weights[1])
    return np.tanh(out)


n_tot = len(X_test)
n_success = 0
for x, target in zip(X_test, y_test):
    if apply(x) / target > 0:
        n_success += 1
print(n_success / n_tot)


results = [abs(target - apply(x)) for x, target in zip(X_test, y_test)]

plt.hist(results, bins=20)

"""
================================
Recognizing hand-written digits
================================

This example shows how scikit-learn can be used to recognize images of
hand-written digits, from 0-9.

original example:
https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html

original author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
License: BSD 3 clause

Adapted by Stuart Knowles
"""

# %%
import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# %% Digits dataset
# Load data set and display first four images with the true values

digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)

# %% Classification
# flatten the images to create training data and split into train and test
data = digits.images.reshape((digits.images.shape[0], -1))
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, train_size=0.5, shuffle=True
)

# Create and train a classifier
classifier = MLPClassifier(activation="relu", solver="lbfgs", max_iter=1000)
classifier.fit(X_train, y_train)
#%%
# Predict the value of the digit on the test subset
predicted = classifier.predict(X_test)

# Classification report
print(
    f"Classification report for classifier {classifier}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

# Plot and print confusion matrix 
disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

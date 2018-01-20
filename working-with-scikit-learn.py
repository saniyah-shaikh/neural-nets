# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:27:47 2018

@author: Saniyah
"""

# playing with scikit-learn

# Pulled initial code from www.github.com/chanlaw/nn-presentation after PennApps demo

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_circles

#We'll use a synthetic dataset for ease of visualization
print("Creating Dataset...")
X, y = make_circles(n_samples=1000, noise=0.2, factor=0.5)
X = StandardScaler().fit_transform(X)

#Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#Start by plotting data
cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
plt.title("Training Data")
plt.show()

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright)
plt.title("Testing Data")
plt.show()

#Now Train Classifier
print("")
print("Creating Neural Network Classifier...")
clf = MLPClassifier(hidden_layer_sizes=(20,10), alpha=1e-3, learning_rate_init=1e-3, 
                    max_iter=5000, shuffle=True, warm_start=True)
print("")
print("Fitting Neural Network classifier...")
clf.fit(X_train, y_train)

training_accuracy = clf.score(X_train, y_train)
test_accuracy = clf.score(X_test, y_test)
print("Training accuracy: {}, Test Accuracy: {}".format(training_accuracy, test_accuracy))
print("")

#Visualize Decision Boundary
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))

Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=cm, alpha=.8)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                   edgecolors='black', s=25)

plt.title("Decision Boundary Visualization")
plt.show()
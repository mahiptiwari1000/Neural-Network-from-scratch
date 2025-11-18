# Neural Network From Scratch

A simple neural network implemented completely from scratch using Python and NumPy.  
This project is meant to understand how forward propagation, backpropagation, and gradient descent work under the hood.

## Features
- Fully connected neural network
- Forward & backward propagation
- Activation functions (ReLU, Sigmoid, Tanh)
- Mean Squared Error loss
- Gradient descent training loop

## Usage
Example (once you implement the NN):

```python
from nn import NeuralNetwork
import numpy as np

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])  # XOR

model = NeuralNetwork([2, 4, 1], learning_rate=0.1)
model.fit(X, y, epochs=5000)

print(model.predict(X))

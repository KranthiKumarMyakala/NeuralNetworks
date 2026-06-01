import pandas as pd
import numpy as np

inputs = [1,2,3]
weights = [0.2,0.8,-0.5]
bias = 2

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)

ReLu = max(0, output) # ReLU activation function
print(ReLu)

Sigmoid = 1 / (1 + np.exp(-output)) # Sigmoid activation function
print(Sigmoid)


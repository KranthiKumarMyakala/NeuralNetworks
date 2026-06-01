import pandas as pd
import numpy as np

#Create 4 Neurons
inputs = [1,2,3, 2.5]
weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87],
           [0.1, -0.14, 0.5, -0.5]]
bias = [2,3,0.5, 0.1]

# for loop to dot product of inputs and weights and add bias
outputs = []
for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    outputs.append(neuron_output)

print(outputs)
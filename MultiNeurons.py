inputs = [1,2,3, 2.5]
weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
weights1 = weights[0] #List of weight associated with 1ST Neuron :w11,w12,w13,w14
weights2 = weights[1] #List of weight associated with 1ST Neuron :w21,w22,w23,w24
weights3 = weights[2] #List of weight associated with 1ST Neuron :w31,w32,w33,w34

bias = [2,3,0.5]

bias1 = 2
bias2 = 3
bias3 = 0.5


outputs = [
    #Neuron1
    inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] +bias1,
    inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] +bias2,
    inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] +bias3,

]


print(outputs)
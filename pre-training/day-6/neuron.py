import math

# Simple neuron implementation with no libraries

class Neuron:
    def __init__(self, n_inputs, activation='sigmoid'):
        # randomly initialize weights
        self.weights = [0.1 * (i % 2 - 0.5) for i in range(n_inputs)]
        self.bias = 0.1
        self.activation = activation
    
    def sigmoid(self, x):
        try:
            return 1 / (1 + math.exp(-x))
        except:
            return 0 if x < 0 else 1
    
    def relu(self, x):
        return max(0, x)
    
    def forward(self, inputs):
        # compute weighted sum
        total = self.bias
        for i, w in enumerate(self.weights):
            total += w * inputs[i]
        
        # apply activation
        if self.activation == 'sigmoid':
            return self.sigmoid(total)
        elif self.activation == 'relu':
            return self.relu(total)
        else:
            return total


class DenseLayer:
    def __init__(self, n_inputs, n_neurons, activation='sigmoid'):
        self.neurons = [Neuron(n_inputs, activation) for _ in range(n_neurons)]
        self.n_neurons = n_neurons
    
    def forward(self, inputs):
        return [neuron.forward(inputs) for neuron in self.neurons]


class Network:
    def __init__(self):
        self.layer1 = DenseLayer(3, 4, activation='sigmoid')
        self.layer2 = DenseLayer(4, 2, activation='sigmoid')
    
    def forward(self, inputs):
        x = self.layer1.forward(inputs)
        return self.layer2.forward(x)


# test it
net = Network()
sample_input = [0.5, -0.3, 0.8]

print("\nNEURAL NETWORK FROM SCRATCH")
print("=" * 50)
print(f"Input: {sample_input}")

output = net.forward(sample_input)
print(f"Output: {[f'{o:.4f}' for o in output]}")
print(f"\nLayer 1 has 4 neurons, Layer 2 has 2 neurons")
print(f"Final output shape: ({len(output)},)")

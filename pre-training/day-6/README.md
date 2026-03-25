# Day 6: Build a Neuron from Scratch

## What I Built

A neural network with no libraries - just Python and math. 2 dense layers:
- Layer 1: 3 inputs → 4 neurons
- Layer 2: 4 inputs → 2 neurons

Each neuron takes inputs, multiplies by weights, adds the bias, passes through an activation function (sigmoid or ReLU).

## Forward Propagation

Forward propagation is just passing data through the network step by step:

1. Input [0.5, -0.3, 0.8] enters Layer 1
2. Each of the 4 neurons in Layer 1 does: (weight*input1 + weight*input2 + weight*input3 + bias) → activation
3. Those 4 outputs feed into Layer 2's 2 neurons
4. Same calculation happens again
5. Out comes 2 numbers - the final answer

It's called "forward" because data flows forward through the network. No loops, no fancy math - just multiply, add, apply a function, repeat.

## What's Missing For Learning?

Right now this network can't learn anything. We can set weights manually and run inputs through, but that's it.

To make it actually learn, we need:

1. **Loss function**: Measures how wrong the network is. "Real answer was 0.8, we predicted 0.3, so we're off by 0.5"

2. **Backpropagation**: Works backwards through the network to figure out which weights caused the wrong answer.

3. **Weight updates**: Once we know which weights are bad, change them slightly to reduce the error.

4. **Repeat**: Do this thousands of times on different examples until the network gets good.

The hard part (backprop + weight updates) is what makes learning happen. That's what PyTorch does for you - but now you know what it's actually doing.

## Key Files

- `neuron.py`: The implementation - Neuron class, DenseLayer, and a tiny Network
- `WORKFLOW.md`: Detailed explanation of how the network flows data and what's needed for learning
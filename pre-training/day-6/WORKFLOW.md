# Neural Network Workflow - Day 6

## What We Built

A simple neural network from scratch with 2 dense layers:
- **Layer 1**: Takes 3 inputs, produces 4 outputs via 4 neurons
- **Layer 2**: Takes 4 inputs, produces 2 final outputs via 2 neurons

No PyTorch, no NumPy - just pure Python with math.

## Forward Propagation (How it works)

1. **Input goes in**: We send [0.5, -0.3, 0.8] to the network

2. **Neuron computes**: Each neuron does:
   - Multiply each input by its weight
   - Add them all up with the bias
   - Put the total through an activation function (sigmoid or ReLU)
   - Return the result

3. **Layer computes**: All neurons in a layer do this in parallel, producing multiple outputs

4. **Chain it together**: Layer 1 output becomes Layer 2 input

5. **Final output**: We get 2 numbers from Layer 2 (because it has 2 neurons)

So for our example:
- Input [0.5, -0.3, 0.8] → Layer 1 (4 neurons) → [out1, out2, out3, out4]
- [out1, out2, out3, out4] → Layer 2 (2 neurons) → [final1, final2]

## What Each Part Does

**Weights**: Each weight determines how important an input is. A big weight = that input really matters. A small weight = that input barely affects the neuron.

**Bias**: The bias acts like a "baseline" or "offset". Without it, a neuron receiving all zero inputs would always produce zero. The bias lets the neuron output something even with zero inputs.

**Activation Function (sigmoid)**: Squashes any number into a range 0-1. Useful for probabilities. Formula: 1/(1 + e^-x)

**Activation Function (ReLU)**: Simpler - if x is negative, output 0. If x is positive, output x. Used in modern networks because it's fast.

## What's Missing For Learning?

This network can't learn anything yet. We can manually set weights and pass data through, but that's it.

To actually learn, we need:

1. **A loss function**: Something that measures "how wrong are we?" Compare network output to actual answer.

2. **Backpropagation**: A way to figure out which weights are causing the wrong outputs. Walk backwards through the network and adjust weights.

3. **Optimization**: A strategy for changing weights. Usually: take small steps in the direction that reduces loss. (Gradient descent)

4. **Training loop**: Repeat many times:
   - Pass data through network (forward pass)
   - Compute how wrong we were (loss)
   - Backpropagate to find which weights to change
   - Update weights slightly
   - Do it again with new data

Without these 4 things, weights stay fixed and the network never improves.

## In Code Terms

Our network right now is just functions. Real learning needs:

```
for each training example:
    output = network.forward(input)           # Forward pass ✓
    loss = compute_error(output, real_answer) # Loss ✗ (we skip this)
    gradients = backward()                     # Backprop ✗ (we skip this)
    update_weights(gradients)                 # Update ✗ (we skip this)
```

The ✓ part works. The ✗ parts are what PyTorch/TensorFlow automate for you.

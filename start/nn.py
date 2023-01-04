# neural network = mathematical abstraction of the brain
# it is a mathematical expression, and it is a fairly simple
# expressiom when you get down to it

# emergent magical behaviour despite them being so simple
# mathematically
# it's basically a sequence of Matrix multiplies which are
# 1:21
# really dot products mathematically and some nonlinearities thrown in and so it's a very simple mathematical
# 1:26
# expression and it's got knobs in it many knobs many knobs and these knobs are Loosely related to basically the
# 1:33
# synapses in your brain they're trainable they're modifiable and so the idea is like we need to find the setting of The Knobs that makes the neural nut do
# 1:40
# whatever you want it to do like classify images and so on and so there's not too much mystery I would say in it like
# 1:46
# um you might think that basically don't want to endow it with too much meaning with respect to the brain and how it
# 1:52
# works it's really just a complicated mathematical expression with knobs and those knobs need a proper setting for it
# 1:57
# to do something uh desirable
# are actually fairly good at optimizing these neural Nets and when you give them a hard enough problem they are forced to
# 4:30
# learn very interesting Solutions in the optimization and those solution basically have these immersion
# 4:37
# properties that are very interesting there's wisdom and knowledge in the knobs


# inputs from reality, information.
inputs = [1, 2, 3, 2.5]

# comment of the system on information.
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

print(list(zip(weights, biases)))

layer_outputs = []  # output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0  # output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)

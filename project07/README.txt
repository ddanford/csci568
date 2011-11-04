This implementation of an ANN is visually described in the ANN.png file.

The Network class is the top most layer of abstraction.  At creation, it accepts a list of layer sizes.  This corresponds to the number of nodes in each layer.  It runs values through the entire network by calling the function calculateOutputs with the paramter a list of values equal in size to the number of nodes in the input layer.  This class is also responsible for keeping training data, and running the network through the training data.

The Layer class is the middle layer of abstraction.  It accepts its size, and the size in the layer forward of it at creation.  It accepts new node values as a list (from previous layer, input or otherwise), and calculates the outputs from its nodes and their weights.

Nodes take a value in (from its layer) and outputs a list of its impact on the next layer.  It multiplies its value by the values of its weights.

The driver file project7.py can be run without any command line parameters.  At creation, all weights are initialized to random values, so until training is implemented, the output will be different every time.
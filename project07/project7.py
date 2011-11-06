import Network

ann = Network.Network([3,2,3])
ann.addTrainingData([1.0, 0.25, -0.5, 1.0, -1.0, 0.0])
ann.train()

print ann.calculateOutputs([1.0,0.25,-0.5])
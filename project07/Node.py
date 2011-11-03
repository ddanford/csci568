import random

class Node:
	def __init__(self, nextLayerSize):
		self.value = 0.0
		self.weights = [random.random()*2-1 for i in range(0,nextLayerSize]
	
	#Sets the value of the node, used when calculating the value of nodes in the next layer
	def setValue(self, newV):
		self.value = newV
		
	#Returns this nodes contribution to the next layer, or it's value if there is no next layer
	def getResults(self):
		if len(self.weights) == 0:
			return self.value
		return [self.value*w for w in self.weights]
		
	#Fixes the weights based on error from the next layer, a is the learning rate
	def adjustWeights(self, error, a=0.1):
		if len(error) != len(self.weights):
			return -1
		self.weights = [self.weights[i] - a*error[i]*self.value for i in range(0, len(weights))]
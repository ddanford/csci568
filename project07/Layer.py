class Layer:
	def __init__(self, size, nextLayerSize):
		self.nodes = [node(nextLayerSize) for i in range(0,size)]
		self.outputSize = nextLayerSize
	
	def setNodeValues(self, values):
		if(len(values) != len(self.nodes)):
			print("Invalid number of values.")
			quit()
		for i in range(0, len(self.nodes)):
			self.nodes[i] = values[i]
	
	#Calculates the values for the next layer from its nodes
	def getResults(self):
		results = []
		for i in range(0,self.outputSize):
			sum = 0.0
			for j in range(0,len(self.nodes)):
				sum = sum + self.nodes[j].getResults()[i]
			results.append(sum)
		return results
		
	#Fixes the weights of each node based on the error of the next layer
	#Returns the error of all nodes as a list
	def train(self, error):
		if(len(error) != self.outputSize):
			print("Size of error list does not match expected size")
			quit()
		return [self.nodes[i].train(error) for i in range(0,len(self.nodes))]
import Layer, random

class Network:
	def __init__(self, layerSizes):
		self.layers = [ Layer.Layer(layerSizes[i], layerSizes[i+1]) for i in range(0,len(layerSizes)-1) ]
		self.inputSize = layerSizes[0]
		self.outputSize = layerSizes[len(layerSizes)-1]
		self.trainingData = []
	
	#Runs input values through the network and returns the output
	def calculateOutputs(self, values, precision=10):
		for i in range(0,len(self.layers)):
			self.layers[i].setNodeValues(values)
			values = self.layers[i].getResults(precision)
		return values
		
	#Adds training data to adjust weights
	def addTrainingData(self, data):
		if len(data) != self.inputSize + self.outputSize:
			print("Training data is of the wrong size.")
			quit()
		self.trainingData.append(data)
	
	#Trains based on training data added to the network
	#Precision is the number of decimals to round to when checking error.
	def train(self,precision=12):
		sumError = 1.0
		while sumError != 0.0:
			sumError = 0.0
			trainDup = list(self.trainingData)
			while len(trainDup) > 0:
				dataSet = trainDup.pop(random.randint(0,len(trainDup)-1))
				inputData = dataSet[0:self.inputSize]
				outputData = dataSet[self.inputSize:]
				results = self.calculateOutputs(inputData,precision)
				error = [outputData[i]-results[i] for i in range(0,self.outputSize)]
				sumError += round(sum(error),precision)
				for i in range(0,len(self.layers)):
					error = self.layers[len(self.layers)-i-1].train(error)
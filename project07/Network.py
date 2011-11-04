import Layer

class Network:
	def __init__(self, layerSizes):
		self.layers = [ Layer.Layer(layerSizes[i], layerSizes[i+1]) for i in range(0,len(layerSizes)-1) ]
		self.inputSize = layerSizes[0]
		self.outputSize = layerSizes[len(layerSizes-1)]
		self.trainingData = []
	
	def calculateOutputs(self, values):
		for( i in range(0,len(self.layers)):
			self.layers[i].setNodeValues(values)
			values = self.layers[i].getResults()
		return values
		
	def addTrainingData(self, data):
		if len(data) != self.inputSize + self.outputSize:
			print("Training data is of the wrong size.")
			quit()
		self.trainingData.append(data)
	
	def train(self):
		sumError = 1.0
		while sumError != 0.0:
			sumError = 0.0
			trainDup = list(self.trainingData)
			while len(trainDup) > 0:
				dataSet = trainDup.pop(random.randint(0,len(trainDup)-1))
				inputData = dataSet[0:self.inputSize]
				outputData = dataSet[self.inputSize:]
				results = calculateOutputs(inputData)
				print results
				error = [outputData[i]-results[i] for i in range(0,self.outputSize)]
				sumError += sum(error)
				for i in range(len(self.layers),0):
					error = self.layers[len(self.layers)-i-1].train(error)
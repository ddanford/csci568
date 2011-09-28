from similarityMetrics import *

def read_csv(filename):
	dataobjects = []
	filelines = open(filename).readlines()
	for line in filelines:
		attributes = line.split(',')
		dataobjects.append(attributes)
	
	return dataobjects
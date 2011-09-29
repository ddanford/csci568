from similarityMetrics import *
import random
import math

def read_csv(filename):
	dataobjects = []
	filelines = open(filename).readlines()
	for line in filelines:
		attributes = line.split(',')
		for i in range(0, len(attributes)-1):
			attributes[i] = float(attributes[i])
		if len(attributes) != 1:
			dataobjects.append(attributes)
	return dataobjects
	
def randomCentroid(numAttr, mins, maxs):
	random.seed()
	centroid = []
	for i in range(0,numAttr):
		centroid.append( random.random()*(maxs[i]-mins[i])+mins[i] )
	return centroid

def findMins(dataobjects, numAttr):
	minAttrs = dataobjects[0][0:numAttr]
	for i in range(1,len(dataobjects)):
		for j in range(0,numAttr):
			if dataobjects[i][j] < minAttrs[j]:
				minAttrs[j] = dataobjects[i][j]
	return minAttrs
	
def findMaxs(dataobjects, numAttr):
	maxAttrs = dataobjects[0][0:numAttr]
	for i in range(1,len(dataobjects)):
		for j in range(0,numAttr):
			if dataobjects[i][j] > maxAttrs[j]:
				maxAttrs[j] = dataobjects[i][j]
	return maxAttrs

def kmeans(k, dataobjects, similarityMetric):
	clusters = []
	centroids = []
	numAttr = len(dataobjects[0])-1
	minAttrs = findMins(dataobjects, numAttr)
	maxAttrs = findMaxs(dataobjects, numAttr)
	
	
	
	for i in range(0,k):
		clusters.append([])
		centroids.append(randomCentroid(numAttr, minAttrs, maxAttrs))
	
	clusters[0] = dataobjects
	changed = True
	maxIterations = 1000
	iterations=0
	while(changed and iterations<maxIterations):
		changed = False
		for obj in dataobjects:
			s = 0
			for i in range(0,k):
				sim = similarityMetric(obj[0:numAttr],centroids[i])
				if sim == 0:
					print 'huh?'
				if sim > s:
					s = sim
					if not (obj in clusters[i]):
						changed = True
						for j in range(0,k):
							if obj in clusters[j]:
								clusters[j].remove(obj)
						clusters[i].append(obj)
		for i in range(0,k):
			for j in range(0,numAttr):
				if(len(clusters[i])!=0):
					centroids[i][j]=0
			for obj in clusters[i]:
				for j in range(0,numAttr):
					centroids[i][j] += obj[j]
			for j in range(0,numAttr):
				if(len(clusters[i])!=0):
					centroids[i][j] = centroids[i][j]/len(clusters[i])
		iterations += 1
		print len(clusters[0])
		print len(clusters[1])
		print len(clusters[2])
	print iterations
	return clusters
	
def sse(cluster):
	if len(cluster) == 0:
		return 0
	numAttrs = cluster[0]
	
dataset = read_csv('iris.csv')
clusters = kmeans(3,dataset,euclidean)
print len(clusters[0])
print len(clusters[1])
print len(clusters[2])
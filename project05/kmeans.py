from similarityMetrics import *
import random
import math

def read_csv(filename):
	dataobjects = []
	filelines = open(filename).readlines()
	for line in filelines:
		splitline = line.split(',')
		attributes = [float(splitline[i]) for i in range(0,len(splitline)-1)]
		if len(attributes) != 0:
			dataobjects.append(attributes)
	return dataobjects
	
def randomCentroids(k, numAttr, mins, maxs):
	centroids = []
	for i in range(0,k):
		centroid = []
		random.seed()
		for j in range(0,numAttr):
			centroid.append(random.random()*(maxs[j]-mins[j])+mins[j])
		centroids.append(centroid)
	print centroids[0]
	print centroids[1]
	print centroids[2]
	return centroids

def findMins(dataobjects, numAttr):
	minAttrs = dataobjects[0]
	for i in range(1,len(dataobjects)):
		for j in range(0,numAttr):
			if dataobjects[i][j] < minAttrs[j]:
				minAttrs[j] = dataobjects[i][j]
	print minAttrs,'Raage'
	return minAttrs
	
def findMaxs(dataobjects, numAttr):
	maxAttrs = dataobjects[0]
	for i in range(1,len(dataobjects)):
		for j in range(0,numAttr):
			if dataobjects[i][j] > maxAttrs[j]:
				maxAttrs[j] = dataobjects[i][j]
	print maxAttrs,'Raage'
	return maxAttrs
	
def emptyClusters(k):
	clusters = []
	for i in range(0,k):
		clusters.append([])
	return clusters
	
def assignObjects(dataobjects, similarityMetric, centroids):
	k = len(centroids)
	clusters = emptyClusters(k)
	numAttrs = len(dataobjects[0])
	
	for obj in dataobjects:
		maxSim = 0
		clusterIndex = -1
		for i in range(0,k):
			sim = similarityMetric(obj, centroids[i])
			#print i,' ',maxSim,' ',sim
			if sim > maxSim:
				maxSim = sim
				clusterIndex = i
		clusters[clusterIndex].append(obj)
	return clusters
	
def zeroCentroid(attrs):
	c = []
	for i in range(0,attrs):
		c.append(0)
	return c
	
def moveCentroids(clusters, numAttrs):
	centroids = emptyClusters(len(clusters))
	for c in centroids:
		c = zeroCentroid(numAttrs)
	for i in range(0,len(clusters)):
		clusterSize = len(clusters[i])
		attrSum = zeroCentroid(numAttrs)
		for obj in clusters[i]:
			for j in range(0,numAttrs):
				attrSum[j] += obj[j]
		centroids[i] = attrSum
		if clusterSize > 0:
			centroids[i] = [a/clusterSize for a in attrSum]
	return centroids

def randomCentroidPoints(k, dataobjects, numAttrs):
	centroids = []
	for i in range(0,k):
		centroids.append(dataobjects[int(math.ceil(random.random()*len(dataobjects)))])
	return centroids
	
def kmeans(k, dataobjects, similarityMetric):
	numAttr = len(dataobjects[0])
	# minAttrs = findMins(dataobjects, numAttr)
	# print minAttrs
	# maxAttrs = findMaxs(dataobjects, numAttr)
	# print minAttrs,'Double raage'
	
	centroids = randomCentroidPoints(k, dataobjects, numAttr)
	print centroids
	clusters = assignObjects(dataobjects, similarityMetric, centroids)
	
	changing = True
	maxIt = 1000
	it=0
	while(changing and it<maxIt):
		changing = False
		centroids = moveCentroids(clusters, numAttr)
		newclusters = assignObjects(dataobjects, similarityMetric, centroids) 
		
		for i in range(0,k):
			for obj in clusters[i]:
				if not obj in newclusters[i]:
					changing = True
		
		clusters = newclusters
		it += 1
	
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
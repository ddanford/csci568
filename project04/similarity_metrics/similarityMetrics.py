import random
from math import sqrt

#Find the Euclidean (linear) distance between two data objects
#Returns a number in the range [0,1]
def euclidean(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	distance = 0
	for attr in range(0,len(subject)):
		distance += (subject[attr]-target[attr])**2
	
	distance = sqrt(distance)
	return 1/(1+distance)
	
#Find the Simple Matching Coefficient
#This value will always be in the range [0,1]
def smc(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	num00 = 0.0
	num01 = 0.0
	num10 = 0.0
	num11 = 0.0
	for attr in range(0,len(subject)):
		if int(subject[attr])==0 and int(target[attr])==0:
			num00+= 1
		elif int(subject[attr])==0 and int(target[attr])==1:
			num01+= 1
		elif int(subject[attr])==1 and int(target[attr])==0:
			num10+= 1
		elif int(subject[attr])==1 and int(target[attr])==1:
			num11+= 1
		
	similarity = (num00+num11)/len(subject)
	return similarity

#Find the Jaccard Similarity
#This value will always be in the range [0,1]
def jaccard(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	num00 = 0.0
	num01 = 0.0
	num10 = 0.0
	num11 = 0.0
	for attr in range(0,len(subject)):
		if int(subject[attr])==0 and int(target[attr])==0:
			num00+= 1
		elif int(subject[attr])==0 and int(target[attr])==1:
			num01+= 1
		elif int(subject[attr])==1 and int(target[attr])==0:
			num10+= 1
		elif int(subject[attr])==1 and int(target[attr])==1:
			num11+= 1
	
	similarity = num11/(num01+num10+num11)
	return similarity

#Standard Deviation function for use in Pearson Correlation
def stdev(list):
	mean = sum(list)/len(list)
	std = 0
	for i in range(0,len(list)):
		std += (list[i]-mean)**2
	
	std = sqrt(std/(len(list)-1.0))
	return std
	
#Find Pearson Correlation Coefficient
#Returns a value in the range [-1,1]
def pearson(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	sbar = sum(subject)/len(subject)
	tbar = sum(subject)/len(subject)
	sstd = stdev(subject)
	tstd = stdev(target)
	pcc = 0
	for attr in range(0,len(subject)):
		pcc += (subject[attr]-sbar)/sstd*(target[attr]-tbar)/tstd
	pcc = pcc/(len(subject)-1)
	return pcc

#Find the Cosine Similarity
#Returns a value in the range [0,1]
def cosine(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	dot = 0
	mags = 0
	magt = 0
	for attr in range(0,len(subject)):
		dot += subject[attr]*target[attr]
		mags += subject[attr]**2
		magt += target[attr]**2
	mags = sqrt(mags)
	magt = sqrt(magt)
	similarity = dot/(mags*magt)
	return (similarity+1)/2
	
def roundedRandom():
	return round(random.random())

def test():
	if round(euclidean([1.0,3.0,4.0,6.0],[8.0,7.0,5.0,10.0]),5) != 0.09945:
		print 'Problem with Euclidean!'
		print euclidean([1.0,3.0,4.0,6.0],[8.0,7.0,5.0,10.0])
	if smc([0,0,1],[0,0,1]) != 1:
		print 'Problem with SMC!'
		print smc([0,0,1],[0,0,1])
	if jaccard([0,1,1],[0,1,0]) != .5:
		print 'Problem with Jaccard!'
		print jaccard([0,1,1],[0,1,0])
	if round(pearson([1.0,3.0,4.0,6.0],[8.0,7.0,5.0,10.0]),5) != 0.30769:
		print '\nProblem with Pearson!'
		print pearson([1.0,3.0,4.0,6.0],[8.0,7.0,5.0,10.0])
	if round(cosine([1.0,3.0,4.0,6.0],[8.0,7.0,5.0,10.0]),5) != 0.94865:
		print '\nProblem with Cosine!'
		print cosine([1.0,3.0,4.0,6.0],[8.0,7.0,5.0,10.0])
	

if __name__ == "__main__":
	subject = [roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom()]
	target = [roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom(), roundedRandom()]

	test()

	print '\nSubject is '
	print subject
	print '\nTarget is '
	print target
	print '\nEuclidean distance is ' + str(euclidean(subject, target))
	print 'Simple Matching Coefficient is ' + str(smc(subject, target))
	print 'Jaccard coefficient is ' + str(jaccard(subject, target))
	print 'Pearson Corelation Coefficient is ' + str(pearson(subject, target))
	print 'Cosine similarity is ' + str(cosine(subject, target))



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
	return distance
	
def smc(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	num00 = 0
	num01 = 0
	num10 = 0
	num11 = 0
	for attr in range(0,len(subject)):
		if subject[attr]==0 and target[attr]==0:
			num00++
		elif subject[attr]==0 and target[attr]==1:
			num01++
		elif subject[attr]==1 and target[attr]==0:
			num10++
		elif subject[attr]==1 and target[attr]==1:
			num11++
	
	similarity = (num00+num11)/len(subject)
	return similarity

def jaccard(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	num00 = 0
	num01 = 0
	num10 = 0
	num11 = 0
	for attr in range(0,len(subject)):
		if subject[attr]==0 and target[attr]==0:
			num00++
		elif subject[attr]==0 and target[attr]==1:
			num01++
		elif subject[attr]==1 and target[attr]==0:
			num10++
		elif subject[attr]==1 and target[attr]==1:
			num11++
	
	similarity = num11/(num01+num10+num11)
	return similarity

def stdev(list):
	mean = sum(list)/len(list)
	std = 0
	for l in list:
		std += (l-mean)**2
	
	std = sqrt(std/len(list))
	return std
	
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
		pcc = (subject[attr]-sbar)/sstd*(target[attr]-tbar)/tstd
	pcc = (len(subject)-1)*pcc
	return pcc

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
	return similarity
	
	
	
	
	

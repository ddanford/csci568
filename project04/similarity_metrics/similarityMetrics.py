

def euclidean(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return
	distance = 0
	for attr in subject:
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
	for attr in subject:
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

def pearson(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return

def cosine(subject, target):
	if type(subject) != type([]) or type(target) != type([]):
		print 'Parameters must both be lists of attributes.\n'
		return
	if len(subject) != len(target):
		print 'Paramters must have the same number of attributes.\n'
		return

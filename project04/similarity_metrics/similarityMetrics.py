

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


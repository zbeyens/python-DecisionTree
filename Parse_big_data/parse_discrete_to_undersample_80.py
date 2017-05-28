from random import sample, shuffle
training_positives = 80/100


def parse_credits(filename="creditcard_discretised.csv"):
	f = open(filename)
	attributes = f.readline().strip().split(",")
	
	#database = [[] for x in classes]
	database = []
	
	maxlines = float("inf") # 10000 #
	for line in f:
		line = line.strip().split(",")
		line = [int(x) for x in line]
		#for i, elem in enumerate(line):
		#	database[i].append(elem)
		database.append(line)
		
		if(len(database[0])>=maxlines):
			break
	f.close()
	return attributes,database
	
def export_credits(attributes,database,filename="creditcard_undersampled.csv"):
	
	f = open(filename,"w")
	f.write(",".join((x for x in attributes)))
	f.write("\n")
	for line in database:
		f.write(" ,".join(str(int(x)) for x in line))
		f.write("\n")
		
	

def resample_and_separate(attributes,database,target):
	"""Undersampling 
	https://www.kaggle.com/arathee2/achieving-100-accuracy
	https://www.kaggle.com/joparga3/in-depth-skewed-data-classif-93-recall-acc-now
	"""
	target_index = attributes.index(target)
	positive = []
	negative = []
	for line in database:
		if(line)[target_index]==1:
			positive.append(line)
		else:
			negative.append(line)
	print("Pos:",len(positive))
	print("Neg:",len(negative))
	keep = int(len(positive)*training_positives) #keep 80% for training, and 20% for testing
	
	shuffle(positive)
	shuffle(negative)
	
	positive_training = positive[:keep]
	positive_testing = positive[keep:]
	
	negative_training = negative[:keep]
	negative_testing1 = negative[keep:len(positive)] #Undersampled negatives also
	negative_testing2 = negative[keep:] #All the remaining negatives
	
	negative_undersampled = sample(negative,len(positive))
	lines = []
	problems = 0
	"""for line in negative:
		for lane in positive:
			if(line[:target_index]+line[target_index:] == lane[:target_index]+lane[target_index:]):
				if(line not in lines):
					print("Ligne à problème:\n",database.index(line),line,"\n",database.index(lane),lane)
					lines.append(line)
				problems+=1
	print("Problèmes:",len(lines))
	print("Lignes à problèmes:",problems)
	database = negative_undersampled+positive
	shuffle(database)
	print("Und:",len(database))"""
	training_set = positive_training+negative_training
	shuffle(training_set)
	valisation_set_1 = positive_testing+negative_testing1
	shuffle(valisation_set_1)
	valisation_set_2 = positive_testing+negative_testing2
	shuffle(valisation_set_2)
	
	return training_set, valisation_set_1, valisation_set_2

att,dat = parse_credits()
train,valid1,valid2=resample_and_separate(att,dat, "Class")
export_credits(att,train,"training_set.csv")
export_credits(att,valid1,"validation_set_undersampled.csv")
export_credits(att,valid2,"validation_set_extended.csv")
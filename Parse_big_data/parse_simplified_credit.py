from random import sample, shuffle

def parse_credits(filename="creditcard_simplified.csv"):
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
		
	

def resample(database):
	"""Undersampling 
	https://www.kaggle.com/arathee2/achieving-100-accuracy
	https://www.kaggle.com/joparga3/in-depth-skewed-data-classif-93-recall-acc-now
	"""
	positive = []
	negative = []
	for line in database:
		if(line)[-1]==1:
			positive.append(line)
		else:
			negative.append(line)
	print("Pos:",len(positive))
	print("Neg:",len(negative))
	negative_undersampled = sample(negative,len(positive))
	lines = []
	problems = 0
	for line in negative:
		for lane in positive:
			if(line[:-1] == lane[:-1]):
				if(line not in lines):
					print("Ligne à problème:\n",database.index(line),line,"\n",database.index(lane),lane)
					lines.append(line)
				problems+=1
	print("Problèmes:",len(lines))
	print("Lignes à problèmes:",problems)
	database = negative_undersampled+positive
	shuffle(database)
	print("Und:",len(database))
	return database

att,dat = parse_credits()
dat=resample(dat)
export_credits(att,dat)

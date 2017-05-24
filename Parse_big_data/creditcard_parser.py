import statistics
from math import ceil

def histogram(dataset,height=8,width=80,full="X",empty="_"):
	"""Given a list of data, draws an histogram 
	of given width and height with given characters
	Returns if histogram was succesful"""
	mv = min(dataset)
	Mv = max(dataset)
	print("[",mv,":",Mv,"]")
	if(mv==Mv):
		print(elem,"has no interval")
		return False
	if(width!=None):
		counter = [0]*width
		for n in dataset:
			counter[int((n-mv)*float(width-1)/(Mv-mv))]+=1
		#print("Biggest class size:",max(counter))
	else:
		data = sorted(set(dataset))
		counter = len(data)*[0]
		for n in dataset:
			counter[data.index(n)]+=1
			
	mc = max(counter)
	for i in range(height):
		print("".join((height-val*height/mc < i+1) and full or empty for val in counter))
	print()  
	return True

def parse_database(noisy=True):
	"""Opens creditcard.csv and read the data.
	The continuous data is discretised into 
	-1,0,1 based on the bottom 5% and top 5% of the values
	Returns a list containing the name of the attributes
	and a list containing data arranged by attribute then by line
	Prints stuff if noisy=True
	"""
	f = open("creditcard.csv")
	classes = f.readline().strip().replace('"',"").split(",")
	#[classes.index[""]] #nom de la classe
	database = [[] for x in classes]
	if(noisy): print(classes)
	maxlines =  float("inf") # 10000 #
	for line in f:
		line = line.strip()
		line = line.replace('"',"")
		line = line.split(",")
		line = [float(x) for x in line]
		for i, elem in enumerate(line):
			database[i].append(elem) 
		if(len(database[0])>=maxlines):
			break
	f.close()
	if(noisy):
		print("There are",len(database[0]),"data")
	is_integer = []
	for i, elem in enumerate(classes):
		#lower = 25/100
		#upper = 75/100
		mev = statistics.mean(database[i])
		dev = statistics.stdev(database[i])
		print("---",elem,"---\nMin:",min(database[i]),"- Max:",max(database[i]))
		print("Mean:",mev,"\nStandard Deviation:",dev)
		#dataset = sorted(database[i])
		if(noisy): 
			print("Histogram:")
			if(not histogram(database[i])): #dataset
				continue
				
		if(elem=="Time"):
			continue
		if( elem=="Class"):
			continue
		if(elem=="Amount"):
			classification = [5,15,50,100,500,1000,5000,10000,50000,100000,1000000,9999999999999999]
			for index,elem in enumerate(database[i]):
				a = database[i][index]
				if(a==int(a)):
					is_integer.append(1) #integer amount
				else:
					is_integer.append(0) #floating amount
				for uplim in classification:
					if a<uplim:
						a = uplim
						break
				database[i][index] = a
				
				
			"""if(noisy): 
				down = sorted(database[i])
				mid = statistics.median(down)
				histogram(down[:down.index(mid)])
				"""
		else:
			for j in range(len(database[i])):
				database[i][j]=int(ceil((database[i][j]-mev)/dev))
				if(database[i][j])>3:
					database[i][j]=4
				if(database[i][j])<-3:
					database[i][j]=-4
			
		"""lbi = int(len(dataset)*lower) #lower bound index
		ubi = int(len(dataset)*upper) #upper bound index
		
		if( elem=="Class"): #or elem=="Time"): # or elem=="Amount"
			continue
		if(noisy): 
			print("Histogram by cutting the lowest and highest 25%:")
			histogram(dataset[lbi:ubi])
		lb = dataset[lbi] #lower bound
		ub = dataset[ubi] #upper bound
		
		
		for j in range(len(database[i])):
			val = database[i][j]
			if(val<lb):
				database[i][j]=-1
			elif(val<ub):
				database[i][j]=0
			else:
				database[i][j]=1"""
				
		if(noisy): 
			print("Histogram after discretisation:")
			if(not histogram(database[i],width=None)):
				continue
			ldat = set(database[i])
			print(len(ldat),"different values")
	
	
	database = database[1:-1]+[is_integer]+[database[-1]]
	classes = classes[1:-1]+["Integer_amount"]+[classes[-1]]
	return classes,database

def main():
	classes, database = parse_database(noisy=True)
	#Note: it could be interesting to shift database from i;j to j;i 
	#Since we want to select specific lines 
	f = open("creditcard_discretised.csv","w")
	f.write(",".join((x for x in classes)))
	f.write("\n")
	for i in range(len(database[0])):
		line = ""
		for j in range(len(classes)):
			line+=str(int(database[j][i]))
			line+=" ,"
		line = line[:-1] + "\n"
		f.write(line)
			
		
if __name__ == "__main__":
	main()

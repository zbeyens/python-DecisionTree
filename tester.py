from _Utilities_.parse_credits import parse_credits
from os import sep

def majority_answer(tree):
	#Explore l'arbre et renvoie la valeur majoritaire
	#Pondérée par la profondeur et le nombre d'enfants
	to_explore = [(tree,1)]
	true = 0
	false = 0
	while(to_explore):
		tree,level = to_explore.pop()
		level/=len(tree)
		for key in tree:
			subtree = tree[key]
			if(isinstance(subtree,dict)):
				to_explore.append((subtree,level))
			else:
				if(subtree == 0):
					false+= level
				elif(subtree == 1):
					true += level
				else:
					print("Big error: no answer")
					print(subtree)
	if not(abs(true + false -1)<= 0.0000001):
		#Juste pour vérifier que leur somme fasse bien 1
		print("T:",true,"F:",false,"T+F:",true+false)
	if(true>false):
		return 1
	else:
		return 0
def test_tree(tree,classes,target,dataset):
	total_correct = 0
	frauds_total = 0
	legit_total = 0
	frauds_correct = 0
	legit_correct = 0
	error_lines = []
	
	detected_fraud = 0
	correctly_detected_fraud = 0
	
	detected_normal = 0
	undetected_fraud = 0
	
	target_id = classes.index(target)
	
	#Dans l'arbre: legit = 0
	#Dans les data: legit = 0
	for line_index,line in enumerate(dataset):
		found = False
		next_tree = tree #Niveau au dessus du nom de la prochaine classe
		previous_tree = next_tree
		class_name = list(tree.keys())[0] #classe dont la valeur est à tester
		while(not found):
			if(class_name in classes):
				try:
					next_tree = next_tree[class_name] #le sous-arbre de cette classe, dans lequel on va chercher la valeur correspondante
					#Niveau à l'intérieur de la classe
				except KeyError as e:
					print(previous_tree)
					print(next_tree)
					print(class_name)
					raise e
				class_index = classes.index(class_name) #l'index de la classe à tester
				class_value = line[class_index] #la valeur de la ligne à faire correspondre pour trouver le prochain
				try:
					previous_tree = next_tree
					next_tree = next_tree[class_value] #Donc, quel est le prochain?
					
					if(isinstance(next_tree,dict)):
						class_name = list(next_tree.keys())[0] #classe dont la valeur est à tester
					else:
						class_name = next_tree
				except(KeyError):
					class_name = majority_answer(next_tree)
					#print("Must go with majority:",class_value)
					#print(next_tree)
					#print(class_value)
					#print("Not found")
			else:
				#pas de sous-arbre correspondant: réponse!
				answer = class_name
				found = True
				real_answer = line[classes.index(target)]
				if(answer != 0 and answer != 1):
					print("Error, answer is not 0 or 1")
					print("Answer is:",answer)
				
				if(real_answer == answer):
					total_correct+=1
					if(real_answer == 0):
						legit_correct+=1
					else:
						frauds_correct+=1
				else:
					error_lines.append(line_index)
					#print(line)
				if(real_answer==0):
					legit_total+=1
				else:
					frauds_total+=1
				
	print("RESULTS======")
	print("Total accuracy:",int(round(total_correct/len(dataset)*100)),"%")
	print("Successful Frauds detection:",int(round(frauds_correct/frauds_total*100)),"%")
	print("Successful Legit detection:",int(round(legit_correct/legit_total*100)),"%")
	#print("Accuracy of Frauds detection:",int(round(frauds_correct/frauds_total*100)),"%")
	#print("Accuracy of Legit detection:",int(round(legit_correct/legit_total*100)),"%")
	print("Legit",legit_total)
	print("Fraud",frauds_total)
	print(len(error_lines),"errors")
	

if __name__ == "__main__":
	filename = "validation_set_extended"
	attributes, validation_set_extended = parse_credits("_Data_"+sep+filename+".csv")
	#import _Output_.creditcard_discretised_graphtree_generated as discretised
	
	filename = "validation_set_undersampled"
	attributes, validation_set_undersampled = parse_credits("_Data_"+sep+filename+".csv")
	import _Output_.training_set_graphtree_generated as undersampled
	
	"""print("We have a biaised dataset of",len(discretised_data),\
	"and balanced sub-samples of",len(undersampled_data))"""
	
	"""print("Trying to use total tree (biaised) on total data (self-data)")
	test_tree(discretised.tree,attributes,"Class",discretised_data)"""
	"""print("Using undersampled tree (balanced) on undersample of data (self-data)")
	test_tree(undersampled.tree,attributes,"Class",undersampled_data)
	print("Using undersampled tree (balanced) on total data")
	test_tree(undersampled.tree,attributes,"Class",discretised_data)"""
	print("Using undersampled tree (balanced) on extended data")
	test_tree(undersampled.tree,attributes,"Class",validation_set_extended)
	print("Using undersampled tree (balanced) on undersampled data")
	test_tree(undersampled.tree,attributes,"Class",validation_set_undersampled)
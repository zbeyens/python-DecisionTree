from _Utilities_.parse_credits import parse_credits
from os import sep

def test_tree(tree,classes,target,dataset):
	total_correct = 0
	frauds_total = 0
	legit_total = 0
	frauds_correct = 0
	legit_correct = 0
	error_lines = []
	target_id = classes.index(target)
	for line_index,line in enumerate(dataset):
		#print(tree.keys())
		found = False
		class_name = list(tree.keys())[0]
		#for class_name in tree: #normalement une seule entrée
		while(not found):
			if(class_name in classes):
				class_index = classes.index(class_name)
				class_name = line[class_index]
			else:
				answer = class_name
				found = True
				real_answer = line[classes.index(target)]
				#print(real_answer,answer)
				if(real_answer != answer):
					total_correct+=1
					if(real_answer == 1):
						legit_correct+=1
					else:
						frauds_correct+=1
				else:
					error_lines.append(line_index)
					#print(line)
				if(real_answer==1):
					legit_total+=1
				else:
					frauds_total+=1
	print("RESULTS======")
	print("Total accuracy:",int(round(total_correct/len(dataset)*100)),"%")
	print("Frauds detection:",int(round(frauds_correct/frauds_total*100)),"%")
	print("Legit detection:",int(round(legit_correct/legit_total*100)),"%")
	print(len(error_lines),"errors")
	

if __name__ == "__main__":
	filename = "creditcard_discretised"
	attributes, discretised_data = parse_credits("_Data_"+sep+filename+".csv")
	import _Output_.creditcard_discretised_graphtree_generated as discretised
	
	filename = "creditcard_undersampled"
	attributes, undersampled_data = parse_credits("_Data_"+sep+filename+".csv")
	import _Output_.creditcard_undersampled_graphtree_generated as undersampled
	
	print("We have a biaised dataset of",len(discretised_data),\
	"and balanced sub-samples of",len(undersampled_data))
	
	print("Trying to use total tree (biaised) on total data (self-data)")
	test_tree(discretised.tree,attributes,"Class",discretised_data)
	print("Using undersampled tree (balanced) on undersample of data (self-data)")
	test_tree(undersampled.tree,attributes,"Class",undersampled_data)
	print("Using undersampled tree (balanced) on total data")
	test_tree(undersampled.tree,attributes,"Class",discretised_data)
from _Utilities_.parse_credits import parse_credits
from _DecisionTree_ import DecisionTree
from os import sep
from tkintertree import start

"""Ouvre un fichier donné, lance le générateur de tree, 
créé un .py qui contient l'arbre"""

def main():
	target = "Class"
	##############
	name = "creditcard_undersampled"
	attributes, data = parse_credits("_Data_"+sep+name+".csv")
	
	tree = DecisionTree.createTree(data, attributes, target)
	print("Generated decision tree")
	print(tree)
	f=open("_Output_"+sep+name+"_graphtree_generated.py","w")
	f.write("tree = "+repr(tree))
	f.write("\n")
	f.close()
	
	start(tree)#affiche l'arbre donné
	
	############
	name = "creditcard_discretised"
	attributes, data = parse_credits("_Data_"+sep+name+".csv")
	
	tree = DecisionTree.createTree(data, attributes, target)
	print("Generated decision tree")
	print(tree)
	f=open("_Output_"+sep+name+"_graphtree_generated.py","w")
	f.write("tree = "+repr(tree))
	f.write("\n")
	f.close()
	
	start(tree)#affiche l'arbre donné
	
if __name__ == '__main__':
	main()

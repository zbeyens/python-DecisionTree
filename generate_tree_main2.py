from _Utilities_.parse_credits import parse_credits
from _DecisionTree_ import DecisionTree
from os import sep
from tkintertree import start

"""Ouvre un fichier donné, lance le générateur de tree,
créé un .py qui contient l'arbre"""

def generate_decision_tree(target,name):
    attributes, data = parse_credits("_Data_" + sep + name + ".csv")
	
    tree = DecisionTree.createTree(data, attributes, target)
    print("Generated decision tree")
    # print(tree)
    f = open("_Output_" + sep + name + "_graphtree_generated.py", "w")
    f.write("tree = " + repr(tree))
    f.write("\n")
    f.close()
	
    target_values = sorted(set((line[attributes.index(target)] for line in data)))
    start(tree,target_values = target_values,dimensions=(1000,500))  # affiche l'arbre donné
def main():
    target = "Victim Sex"
    ##############
    name = "validation_set2"
    generate_decision_tree(target,name)
    name = "training_set2_full"
    generate_decision_tree(target,name)
    
	

if __name__ == '__main__':
    main()

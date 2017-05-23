from _Utilities_.parse_credits import parse_credits
from _DecisionTree_ import DecisionTree
from os import sep
from tkintertree import start

"""Ouvre un fichier donné, lance le générateur de tree, 
créé un .py qui contient l'arbre"""
def main():
    """
	Exemple basique:
    target = "Class"
    data = [
        ["Hair", "Height", "Weight", "Lotion", "Class"],
        ["Blonde", "Average", "Light", "No", "Burned"],
        ["Blonde", "Tall", "Average", "Yes", "Not burned"],
        ["Brown", "Short", "Average", "Yes", "Not burned"],
        ["Blonde", "Short", "Average", "No", "Burned"],
        ["Red", "Average", "Heavy", "No", "Burned"],
        ["Brown", "Tall", "Heavy", "No", "Not burned"],
        ["Brown", "Average", "Heavy", "No", "Not burned"],
        ["Blonde", "Short", "Light", "Yes", "Not burned"],
    ]

    attributes = data[0]
    data.pop(0)
    """
    attributes, data = parse_credits("_Data_"+sep+"creditcard_undersampled.csv")
    #attributes, data = parse_credits("creditcard_simplified.csv")
    target = attributes[-1]
    

    # Run ID3
    tree = DecisionTree.createTree(data, attributes, target)
    print(tree)
    print("generated decision tree")
    f=open("_Output_"+sep+"graphtree_generated.py","w")
	
    
    f.write("tree = "+repr(tree))
    f.write("\n")
    f.close()
    
    start(tree)#affiche l'arbre donné
if __name__ == '__main__':
    main()

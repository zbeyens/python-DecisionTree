from _Utilities_.parse_credits import parse_credits
from _DecisionTree_ import DecisionTree
from os import sep

def main():
    # Insert input file
    # IMPORTANT: Change this file path to change training data
    # file = open('SoybeanTraining.csv')

    # IMPORTANT: Change this variable too change target attribute
    """
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
    """
    global graph
    graph = pydot.Dot(graph_type='graph')
    visit(tree)
    graph.write_png('example1_graph.png')"""
    f=open("_Output_"+sep+"graphtree_generated.py","w")
    
    f.write("tree = "+repr(tree))
    f.write("\n")
    f.close()

if __name__ == '__main__':
    main()

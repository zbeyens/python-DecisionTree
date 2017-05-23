import DecisionTree
import networkx as nx
import numpy as np
from parse_credits import parse_credits
from collections import Mapping


def draw():
	
	graph_data = {"root": {"level-0.A":0,
						  "level-0.B":{"level-1.B.1":2,
									   "level-1.B.2": {"level-2.B.2.1":3, "level-2.B.2.2":1}}}}
	# Empty directed graph
	G = nx.DiGraph()

	# Iterate through the layers
	q = list(graph_data.items())
	while q:
		v, d = q.pop()
		for nv, nd in d.items():
			G.add_edge(v, nv)
			if isinstance(nd, Mapping):
				q.append((nv, nd))

	np.random.seed(8)
	nx.draw(G, with_labels=True)
            
def main():
    # Insert input file
    # IMPORTANT: Change this file path to change training data
    # file = open('SoybeanTraining.csv')

    # IMPORTANT: Change this variable too change target attribute
    """target = "Class"
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
    data.pop(0)"""
    attributes, data = parse_credits("creditcard_undersampled.csv")
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
    draw()



if __name__ == '__main__':
    main()

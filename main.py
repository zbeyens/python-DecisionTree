import DecisionTree
from parse_credits import parse_credits

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
    attributes, data = parse_credits("creditcard_simplified.csv")
    target = attributes[-1]

    # Run ID3
    tree = DecisionTree.createTree(data, attributes, target)
    print(tree)
    print("generated decision tree")


if __name__ == '__main__':
    main()

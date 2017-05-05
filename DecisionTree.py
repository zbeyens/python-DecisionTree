import math

# find item in a list


# def find(item, list):
#     for i in list:
#         if item(i):
#             return True
#         else:
#             return False

def getAttrValues(data, attributes, attr):
    # get the different values in the column of the given attribute
    i = attributes.index(attr)
    values = []
    for line in data:
        if line[i] not in values:
            values.append(line[i])
    return values


def getSubDataset(data, attributes, best, val):
    """
    Get the dataset corresponding to the best attribute (without best attr data)
    """
    subData = [[]]
    index = attributes.index(best)

    for line in data:
        # find the lines with val in the best attr
        if (line[index] == val):
            newLine = []
            # add value (not in best attr)
            for i in range(0, len(line)):
                if (i != index):
                    newLine.append(line[i])
            subData.append(newLine)
    subData.remove([])
    return subData


def calcFreqTarget(data, i):
    # compute frequency of values in target attribute
    freqTarget = {}

    for line in data:
        if (line[i] in freqTarget):
            freqTarget[line[i]] += 1.0
        else:
            freqTarget[line[i]] = 1.0

    return freqTarget


def majority(attributes, data, target):
    # get target index
    i = attributes.index(target)

    freqTarget = calcFreqTarget(data, i)

    # find the major value in the target attribute
    majorVal = ""
    maxFreq = 0
    for key in freqTarget.keys():
        if freqTarget[key] > maxFreq:
            maxFreq = freqTarget[key]
            majorVal = key
    return majorVal


# Calculates the entropy of the given data set for the target attr
def calcEntropy(data, attributes, target):
    # find index of the target attribute
    # i = 0
    # for attr in attributes:
    #     if (target == attr):
    #         break
    #     ++i
    i = attributes.index(target)

    freqTarget = calcFreqTarget(data, i)

    subEntropy = 0.0
    # Calculate the entropy of the data for the target attr
    for freq in freqTarget.values():
        pi = freq / len(data)
        subEntropy += (-pi) * math.log(pi, 2)

    return subEntropy


def gain(data, attributes, target, targetEntropy, attr):
    """
    Compute the information gain by splitting the data on attr.
    """
    i = attributes.index(attr)

    # compute frequency of values in attr
    freqTarget = calcFreqTarget(data, i)

    allSubEntropy = 0.0
    # compute the weighted sum of the entropy for each value in attr
    for val in freqTarget.keys():
        # get the probability of this value
        freqTotal = sum(freqTarget.values())
        probVal = freqTarget[val] / freqTotal

        # get all the lines with this value
        dataSubset = []
        for line in data:
            if line[i] == val:
                dataSubset.append(line)

        # add the entropy of this value to allSubEntropy
        allSubEntropy += probVal * calcEntropy(dataSubset, attributes, target)

    # Subtract the entropy of the entire dataSet by the entropy on this attr
    return (targetEntropy - allSubEntropy)


def findBestAttr(data, attributes, target):
    """
    Find the best attibute with the best information gain
    """
    targetEntropy = calcEntropy(data, attributes, target)
    bestAttr = ""
    maxGain = 0
    for attr in attributes:
        if attr == target:
            continue
        print(attr)
        newGain = gain(data, attributes, target, targetEntropy, attr)
        print("gain", newGain)
        if newGain > maxGain:
            bestAttr = attr
            maxGain = newGain
    return bestAttr


def createTree(data, attributes, target):
    """
    Create a tree level by level (recursively)
    Params:
    data: line by line [[]]
    attributes: first line [attr]
    target: String, attr
    """

    targetMajor = majority(attributes, data, target)
    # len attributes without the target
    lenAttr = len(attributes) - 1

    targetVals = []
    for line in data:
        targetVals.append(line[attributes.index(target)])

    # If the dataset is empty or the attributes list is empty, return
    # targetMajor. We can not continue the branching.
    # END OF THE BRANCH by choosing the BEST TARGET
    if not data or lenAttr < 1:
        print("END - MAJOR TARGET", targetMajor)
        return targetMajor

    # If all the targetValues have the same value, return this value.
    # Useless to continue the branching.
    # END OF THE BRANCH by choosing the ONLY ONE TARGET
    elif targetVals.count(targetVals[0]) == len(targetVals):
        print("END - ONE TARGET", targetVals[0])
        return targetVals[0]

    # We can continue the branching.
    else:
        # Find the next best attribute that best classifies the dataset
        best = findBestAttr(data, attributes, target)
        print("Best attribute is", best)

        # Create a new decision tree with the chosen node.
        tree = {best: {}}

        # Create a new decision subtree for all the best attribute values
        for val in getAttrValues(data, attributes, best):
            subData = getSubDataset(data, attributes, best, val)

            # remove best attr
            newAttr = attributes[:]
            newAttr.remove(best)

            # recursively
            print("\nNew tree on", val)
            subTree = createTree(subData, newAttr, target)
            print(subTree)

            tree[best][val] = subTree

    return tree

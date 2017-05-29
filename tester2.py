from _Utilities_.parse_credits import parse_credits
from os import sep


def majority_answer(tree, target_values):
    # Explore l'arbre et renvoie la valeur majoritaire
    # Pondérée par la profondeur et le nombre d'enfants
    to_explore = [(tree, 1)]
    target_count = [0 for x in target_values]
    while(to_explore):
        tree, level = to_explore.pop()
        level /= len(tree)
        for key in tree:
            subtree = tree[key]
            if(isinstance(subtree, dict)):
                to_explore.append((subtree, level))
            else:
                target_count[target_values.index(subtree)]+=level
    if not(abs(sum(target_count) - 1) <= 0.0000001):
        # Juste pour vérifier que leur somme fasse bien 1
        print((str(target_values[i])+":"+str(target_count[i]) for i in range(len(target_values))))
        print(sum(target_count))
    majo = max(target_count)
    return target_values[target_count.index(majo)]


def test_tree(tree, classes, target, dataset):
    total_correct = 0
    error_lines = []

    target_id = classes.index(target)
    target_values = sorted(set(line[target_id] for line in dataset) )
    total_target_counts = [0 for x in target_values]
    correct_target_counts = [0 for x in target_values]
    print(target_values)

    # Dans l'arbre: legit = 0
    # Dans les data: legit = 0
    for line_index, line in enumerate(dataset):
        found = False
        next_tree = tree  # Niveau au dessus du nom de la prochaine classe
        previous_tree = next_tree
        class_name = list(tree.keys())[0]  # classe dont la valeur est à tester
        while(not found):
            if(class_name in classes):
                try:
                    # le sous-arbre de cette classe, dans lequel on va chercher
                    # la valeur correspondante
                    next_tree = next_tree[class_name]
                    # Niveau à l'intérieur de la classe
                except KeyError as e:
                    print(previous_tree)
                    print(next_tree)
                    print(class_name)
                    raise e
                # l'index de la classe à tester
                class_index = classes.index(class_name)
                # la valeur de la ligne à faire correspondre pour trouver le
                # prochain
                class_value = line[class_index]
                try:
                    previous_tree = next_tree
                    # Donc, quel est le prochain?
                    next_tree = next_tree[class_value]

                    if(isinstance(next_tree, dict)):
                        # classe dont la valeur est à tester
                        class_name = list(next_tree.keys())[0]
                    else:
                        class_name = next_tree
                except(KeyError):
                    class_name = majority_answer(next_tree,target_values)
                    # print("Must go with majority:",class_value)
                    # print(next_tree)
                    # print(class_value)
                    # print("Not found")
            else:
                # pas de sous-arbre correspondant: réponse!
                answer = class_name
                found = True
                if not(answer in target_values):
                    print("Error, answer is not target")
                    print("Answer is:", answer)
                real_answer = line[classes.index(target)]
                answer_id = target_values.index(answer)
                real_answer_id = target_values.index(real_answer)

                if(real_answer == answer):
                    total_correct += 1
                    correct_target_counts[real_answer_id] += 1
                else:
                    error_lines.append(line_index)
                    # print(line)
                total_target_counts[answer_id] += 1

    print("RESULTS======")
    print("Total accuracy:", int(round(total_correct / len(dataset) * 100)), "%")
    for t in target_values:
        i = target_values.index(t)
        print("Successful",t,"detection:",\
            int(correct_target_counts[i] / max(1,total_target_counts[i]) *100),"%")
    for t in target_values:
        print(t,total_target_counts[target_values.index(t)])
    print(len(error_lines), "errors")


if __name__ == "__main__":

    filename = "validation_set2"
    attributes, validation_set2 = parse_credits(
        "_Data_" + sep + filename + ".csv")
    import _Output_.training_set2_graphtree_generated as undersampled

    print("Using undersampled tree (balanced) on extended data")
    test_tree(undersampled.tree, attributes, "Victim Sex", validation_set2)

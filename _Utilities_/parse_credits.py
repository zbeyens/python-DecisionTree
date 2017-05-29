def parse_credits(filename="_Data_/creditcard_simplified.csv"):
    f = open(filename)
    attributes = f.readline().strip().split(",")

    # database = [[] for x in classes]
    database = []

    maxlines = float("inf")  # 10000 #
    for line in f:
        line = line.strip().split(",")
        line = [x for x in line]
        # for i, elem in enumerate(line):
        # database[i].append(elem)
        database.append(line)

        if(len(database[0]) >= maxlines):
            break
    f.close()
    return attributes, database

def dotProduct(listA, listB):
    output = 0
    for i, v in enumerate(listA):
        output += listB[i] * v

    return output




print(         dotProduct([1, 2, 3], [4, 5, 6])          )
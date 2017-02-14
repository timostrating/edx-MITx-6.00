def flatten(aList):
    ListCopy = []
    for v in aList:
        if isinstance(v, list):
            ListCopy.extend( flatten(v) )
        else:
            ListCopy.append(v)

    return ListCopy



print(            flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])           )
def f(a, b):
    return a + b


def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for key in d1:
        if key in d2:
            difference[key] = f( d1[key], d2[key] )
        else:
            intersect[key] = d1[key]

    for key in d2:
        if key not in d1:
           intersect[key] = d2[key]

    return (difference, intersect,)




print(       dict_interdiff({1:30, 2:20, 3:30, 5:80},  {1:40, 2:50, 3:60, 4:70, 6:90})         )
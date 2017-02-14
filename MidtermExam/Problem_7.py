def f(a, b):
    return a + b


# def dict_interdiff(d1, d2):
#     intersect = {}
#     difference = {}
#
#     for key in d1.keys():
#         if key in d2:
#             intersect[key] = d1[key]
#
#     for key in d1.keys():
#         if key not in d2:
#             difference[key] = d1[key]
#         elif d1[key] != d2[key]:
#             difference[key] = d1[key] + d2[key]
#
#     for key in d2.keys():
#         if key not in d2:
#             difference[key] = d2[key]
#
#     return (intersect, difference,)

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

# def dict_interdiff(d1, d2):
#     keyd1 = set(d1)
#     keyd2 = set(d2)
#     keySetInter = keyd1.intersection(keyd2)
#     keySetDiff = keyd1
#     keySetDiff ^= keyd2
#
#     if keyd1 != keyd2:
#         newList = (dict.fromkeys(keySetInter,0),dict.fromkeys(keySetDiff,0))
#         for i in keySetInter:
#             newList[0][i] = d1.get(i)+d2.get(i)
#         for i in keySetDiff:
#             if i in d1:
#                 newList[1][i] = d1.get(i)
#             if i in d2:
#                 newList[1][i] = d2.get(i)
#
#     else:
#         newList = ({},{})
#
#         for i, j in zip(d1,d2):
#             if i > j:
#                 newList[0].update({i:False})
#             else:
#                 newList[0].update({i:True})
#
#     return newList



print(       dict_interdiff({1:30, 2:20, 3:30, 5:80},  {1:40, 2:50, 3:60, 4:70, 6:90})         )
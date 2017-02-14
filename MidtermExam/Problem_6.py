def deep_reverse(L):
    L.reverse()
    for v in L:
        if isinstance(v, list):
            deep_reverse(v)


L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)
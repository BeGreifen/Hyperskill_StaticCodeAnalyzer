from copy import deepcopy


def solve(obj):
    return id(obj) != id(deepcopy(obj))

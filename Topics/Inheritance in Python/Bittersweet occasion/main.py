# finish the function
def find_the_parent(child):
    for el in [Drinks, Pastry, Sweets]:
        if issubclass(child, el):
            print(el.__name__)
iris = {}


def add_iris(*args, **kargs):
    global iris
    id_n = args[0]
    flower_details = {}
    flower_details["species"] = args[1]
    flower_details["petal_length"] = args[2]
    flower_details["petal_width"] = args[3]
    flower_details.update(**kargs)
    iris[id_n] = flower_details
    pass

# x = add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
#   print(iris)
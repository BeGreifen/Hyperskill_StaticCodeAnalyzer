iris = {}


def add_iris(id_n: int, species: str, petal_length: float, petal_width: float, **kwargs):
    iris[id_n] = {"species": species,
                  "petal_length": petal_length,
                  "petal_width": petal_width,
                  **kwargs}

#  _ = add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
#  print(iris)

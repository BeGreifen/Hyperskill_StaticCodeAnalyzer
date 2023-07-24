class Star:
    def __init__(self, name, spectral_class):
        self.name = name
        self.spectral_class = spectral_class

# create a child class here
class YellowDwarf(Star):
    def __repr__(self):
        return f"{self.name}, {self.spectral_class}"

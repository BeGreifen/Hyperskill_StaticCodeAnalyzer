class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    def __str__(self):
        return self.name


if __name__ == '__main__':
    seine = River("Seine", 777)

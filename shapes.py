class Square():
    NO_OF_EDGES = 4

    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge * self.edge


class Circle():
    PI = 3.141592

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * (self.radius ** 2)

    def circumference(self):
        return 2 * Circle.PI * self.radius

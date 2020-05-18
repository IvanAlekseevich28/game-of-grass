import json

Grass_maxGrow = 9

class Grass:
    def __init__(self, grow = 0, color = 0):
        self.grow = grow
        self.color = color


    def copy(self):
        return Grass(self.grow, self.color)


    def isLife(self) -> bool:
        return self.grow != 0


    def toAlive(self):
        if self.grow < Grass_maxGrow:
            self.grow += 1


    def toDie(self):
        self.grow = 0
        self.color += 1


    def __str__(self):
        return str(self.grow)


from grass import Grass
from rules import Rule
from conseedset import StartBoardGenerator
import numpy as np
from collections import namedtuple
from soil import Soil


Cell = namedtuple('Cell', ['x', 'y', 'grow', 'color'])


class Simulator:
    
    def __init__(self, rule : Rule, square_face):
        self.face   = int(square_face)
        self.rule   = rule
        self.field = self.getZeroField()
        self.soil = Soil(square_face, rule.PMR, 1000)


    def getZeroField(self):
        field = np.zeros([self.face, self.face], dtype=object)
        
        for row in range(self.face):
            for col in range(self.face):
                field[row][col] = Grass(0, 0)

        return field


    def setSeed(self, seedSet : set):
        for el in seedSet:
            self.field[int(el[1])][int(el[0])].toAlive()

    
    def getCells(self) -> set:
        cells = set()
        for row in range(self.face):
            for col in range(self.face):
                grass = self.field[row][col]
                if grass.isLife():
                    cells.add(Cell(col, row, grass.grow, grass.color))

        return cells


    def getCountOfNeighbours(self, row, col):
        up = int(self.face)
        rad = int(self.rule.radius)

        horizontalLow  = row - rad
        horizontalLow  = 0 if horizontalLow < 0 else horizontalLow
        horizontalHigh = row + rad + 1
        horizontalHigh = up if horizontalHigh > up else horizontalHigh

        verticalLow  = col - rad
        verticalLow  = 0 if verticalLow < 0 else verticalLow
        verticalHigh = col + rad + 1
        verticalHigh = up if verticalHigh > up else verticalHigh

        neighbours = -1 if self.field[row][col].isLife() else 0

        for y in range(horizontalLow, horizontalHigh):
            for x in range(verticalLow, verticalHigh):
                if self.field[y][x].isLife():
                    neighbours += 1

        return neighbours


    def simulateStep(self):
        f = self.getZeroField()
        for row in range(self.face):
            for col in range(self.face):
                n = self.getCountOfNeighbours(row, col)
                oldG = self.field[row][col]
                newG = self.rule.executeRule(oldG, n)
                # if newG.isLife():
                #     if newG.grow > oldG.grow:
                #         if self.soil.rem_value(row, col, self.rule.PU):
                #             newG.grow -= 1

                f[row][col] = newG
                
        self.field = f


    def getGrowMatrix(self):
        m = np.zeros([self.face, self.face], dtype=np.int32)
        for row in range(self.face):
            for col in range(self.face):
                m[row][col] = self.field[row][col].grow

        return m
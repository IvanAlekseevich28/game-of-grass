from collections import namedtuple
from random import randint
import json

Point = namedtuple('Point', ['x', 'y'])

class StartBoardGenerator:
    def __init__(self, file_name, square_face = 15):
        self.square_face = square_face
        self.file_name = file_name
        self.board = set()


    def consInit(self):
        self.square_face = int(input("Input square face: "))
        mode = input("How to fill board? (Hand/Random)")
        if mode == 'Hand':
            self.initHand()
        else:
            density = float(input('Input density of life cell (0-1): '))
            self.initRandom(density)
        

    def initHand(self):
        count = input("Input count of points: ")
        for _ in range(int(count)):
            x, y = input("x y: ").split()
            self.board.add(Point(int(x), int(y)))


    def initRandom(self, density = 0.5):
        for x in range(self.square_face):
            for y in range(self.square_face):
                if (randint(1, 101) < density * 100):
                    self.board.add(Point(x, y))



    def showSelf(self):
        print("Start seed")
        print(self.board)


    def fileSave(self):
        f = open(self.file_name, 'w')

        jsonDict = {
            'Seed' : {
                'Square face'   : self.square_face,
                'Points'        : list(self.board)
            }
        }
        json.dump(jsonDict,f, indent=4)

        f.close()


    def fileLoad(self):
        try:
            f = open(self.file_name, 'r')
            
            jsonData = json.load(f)

            if 'Seed' not in jsonData:
                return False

            js = jsonData['Seed']
            self.square_face = js['Square face']
            listData = js['Points']
            for el in listData:
                self.board.add(Point(el[0], el[1])) 

            f.close()

        except:
            return False

        return True


    def printPoints(self):
        for el in self.board:
            print(el)



if __name__ == '__main__':
    generator = StartBoardGenerator("startPoints.json")
    # generator.consInit()
    # generator.fileSave()
    generator.fileLoad()
    generator.printPoints()

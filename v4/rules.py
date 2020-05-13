from collections import namedtuple
from grass import Grass
import json


class Rule:

    def __init__(self, appear_range = range(3,4), survival_range = range(2,4), radius = 1):
        self.appear = appear_range
        self.surv = survival_range
        self.radius = radius        # Raduis of search neighbours e.g. 1->8, 2->24, 5->120


    def consInit(self):
        self.radius = int(input("Input radius of searching neighbours: "))
        maxStopValue = (self.radius + 2) ** 2
        startA, stopA = input("Input appear range (start stop(" + str(maxStopValue) +")): ").split()
        startS, stopS = input("Input survival range (start stop(" + str(maxStopValue) +")): ").split()
        self.appear = range(int(startA), int(stopA))
        self.surv = range(int(startS), int(stopS))
        print("Done!")


    def executeRule(self, const_grass : Grass, countNeighbours : int):
        grass = const_grass.copy()
        if grass.isLife():
            if countNeighbours in self.surv:
                grass.toAlive()
            else:
                grass.toDie()
        else:
            if countNeighbours in self.appear:
                grass.toAlive()

        return grass


    def objToJson(self, fileName):
        f = open(fileName, 'w')

        jsonDict = {
            'Rule' : {
                'appear_range' : {
                    'start' : self.appear.start,
                    'stop'  : self.appear.stop
                },
                'survival_range' : {
                    'start' : self.surv.start,
                    'stop'  : self.surv.stop
                },
                'radius' : self.radius
            }
        }        
        json.dump(jsonDict, f, indent=4)

        f.close


    def jsonToObj(self, fileName):
        f = open(fileName, 'r')
        jsonDict = json.load(f)
        jr = jsonDict['Rule']
        self.appear = range(jr['appear_range']['start'], jr['appear_range']['stop'])
        self.surv   = range(jr['survival_range']['start'], jr['survival_range']['stop']) 
        self.radius = jr['radius']
        f.close()



if __name__ == '__main__':   

    r1 = Rule()
    r1.consInit()
    r1.objToJson('rule.json')

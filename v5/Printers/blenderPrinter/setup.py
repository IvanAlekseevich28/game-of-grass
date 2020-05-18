import json



class Setup:
    def __init__(self, outputDir = '?', inputFile = '?', FPS = 5, fileNameSetup = 'setup.json'):
        self.outputDir = outputDir
        self.inputFile = inputFile
        self.FPS = int(FPS)
        self.FNS = fileNameSetup


    def consInitOutputDir(self):
        self.outputDir = input("Input output directory: ")


    def consInitSource(self):
        self.inputFile = input("Input source file: ")


    def consInitFPS(self):
        self.FPS = int(input("Input fps count: "))


    def consInit(self):
        self.consInitOutputDir()
        self.consInitSource()
        self.consInitFPS()


    def showSelf(self):
        print("setup config:")
        print("FPS = " + str(self.FPS))
        print("output: " + self.outputDir)
        print("source: " + self.inputFile)
        print("class save file: " + self.FNS)



    def load(self):
        try:
            f = open(self.FNS, 'r')
            jsonDict = json.load(f)
            if 'setup' not in jsonDict:
                print("Rule not found")
                return False
            f.close()    

            js = jsonDict['setup']

            self.FPS = js['fps']
            self.outputDir = js['outFD']
            self.inputFile = js['inFN']
        except:
            print('File has not configured!')
            return False

        return True

    
    def save(self):
        jsonDict = {
            'setup' : {
                'fps' : self.FPS,
                'outFD' : self.outputDir,
                'inFN' : self.inputFile
            }
        }

        f = open(self.FNS, 'w')
        json.dump(jsonDict, f)
        f.close()



if __name__ == '__main__':
    s = Setup()
    if s.load():
        s.showSelf()
    else:
        s.consInit()
        s.save()
    




    
    
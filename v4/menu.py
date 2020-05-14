from rules import Rule


mainMenu = ('Start simulation',
            'Set count of iteration',
            'Set seed',
            'Set rule',
            'Set file seed',
            'Set file rule'
            )

class Menu:
    def __init__(self, consoleMode = False):
        self.consoleMode = consoleMode

    
    def askAction(self, menu : list)-> str:
        if self.consoleMode == False:
            return 1

        i = 1
        for el in menu:
            print(str(i) + '. ' + str(el))
            i += 1

        action = str() 
        while True:
            action = input('Select action: ')
            if action in range(1, i):
                break

        return action

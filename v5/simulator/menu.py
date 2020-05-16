mainMenu = ('Start simulation',
            'Set count of iteration',
            'Set seed',
            'Set rule',
            'Set file seed',
            'Set file rule'
            )

def askAction(menu: list) -> int:
    i = 1
    for el in menu:
        print(str(i) + '. ' + str(el))
        i += 1

    action = -1
    while True:
        action = int(input('Select action: '))
        if action in range(1, i):
            break

    return action


def askIterations() -> int:
    

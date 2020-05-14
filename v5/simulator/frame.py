import json
from collections import namedtuple


Cell = namedtuple('Cell', ['x', 'y', 'grow', 'color'])


def frameToJsonFile(listSetNamedtupleOfCells : list,
                    fileName : str,
                    consoleMode = False):
    f = open(fileName, 'w')

    frames = list()
    for frame in listSetNamedtupleOfCells:  # Set of namedtuple
        board = list()                      # One frame
        for cell in frame:                  # Namedtuple with one cell
            board.append({
                'Cell' : {
                    'x'     : cell.x,
                    'y'     : cell.y,
                    'grow'  : cell.grow,
                    'color' : cell.color
                }
            })
        frames.append(board)

    jsonDict = {
        'Frames' : frames
    }

    json.dump(jsonDict, f, indent=4)
    f.close()


def JsonFileToFrames(fileName) -> list:
    frames = list()
    try:
        f = open(fileName, 'r')
        jsonDict = json.load(f)
        if 'Frames' not in jsonDict:
            return False

        jf = jsonDict['Frames']
        for frame in jf:
            cells = list()
            for c in frame:
                cells.append(Cell(  c['x'],
                                    c['y'],
                                    c['grow'],
                                    c['color']
                                    ))

            frames.append(cells)


    except:
        return list()

    return frames
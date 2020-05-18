from frame import JsonFileToFrames
import numpy as np
import os
from time import sleep

frames = JsonFileToFrames('out2.json')
print('Frames count = '+str(len(frames)))
iter = 0
for fr in frames:
    mat = np.zeros([20, 20], dtype=np.int32)
    for cell in fr:
        mat[cell.y][cell.x] = cell.grow
    # os.system("clear")
    print('#'+ str(iter))
    print(mat)
    iter += 1
    sleep(0.1)

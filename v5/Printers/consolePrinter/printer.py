from frame import JsonFileToFrames
import numpy as np

frames = JsonFileToFrames('out.json')
print('Frames count = '+str(len(frames)))
iter = 0
for fr in frames:
    mat = np.zeros([10, 10], dtype=np.int32)
    for cell in fr:
        mat[cell.y][cell.x] = cell.grow
    
    print('#'+ str(iter))
    print(mat)
    iter += 1

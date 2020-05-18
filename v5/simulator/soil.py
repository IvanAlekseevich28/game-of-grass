import numpy as np
from random import randint
import time
import os

class Soil:
    def __init__(self, size, PMR = 0, value = 1):
        self.PMR = PMR
        self.MTS = size
        self.MTR = np.zeros((size, size), dtype=np.uint32)
        if value:
            self.MTR += value
    

    def add_value(self, row, col, value) -> bool:
        if self.valid_possition(row, col):
            self.MTR[row, col] += value
            return True
        else:
            return False


    def rem_value(self, row, col, value) -> int:
        if self.valid_possition(row, col):
            difference = self.MTR[row, col] - value
            if difference >= 0:
                self.MTR[row, col] -= value
                return int(0)
            else:
                self.MTR[row, col] = 0
                return int(-difference)
        else:
            return int(-1)

        
    def mix(self):
        new_matrix = np.zeros((self.MTS, self.MTS), dtype=np.uint32)
        for row in range(self.MTS):
            for col in range(self.MTS):
                balance = self.MTR[row,col] // (8*(1+self.PMR))
                self.MTR[row,col] -= 8*balance
                for i in range(9):
                    if i == 4:
                        continue

                    R = (row + 1 - (i % 3)) % self.MTS
                    C = (col + 1 - (i // 3)) % self.MTS
                    new_matrix[R,C] += balance

        self.MTR += new_matrix


    def valid_possition(self, row, col):
        if row in range(self.MTS) and col in range(self.MTS):
            return True
        else:
            return False


                




if __name__ == '__main__':
    s = Soil(3,2,100)
    s.rem_value(1,1, 200)
    print(s.MTR)
    start = time.time()
    count = 1000
    for i in range(count):  
        s.mix()
        if ((i+1)%2) == 0:
            os.system('clear')
            print(str(int((i+1)/count * 100)) + ' %')
        
        #print(s.MTR)
        #time.sleep(3)
    
    print((time.time()-start) / 60)
    print(s.MTR)
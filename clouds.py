import pyxel
from random import randint
import random
from mario import Mario
from Blocks import Bricks

class Clouds:
    def __init__(self):
        self.clouds_x1 = 10
        self.clouds_y1 = 15
        self.clouds_x2 = 105
        self.clouds_y2 = 5
        

    def update(self):
        #update position of clouds
        if pyxel.btn(pyxel.KEY_RIGHT):
                self.clouds_x1 = self.clouds_x1 - 1
                self.clouds_x2 = self.clouds_x2 - 1
                #print("x: ",self.clouds_x)
    
    def draw(self):
        #only two cloud with random postions y - coordinate
        if self.clouds_x1 < - 42:
            self.clouds_x1 = 160
            self.clouds_y1 = random.randint(5,20)
        if self.clouds_x2 < -42:
            self.clouds_x2 = 160
            self.clouds_y2 = random.randint(5,20)
        pyxel.blt(self.clouds_x1, self.clouds_y1, 0, 20, 68, 42, 23.5, 13)
        pyxel.blt(self.clouds_x2, self.clouds_y2, 0, 20, 68, 42, 23.5, 13)
    


Clouds()
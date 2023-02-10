import pyxel
from random import randint
import random
from mario import Mario
from Blocks import Bricks
from clouds import Clouds
from pipes import Pipes

class High_Blocks:
    def __init__(self):
        self.high_x = 65
        self.high_y = 50
        self.counter = 0
    
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.high_x = self.high_x - 1
            if self.high_x == -48 and self.counter != 0:
                self.high_x = 160
            self.counter += 1
    
    def draw(self):
        #pyxel.blt(self.high_x,self.high_y, 0, -10, 0, 50, 50, 12)
        pyxel.blt(self.high_x,self.high_y, 0, 0, 16, 16, 15, 12)
        pyxel.blt(self.high_x + 16,self.high_y, 0, 16.5, 0, 16, 15, 12)
        pyxel.blt(self.high_x + 32,self.high_y, 0, 0, 16, 16, 15, 12)
        
        #animation after got coin/ mushroom from high_block
        #pyxel.blt(self.high_x + 40,self.high_y, 0, 16.5, 16.5, 16, 15, 12)
        
    
High_Blocks()

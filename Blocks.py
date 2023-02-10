import random 
import pyxel 
from random import randint
from mario import Mario

class Bricks:
    def __init__(self):
        self.bricks_x = 0
        self.init_pos = [0,16,32,48,64,80,96,112,128,144,160]
        self.mario = Mario()

    def update(self):
        #update position of bricks when right key pressed
        if pyxel.btn(pyxel.KEY_RIGHT):
            for r in range(11):
                self.bricks_x = self.init_pos[r] - 1
                if self.bricks_x < -15:
                    self.bricks_x = 160
                    self.init_pos[r] = self.bricks_x
                else:
                    self.init_pos[r] = self.bricks_x
                #print("Positions: ",self.init_pos.sort())
            
                
                     
              
    def draw(self):
        #sort the x coordinate of the blocks
        self.init_pos.sort()
        #draw block with x-coordinate self.init[r]
        for r in range(11):
            pyxel.blt(self.init_pos[r], 99, 0, 32, 104, 16, 15, 12)
            pyxel.blt(self.init_pos[r], 114, 0, 32, 104, 16, 15,12)
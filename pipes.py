import pyxel
from random import randint
import random
from mario import Mario
from Blocks import Bricks
from clouds import Clouds

class Pipes():
    def __init__(self):
        self.pipes_x = 160
        self.pipes_y = 69
        self.counter = 0
        self.can_appear = True
        #self.in_map == False

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pipes_x = self.pipes_x - 1
            if self.pipes_x == -48 and self.counter != 0:
                self.pipes_x = 160
                self.pipes_y = random.randint(69,80)
            self.counter += 1
                
    def draw(self):
        #print(f"pipes coordinates: {(self.pipes_x,self.pipes_y)}")
        pyxel.blt(self.pipes_x, self.pipes_y, 0, 32, 0, 32.5, 30, 12)
        



Pipes()
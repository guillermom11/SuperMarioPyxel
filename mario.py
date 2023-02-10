import random 
import pyxel 
from random import randint

class Mario:
    def __init__(self):
        self.player_x = 5
        self.player_y = 84
        self.player_vy = 84
        self.jump = False
        self.jump_speed = 9
    
    def move(self):
        #can just jump if its on physical object
        self.in_floor = False
        if self.player_y == 84:
            self.in_floor = True
            
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 1, pyxel.width - 81) #was in 16 (comment just for us)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 1, 0)
        
        if not self.jump:
            if pyxel.btn(pyxel.KEY_UP) and self.in_floor:
                self.jump = True
                
                
        else:
            if self.jump_speed >= -9:
                direction = 1
                if self.jump_speed < 0:
                    direction = -1
                self.player_y -= (self.jump_speed ** 2) * 0.2 * direction
                self.jump_speed -= 1
            else:
                self.jump = False
                self.jump_speed = 9
        
            return self.player_x, self.player_y, self.player_vy
    
    
        


    def draw(self):
        pyxel.blt(self.player_x,self.player_y, 0, 0, 48.5, 16, 15, 12)


Mario()
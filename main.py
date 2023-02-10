import pyxel
from random import randint
import random
from mario import Mario
from Blocks import Bricks
from clouds import Clouds
from pipes import Pipes
from High_Blocks import High_Blocks

class App:
    def __init__(self):
        pyxel.init(160, 120, caption = "Super Mario Bros")
        pyxel.load("assets/marioassets.pyxres")
        self.mario = Mario()
        self.brick = Bricks()
        self.cloud = Clouds()
        self.pipe = Pipes()
        self.high_block = High_Blocks()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        else:
            self.mario.move()
        self.brick.update()
        self.cloud.update()
        self.pipe.update()
        self.high_block.update()

    def draw(self):
        # blue background
        pyxel.cls(12)
        # draw trees
        pyxel.blt(100, 87, 0, 20, 90, 40, 12)
        pyxel.blt(20, 87, 0, 20, 90, 40, 12)
        
        
        self.mario.draw()
        self.pipe.draw()
        self.brick.draw()
        self.cloud.draw()
        self.high_block.draw()
        

        # draw mountains
        #pyxel.blt(40, 30, 0, 0, 5, 60, 90)


        #draw floor blocks and half floor blocks
        
              
           
                






















        

        
        #draw pipes
        #offset3 = pyxel.frame_count % 160
        #for i in range(2):
            #pyxel.blt(i * 160 - offset3, 69, 0, 32, 0, 32.5, 30, 12)
            
               
        


           
        #draw score
        #s = "MARIO{:>4}".format(self.score)
        #pyxel.text(4, 2, s, 7)

        #draw world
        #w1 = "WORLD"
        #pyxel.text(100, 2, w1, 7)
        #w2 = "1-1"
        #pyxel.text(104, 9, w2, 7)
    

App()


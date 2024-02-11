import pygame as py
from PygameUtil import PygameUtil
from Screens import Screens
import random
import sys
class decoder(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)
        
        

    def Update(self):
        running=True
        while running:
            for event in py.event.get():
                if event.type==py.QUIT:
                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()
            self._screen.fill((158,158,158))
            code=random.randint(0,9)
            for i in range (0,6):
                 code=code+random.randint(0,3)
            code=str(code)
            box=self.createRect(10, 10, 500, 500)
            self.drawRect(255,box,self._screen)
            self.draw_text(code,50,50, 50, (0,0,0))

            back=self.createRect(120,440,80,40)
            self.drawRect((0,0,0),back,self._screen)
            self.draw_textline("Back", 125 , 445, 42, (255, 255, 255))
            

            location=self.getmouse()
            for event in py.event.get():
                if event.type==py.MOUSEBUTTONDOWN:
                            if back.collidepoint(location):
                                return
                            

            py.display.flip()
            self._clock.tick(30)
    py.quit()



decoder().Update()
""" class decoding:
    def __init__(self):
        code=random.randint(0,3)
    def displaycode(self,code):
        code=str(code)
        box=self.createRect(self,10, 10, 500, 500)
        self.drawRect(255,255,255,box)
        self.draw_text(code,50,50, 50, (0,0,0)) """


    
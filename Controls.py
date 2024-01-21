import pygame as py
from Screens import Screens
import sys
#from Menu import Menuscreen

class controls(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)


    def Update(self):
        py.init()
        running=True
        while running:
            for event in py.event.get():
                if event.type==py.QUIT:
                        start_game=False
                        #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                        sys.exit()
                location=self.getmouse()
                if event.type==py.MOUSEBUTTONDOWN:
                        if back.collidepoint(location):
                             sys.exit()
                            
            self._screen.fill((158,158,158))

            background=self.createRect(30,80,450,400)
            self.drawRect((255, 255, 187),background,self._screen)
            back=self.createRect(40,425,80,40)
            self.drawRect((0,0,0),back,self._screen)
            self.draw_textline("Back", 45 , 430, 42, (255, 255, 255))
            
            self.draw_textline("Controls", 120 , 20, 80, (170, 0, 29))#x,y,size,colour
            self.draw_textline('''
Use WASD to move around.\n
Q is used to interact with objects\n
R is used to access the inventory\n
Use your curser to move the camera and to \n
select items in the inventory into your hand.\n
You can press E to return the item to the inventory\n
or use it to interact with items such as locks if nearby.'''
                           , 40 , 100, 20, (0,0,0))

            py.display.flip()
            self._clock.tick(30)
    py.quit()



#controls().Update()
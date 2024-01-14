import pygame as py
from Screens import Screens

class controls(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)
        self._nextbutton={"Next":{"Button":self.createRect(160,130,160,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Next",
                               "Colour":(0,0,0),
                               "Textcolour":(255,255,255),
                               "Textcoords":(170,130),
                               "Textsize":(30)}}

    def Update(self):
        running=True
        while running:
            self._screen.fill((158, 158, 158))
            self.draw_text("Instructions", 10 , 20, 80, (170, 0, 29))#x,y,size,colour
            self.draw_text('''
                           Use WASD to move around.
                        Q is used to interact with objects
                        R is used to access the inventory
                        Use your curser to move the camera and to select items in the inventory into your hand
                        You can press E to return the item to the inventory or use it to interact with items such as locks if near the player'''
                           , 10 , 20, 15, (170, 0, 29))

            py.display.flip()
            self._clock.tick(30)
    py.quit()



#controls().Update()
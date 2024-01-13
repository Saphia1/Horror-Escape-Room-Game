import pygame as py
from Screens import Screens

class Instructions(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)
        self._nextbutton={"Next":{"Button":self.createRect(160,130,160,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Next",
                               "Colour":(0,0,0),
                               "Textcolour":(255,255,255),
                               "Textcoords":(170,130),
                               "Textsize":(30)}}

    def Updateinstructions(self):
        running=True
        while running:
            self._screen.fill((158, 158, 158))
            self.draw_text("Instructions", 10 , 20, 80, (170, 0, 29))#x,y,size,colour
            self.draw_text("You've been woken up in a mysterious place, the name Sakshi runs through your mind like a wild animal feasting for prey", 10 , 20, 15, (170, 0, 29))
        py.display.flip()
        self._clock.tick(30)
    py.quit()



Instructions().Updateinstructions()
"""         WIDTH=500
        HEIGHT=500
        self._screen=py.display.set_mode([WIDTH,HEIGHT]) 
"""
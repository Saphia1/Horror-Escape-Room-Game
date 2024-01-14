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

    def Update(self):
        running=True
        while running:
            self._screen.fill((158, 158, 158))
            self.draw_text("Instructions", 10 , 20, 80, (170, 0, 29))#x,y,size,colour
            self.draw_text('''
                           You've been woken up in a mysterious place, the name Sakshi
                            runs through your mind like a wild animal feasting for prey'''
                           , 10 , 20, 15, (170, 0, 29))
            self.draw_text('''
                           You are a detective sent to investigate a haunted house murder, however once entering the house you are knocked unconscious and wake up in a room alone… or so you thought.
The room is locked but you hear footprints outside.
By completing tasks and puzzles find a way out before its too late. Do not get caught more than three times!
Interact with the map and objects to find clues and secrets.
Feel free to run but remember! As you sprint your energy level decreases and needs to regenerate before you can run again!
Good luck!
'''
                           , 10 , 20, 15, (170, 0, 29))
            self.draw_text('''
                           Use the arrow keys to move around, E to interact with objects, Q to use objects and 
                           DON'T GET CAUGHT!'''
                           , 10 , 20, 15, (170, 0, 29))
            py.display.flip()
            self._clock.tick(30)
    py.quit()



#Instructions().Update()
"""         WIDTH=500
        HEIGHT=500
        self._screen=py.display.set_mode([WIDTH,HEIGHT]) 
"""
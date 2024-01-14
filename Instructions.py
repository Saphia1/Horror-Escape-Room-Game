import pygame as py
from Screens import Screens
import sys

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
            for event in py.event.get():
                if event.type==py.QUIT:
                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()
            self._screen.fill((158,158,158))

            background=self.createRect(30,80,450,400)
            self.drawRect((0,0,0),background,self._screen)
            self.draw_textline("Instructions", 75 , 20, 80, (170, 0, 29))#x,y,size,colour
            self.draw_textline('''
You wake in a mysterious place, the name Sakshi\n
runs through your mind You are a detective sent to\n
investigate a murder however once entering the house \n
you are knocked unconscious and left\n
alone… or so you thought.\n
The room is locked but you hear footprints outside.\n
By completing tasks and puzzles find a way out!\n 
Do not get caught more than three times!\n
Interact with the map and objects to find clues.\n
Good luck!'''
                           , 40 , 90, 20, (170, 0, 29))

            py.display.flip()
            self._clock.tick(30)
    py.quit()



Instructions().Update()#testing purposes only
"""         WIDTH=500
        HEIGHT=500
        self._screen=py.display.set_mode([WIDTH,HEIGHT]) 
"""
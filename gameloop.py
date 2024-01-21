from player import Player
import pygame as py
import sys
from Screens import Screens
from Grid import Grid


class maingame(Screens):
    def __init__(self, bgcolour=(158,158,158)):
        super().__init__()
        self._bgcolour=bgcolour
        

    
    def run_loop(self):
        """
        Subroutine to run the main loop of the game
        
        """
        py.init()
        start_game=True
        grid=Grid(50,50)
        grid.gencells()
        #p1=Player(100,400,20,20,3)

        #ensures game can be quit, draws the screen.
        while start_game==True:
            self._screen.fill((158, 158, 158))
            #if x in corner is clicked, the game stops running
            for event in py.event.get():
                if event.type==py.QUIT:
                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()


            #py.draw.circle(surface(you can have screen, smaller surfaces for text, having multiple different screens),colour E.g.(0,0,0),the coordinates of the centre to place it(250,250),radius75)
            py.display.flip()
            self._clock.tick(30)
        py.quit()

"""         keys=py.key.get_pressed()
            rect=py.Rect(300,200,50,50)
            py.draw.rect(self._screen,(255,0,0),rect)
            p1.movement(keys,rect)
            p1.draw(self._screen) 
            
"""
       


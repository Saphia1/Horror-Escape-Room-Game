from player import Player
import pygame as py
import sys
from Screens import Screens
from Grid import Grid
from enemy import Enemy
from Tasks import Tasks
from riddletask import Riddle
from decodetask import Decodetask
#generate all spawn cells then use for lopp to go through eahc one, then check if equal to current cell, then run that task

class maingame(Screens):
    def __init__(self, bgcolour=(158,158,158)):
        super().__init__()
        self._bgcolour=bgcolour
        self._todo=5
        self._visitedriddle=False
        self._visiteddecode=False
        
        

    
    def run_loop(self):
        """
        Subroutine to run the main loop of the game
        
        """
        py.init()
        start_game=True
        grid=Grid(20,20)
        grid.gencells()
        cells=grid.getcells()
        p1=Player(22,22,10,10,6)
        enemy=Enemy(102,45,10,10,grid.getcellsize())
        detected=False

        #ensures game can be quit, draws the screen.
        while start_game==True:

            self._screen.fill((158, 158, 158))
            #if x in corner is clicked, the game stops running
            for event in py.event.get():
                if event.type==py.QUIT:

                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()

            grid.buildgrid()
            
            keys=py.key.get_pressed()
           # py.draw.rect(self._screen,(255,0,0),rect)

            p1.movement(keys,cells,enemy.getrect())
            p1.draw(self._screen)
            
            enemy.movement(cells,detected,p1.getrect())
      
            enemy.draw(self._screen)

            for taskcell in Tasks.getspawncells():

                if p1.incell(grid).getcoords()==taskcell.getcoords():
                    if self._visitedriddle==False:
                        Riddle(self._todo).update()
                    elif self._visiteddecode==False:
                        Decodetask(self._todo).update()
                
            

            #py.draw.circle(surface(you can have screen, smaller surfaces for text, having multiple different screens),colour E.g.(0,0,0),the coordinates of the centre to place it(250,250),radius75)
            py.display.flip()
            self._clock.tick(10)
        py.quit()

"""         keys=py.key.get_pressed()
            rect=py.Rect(300,200,50,50)
            py.draw.rect(self._screen,(255,0,0),rect)
            p1.movement(keys,rect)
            p1.draw(self._screen) 
            
"""
       


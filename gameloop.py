from player import Player
import pygame as py
import sys
from Screens import Screens
from Grid import Grid
from enemy import Enemy
from Tasks import Tasks
from riddletask import Riddle
from decodetask import Decodetask
from TorF import TorF
from Cell import Cell
from PygameUtil import PygameUtil
#generate all spawn cells then use for lopp to go through eahc one, then check if equal to current cell, then run that task

class maingame(Screens):
    def __init__(self, bgcolour=(158,158,158)):
        super().__init__()
        self._bgcolour=bgcolour
        self._todo=3
        self._visitedriddle=False
        self._visiteddecode=False
        self._visitedTorF=False
        
        
        

    
    def run_loop(self):
        """
        Subroutine to run the main loop of the game
        
        """
        py.init()
        start_game=True
        gridobject=Grid(20,20)
        gridobject.gencells()
        cells=gridobject.getcells()
        gridlist=gridobject.getgrid()
        p1=Player(22,22,10,10,10)
        enemy=Enemy(102,45,10,10,gridobject.getcellsize())
        detected=False
        taskcells=Tasks().choosetaskcell(gridlist)
        #spawncells=Tasks().getspawncells()
        

        #ensures game can be quit, draws the screen.
        while start_game==True:

            self._screen.fill((158, 158, 158))
            #if x in corner is clicked, the game stops running
            for event in py.event.get():
                if event.type==py.QUIT:

                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()
            Tasks().colourcells(taskcells)
            gridobject.buildgrid()
            
            keys=py.key.get_pressed()
           # py.draw.rect(self._screen,(255,0,0),rect)

            p1.movement(keys,cells,enemy.getrect())
            p1.draw(self._screen)
            
            enemy.movement(cells,detected,p1.getrect())
      
            enemy.draw(self._screen)
            
            
            
            
            

   

            
            for i in range (0,len(taskcells)):#0
                if p1.incell(gridlist).getcoords()==taskcells[i].getcoords():
                    
                    if self._todo==3:
                        print(self._todo)
                        self._todo=Riddle(self._todo).update()
                        taskcells=taskcells.remove(taskcells[i])
                        
                    elif self._todo==2:
                       self._todo= Decodetask(self._todo).update()
                     
                    elif self._todo==1:
                       self._todo=TorF(self._todo).update()
                    
                
            

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
       


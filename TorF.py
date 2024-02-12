import pygame as py
from PygameUtil import PygameUtil
from Screens import Screens
import random
import sys
from Tasks import Tasks
class TorF(Screens):#inheritence, stating class to inherit from
    def __init__(self,todo,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)
        self._todo=todo
        self.__rando=Tasks().rando()
        self.__fact=Tasks().genfact(self.__rando)
        
        

    def update(self):
        running=True
        while running:
            for event in py.event.get():
                if event.type==py.QUIT:
                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()
            self._screen.fill((158,158,158))
            
            """             box=self.createRect(10, 10, 500, 500)
            self.drawRect(255,box,self._screen) """

            self.draw_textline(self.__fact,50,50, 30, (255,255,255))

            if self.__rando==0:
                ans=False
                
            elif self.__rando==1:
                 ans=False
            elif self.__rando==2:
                 ans=False
            elif self.__rando==3:
                 ans=True
            
            
                 
                 

            back=self.createRect(15,450,80,40)
            self.drawRect((0,0,0),back,self._screen)
            self.draw_textline("Back", 20 , 455, 42, (255, 255, 255))
            #to make more efficient you could make this into a for loop
            '''answer option 1'''
            answer1=self.createRect(50,300,400,75)
            self.drawRect((0,0,0),answer1,self._screen)
            self.draw_textline("True", 150 , 305, 100, (255, 255, 255))
            
            '''answer option 2'''
            answer2=self.createRect(50,200,400,75)
            self.drawRect((0,0,0),answer2,self._screen)
            self.draw_textline("False", 150 , 205, 100, (255, 255, 255))
            
            

            
       


            location= self.getmouse

            location = self.getmouse()
            for event in py.event.get():
                if event.type == py.MOUSEBUTTONDOWN:
                    if back.collidepoint(location):
                                
                                return (self._todo)
                    elif (answer2.collidepoint(location) and ans == False) or (answer1.collidepoint(location) and ans == True):
                        self.draw_textline("CORRECT", 125 , 445, 42, (255, 0, 0))
                        self._todo = self._todo - 1
                        
                        return (self._todo)
                    else:
                        self.draw_textline("INCORRECT", 125 , 445, 42, (255, 0, 0))
                                 
            
                            

            py.display.flip()
            self._clock.tick(10)
    py.quit()



#TorF(3).update()



    

import pygame as py
from PygameUtil import PygameUtil
from Screens import Screens
import random
import sys
from Tasks import Tasks
class Riddle(Screens):#inheritence, stating class to inherit from
    def __init__(self,todo,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)
        self._todo=todo
        self.__rando=Tasks().rando()
        self.__riddle=Tasks().genriddle(self.__rando)
        
        

    def update(self):
        running=True
        while running:
            for event in py.event.get():
                if event.type==py.QUIT:
                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()
            self._screen.fill((158,158,158))
            
            box=self.createRect(10, 10, 500, 500)
            self.drawRect(255,box,self._screen)

            self.draw_textline(self.__riddle,50,50, 30, (255,255,255))

            if self.__rando==0:
                answers=Tasks().birds()
                ans=0
                
            elif self.__rando==1:
                 answers=Tasks().fear()
                 ans=3
            elif self.__rando==2:
                 answers=Tasks().cereal()
                 ans=3
            elif self.__rando==3:
                 answers=Tasks().echo()
                 ans=3
            
            
                 
                 

            back=self.createRect(15,450,80,40)
            self.drawRect((0,0,0),back,self._screen)
            self.draw_textline("Back", 20 , 455, 42, (255, 255, 255))
            #to make more efficient you could make this into a for loop
            '''answer option 1'''
            answer1=self.createRect(50,300,150,75)
            self.drawRect((0,0,0),answer1,self._screen)
            self.draw_textline(answers[0], 55 , 305, 42, (255, 255, 255))
            
            '''answer option 2'''
            answer2=self.createRect(250,200,150,75)
            self.drawRect((0,0,0),answer2,self._screen)
            self.draw_textline(answers[1], 255 , 205, 42, (255, 255, 255))
            
            '''answer option 3'''
            answer3=self.createRect(50,200,150,75)
            self.drawRect((0,0,0),answer3,self._screen)
            self.draw_textline(answers[2], 55 , 205, 42, (255, 255, 255))

            '''correct answer(reduced replaybility though because eventually will realise which is the correct answer)'''
            correct=self.createRect(250,300,150,75)
            self.drawRect((0,0,0),correct,self._screen)
            self.draw_textline(answers[3], 255 , 305, 42, (255, 255, 255))
            

            
       


            

            location=self.getmouse()
            for event in py.event.get():
                if event.type==py.MOUSEBUTTONDOWN:
                            if back.collidepoint(location):
                                completed=False
                                return (self._todo,completed)
                            elif correct.collidepoint(location) and ans==3  or answer1.collidepoint(location) and ans==0 or answer2.collidepoint(location) and ans==1 or answer3.collidepoint(location) and ans==2:
                                 self.draw_textline("CORRECT", 125 , 445, 42, (255, 0, 0))
                                 self._todo=self._todo-1
                                 completed=True
                                 return (self._todo,completed)
                            else:
                                 self.draw_textline("INCORRECT", 125 , 445, 42, (255, 0, 0))
                                 
                                 
            
                            

            py.display.flip()
            self._clock.tick(3)
    py.quit()



#Riddle(3).update()



    
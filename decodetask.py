import pygame as py
from PygameUtil import PygameUtil
from Screens import Screens
import random
import sys
from Tasks import Tasks
class Decodetask(Screens):#inheritence, stating class to inherit from
    def __init__(self,todo,bgcolour=(158, 158, 158)):
        super().__init__(bgcolour)
        self._todo=todo
        self._code=Tasks().codegenerator()
        self.__ans1=Tasks().answergenerator()
        self.__ans2=Tasks().answergenerator()
        self.__ans3=Tasks().answergenerator()

        
        

    def update(self):
        running=True
        while running:

            self._screen.fill(self._bgcolour)
            
            """             box=self.createRect(10, 10, 500, 500)
            self.drawRect(255,box,self._screen) """
            self.draw_text(self._code,170,100, 50, (255,255,255))
            self.draw_text("Add the digits",120,50, 50, (255,255,255))

            back=self.createRect(15,450,80,40)
            self.drawRect((0,0,0),back,self._screen)
            self.draw_textline("Back", 20 , 455, 42, (255, 255, 255))
            #to make more efficient you could make this into a for loop
            '''answer option 1'''
            answer1=self.createRect(50,300,150,75)
            self.drawRect((0,0,0),answer1,self._screen)
            self.draw_textline(self.__ans1, 55 , 305, 42, (255, 255, 255))
            
            '''answer option 2'''
            answer2=self.createRect(250,200,150,75)
            self.drawRect((0,0,0),answer2,self._screen)
            self.draw_textline(self.__ans2, 255 , 205, 42, (255, 255, 255))
            
            '''answer option 3'''
            answer3=self.createRect(50,200,150,75)
            self.drawRect((0,0,0),answer3,self._screen)
            self.draw_textline(self.__ans3, 55 , 205, 42, (255, 255, 255))

            '''correct answer(reduced replaybility though because eventually will realise which is the correct answer)'''
            correct=self.createRect(250,300,150,75)
            self.drawRect((0,0,0),correct,self._screen)
            self.draw_textline((Tasks().codecalc(self._code)), 255 , 305, 42, (255, 255, 255))

            
       


            

            location=self.getmouse()
            for event in py.event.get():
                if event.type==py.MOUSEBUTTONDOWN:
                            if back.collidepoint(location):
                                
                                return (self._todo)
                            elif answer1.collidepoint(location) or answer2.collidepoint(location) or answer3.collidepoint(location):
                                 self.draw_textline("INCORRECT", 125 , 445, 42, (255, 0, 0))
                            elif correct.collidepoint(location):
                                 self.draw_textline("CORRECT", 125 , 445, 42, (255, 0, 0))
                                 self._todo=self._todo-1
                                 
                                 return (self._todo)
                if event.type==py.QUIT:
                    start_game=False
                    #py.quit()#this causes to stop being initialised, solution: put system.exit instead
                    sys.exit()
                                 
                                 
            
                            

            py.display.flip()
            self._clock.tick(10)
    py.quit()



#Decodetask(5).update()



    
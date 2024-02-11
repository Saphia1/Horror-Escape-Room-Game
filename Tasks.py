import pygame as py
import random

class Tasks():
    
    def __init__(self):
          number=random.randint(0,3)
          self.__number=number
          self.__spawncell=[]
     
     
          

    def choosetaskcell(self,grid):
         count=0
         while count != 3:
              row=random.choice(grid)
              cell=random.choice(row)
              if cell not in self.__spawncell:
               self.__spawncell.append(cell)
               count=count+1

     
    def getspawncells(self):
         return self.__spawncell
                 
        
    def codegenerator(self):#creates a random code string
        code=""
        for i in range (0,6):
                 code=code+str(random.randint(0,9))
                 
                 
        code=str(code)
        return code
    
    def answergenerator(self):
        code=""
        for i in range (0,2):
                 code=code+str(random.randint(0,9))
                 
                 
        code=str(code)
        return code
         
    
    def codecalc(self,code):
        codeint=0
        for i in range (0,(len(code))):
            numb=int(code[i])
            codeint=codeint+numb
        codeint=str(codeint)
        return codeint
    
    def rando(self):
         riddle=["There are ten birds sitting on a fence. You shoot one. How many are left?","I watch you sleep, I haunt you by day. You stare at me and saw nothing, but darkness. What am I?","What is a cereal's worst fear?","I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? "]
         rando=int(random.randint(0,2))
         return rando
    
    def genriddle(self,rando):
         riddle=['''There are ten birds \n
sitting on a fence. You shoot one.\n
How many are left?''',
                 '''I watch you sleep, I haunt you by day.\n
You stare at me and saw nothing,\n 
but darkness. What am I?''',
                 '''What does a cereal\n
fear?''',
                 '''I speak without \n
a mouth and hear without ears.\n
I have no body,but I come alive \n
with wind. What am I? ''']
         chosen=riddle[rando]
         return chosen

    def birds(self):
         answers=["None.","4","9","10"]
         return answers

    def fear(self):
         answers=["Fear","Sakshi","Moon","Shadow"]
         return answers
    
    def cereal(self):
         answers=["Milk","Spoon",'''Mouth''',"Serial Killer"]
         return answers
    def echo(self):
         answers=["Phone","Speaker","Bell","An echo"]
         return answers
    
    
   
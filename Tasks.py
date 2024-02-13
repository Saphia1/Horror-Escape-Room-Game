import pygame as py
import random
from PygameUtil import PygameUtil

class Tasks(PygameUtil):
    
    
    def __init__(self):
          super().__init__()
          number=random.randint(0,3)
          self.__number=number
          self.__spawncell=[]
          self.__count=0
          
     
     
          

    def choosetaskcell(self,grid):
         gridlength=len(grid)
         while self.__count < 3:
              print("in loop 3")
              print(self.__count)
              randgrid=random.randint(0,gridlength-1)
              row=grid[randgrid]
              cell=random.choice(row)
              if cell not in self.__spawncell:
                    print("not in spawncell")
                    self.__spawncell.append(cell)
                    print (self.__spawncell)
                    self.__count=self.__count+1
         return self.__spawncell
     
    def colourcells(self,taskcells):
          taskcells=list(taskcells)
          for i in range (0,(len(taskcells))):
                width=taskcells[i].getwidth()
                height=taskcells[i].getheight()
                x,y=taskcells[i].getcoords()
                colouredcell=self.createRect(x,y,width,height)
                self.drawRect((0,240,0),colouredcell)
                
         

     
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
     rando=int(random.randint(0,3))
  
     return rando
    
    def genriddle(self,rando):
         riddle=['There are ten birds \n sitting on a fence. You shoot one.\n How many are left?', 
                 'I watch you sleep, I haunt you by day.\n You stare at me and saw nothing,\n  but darkness. What am I?',
                 'What does a cereal\fear?',
                 'I speak without \n a mouth and hear without ears.\n I have no body,but I come alive \n with wind. What am I? ']
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
    
    def genfact(self,rando):
         fact=["Sakshis middle name is Jon", "Saskshis fave colour is green", "Sakshis fave friend is Haritha", '''       Sakshis fave roblox game\n
          is dress to impress''']
         chosen=fact[rando]
         return chosen
    
    
   
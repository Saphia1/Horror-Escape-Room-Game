import pygame as py
from player import Player
import random

class Enemy(Player):
    #setting up attributes being used
    def __init__(self,x,y,w,h,speed):
        super().__init__(x,y,w,h,speed)
        self._colour=(200,45,47)
        self.__taskdoing=False
     
        self._speed=speed#this is a tuple of the x speed and y speed (see grid)
        self.__starttime=py.time.get_ticks()//1000
        
    #the movement method of my player
    def movement(self,grid,detected,player=None):#if dont pass in obj, then automatically pass in as none
        newenemy=self._rect.copy() #copies position of player
        
      
        
        if self.__taskdoing==False:
            


                
                cell=self.incell(grid)
                movement=[]
                walls=cell.getwalls()
                if not walls["left"]:
                    movement.append((-self._speed[0],0))
                if not walls["right"]:
                    movement.append((self._speed[0],0))
                if not walls["top"]:
                    movement.append((0,-self._speed[1]))
                if not walls["bottom"]:
                    movement.append((0,self._speed[1]))
                    #look into clock to slow down enemy movement or have own counter that counts down numver of frames till can move again
                currenttime=py.time.get_ticks()//1000 
                if (currenttime-self.__starttime)%200>0:
                    newenemy.move_ip(random.choice(movement))
                
                
               

                if newenemy.left<0:
                    newenemy.left=0
                if newenemy.top<=0:
                    newenemy.top=0
                if newenemy.right>self._WIDTH:
                    newenemy.right=self._WIDTH
                if newenemy.bottom>self._HEIGHT:
                    newenemy.bottom=self._HEIGHT
        if player and newenemy.colliderect(player):
            return
        
        if self.wallcollision(grid,newenemy):#wall collision, if its true then DONT update location
            return
        
        
        self._rect=newenemy







   


py.quit() 

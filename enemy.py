import pygame as py
from player import Player
import random

class Enemy(Player):
    #setting up attributes being used
    def __init__(self,x,y,w,h,speed):
        super().__init__(x,y,w,h,speed)
        self._colour=(200,45,47)
        
    #the movement method of my player
    def movement(self,grid,detected,player=None):#if dont pass in obj, then automatically pass in as none
        newenemy=self._rect.copy() #copies position of player
      
        
        if detected ==False:
                
                movement=[(0,-self._speed),(0,self._speed),(self._speed,0),(-self._speed,0)]
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

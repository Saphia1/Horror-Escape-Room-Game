import pygame as py
from player import Player
import random

class Enemy(Player):
    #setting up attributes being used
    def __init__(self,x,y,w,h,speed):
        self.__speed=speed
        self.__rect=py.Rect(x,y,w,h)
        self.__colour=(129,45,247)
        super().__init__(x,y,w,h,speed)
    #the movement method of my player
    def movement(self,grid,detected,player=None):#if dont pass in obj, then automatically pass in as none
        newenemy=self.__rect.copy() #copies position of player
        #basic logic: if the key is pressed move in that direction
        if detected ==False:
                newenemy.move_ip(0,random.randint(0,100))
                newenemy.move_ip(0,random.randint(0,100))
                newenemy.move_ip(0,random.randint(0,100))
                newenemy.move_ip(0,random.randint(0,100))
                #setting up boundries for player leaving screen
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
        
        enemy=newenemy


py.quit() 

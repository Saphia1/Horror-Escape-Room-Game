import pygame as py
from PygameUtil import PygameUtil

class Player(PygameUtil):
    #setting up attributes being used
    def __init__(self,x,y,w,h,speed):
        self.__speed=speed
        self.__rect=py.Rect(x,y,w,h)
        self.__colour=(129,45,247)
        super().__init__()
    #the movement method of my player
    def movement(self,keys,obj=None):#if dont pass in obj, then automatically pass in as none
        newplayer=self.__rect.copy() #copies position of player
        #basic logic: if the key is pressed move in that direction
        if keys[py.K_UP]:
            newplayer.move_ip(0,-self.__speed)
        if keys[py.K_DOWN]:
            newplayer.move_ip(0,self.__speed)
        if keys[py.K_LEFT]:
            newplayer.move_ip(-self.__speed,0)
        if keys[py.K_RIGHT]:
            newplayer.move_ip(self.__speed,0)
        #setting up boundries for player leaving screen
        if newplayer.left<0:
            newplayer.left=0
        if newplayer.top<=0:
            newplayer.top=0
        if newplayer.right>self._WIDTH:
            newplayer.right=self._WIDTH
        if newplayer.bottom>self._HEIGHT:
            newplayer.bottom=self._HEIGHT
            #function that provides true and false for if two rectangles collide
        if obj and newplayer.colliderect(obj):
            return #if rectangles collide then dont make any changes (dont update clock so they dotn move)
        
        self.__rect=newplayer#making actual player equal to the location of copy so it does update as NOT collided

        
        
#draws the player
    def draw(self,surf):
        py.draw.rect(surf,self.__colour,self.__rect)

py.quit()

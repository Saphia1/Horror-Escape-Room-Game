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
    def movement(self,keys,grid,obj=None):#if dont pass in obj, then automatically pass in as none
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
        if self.wallcollision(grid,newplayer):#wall collision, if its true then DONT update location

            return
        
        self.__rect=newplayer#making actual player equal to the location of copy so it does update as NOT collided
        
    def wallcollision(self, grid, rect):#method to detect if player hits wall
        for row in grid:#check for each cell in the whole grid
            for cell in row:
                cellwall=cell.getwalls()#get the walls
                celledges=cell.getwalledge()#find the edges for each wall
                for key in cellwall.keys():#now for every edge 
                    if cellwall[key]:#if the wall of the cell matches the edge
                        if rect.clipline(celledges[key]):#then return wall collision as true (go back to the if statement in collisions)
                            return True
        return False
    def getrect(self):
        return self.__rect
    
    

        
        



        
        
#draws the player
    def draw(self,surf):
        py.draw.rect(surf,self.__colour,self.__rect)

py.quit()

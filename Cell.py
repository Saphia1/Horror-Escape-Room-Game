
from PygameUtil import PygameUtil as py #how to import from other files
from random import choice
class Cell:
    def __init__(self,x,y,width=20,height=20):#x and y of bottom left coordinates#
        self.__x=x
        self.__y=y
        self._WIDTH=width
        self.__height=height
        self.__walls={"top":True, "right":True, "left":True, "bottom":True}#dictionary to allow for room walls to be removed by having a record of each cell
        self.__neighbours=[]

    def getcoords (self):#by passing in self, we pass in all the __init__ attributes
        return self.__x, self.__y
    
    def getwidth (self):
        return self._WIDTH
    
    def getheight (self):
        return self.__height
    
    def getwalls (self):
        return self.__walls

    def getneighbours(self):
        return self.__neighbours

    def resetNeighbours(self):
        self.__neighbours = []
    
    def addneighbour(self, neighbour):
        self.__neighbours.append(neighbour)
    
    def choosecell(self):
        return choice(self.__neighbours)
    
    def removewall(self, neighbour):
        x,y=neighbour.getcoords()
        change_in_x=self.__x-x
        change_in_y=self.__y-y
        if change_in_y == self.__height:#if we are moving to cell above
            self.__walls["top"]=False
            neighbour.removeindividualwall("bottom")
        if change_in_y == -self.__height:
            self.__walls["bottom"]=False
            neighbour.removeindividualwall("top")
        if change_in_x == self._WIDTH:#if we are moving to cell below
            self.__walls["left"]=False
            neighbour.removeindividualwall("right")
        if change_in_x == -self._WIDTH:
            self.__walls["right"]=False
            neighbour.removeindividualwall("left")
        

    
    def removeindividualwall(self, wall):
        self.__walls[wall]=False



""" from PygameUtil import PygameUtil as py #how to import from other files
from random import choice
class Cell:
    def __init__(self,x,y,width=20,height=20):#x and y of bottom left coordinates#
        self.__x=x
        self.__y=y
        self._WIDTH=width
        self.__height=height
        self.__walls={"top":True, "right":True, "left":True, "bottom":True}#dictionary to allow for room walls to be removed by having a record of each cell
        self.__neighbours=[]

    def getcoords (self):#by passing in self, we pass in all the __init__ attributes
        return self.__x, self.__y
    
    def getwidth (self):
        return self._WIDTH
    
    def getheight (self):
        return self.__height
    
    def getwalls (self):
        return self.__walls

    def getneighbours(self):
        return self.__neighbours
    
    def addneighbour(self, neighbour):
        self.__neighbours.append(neighbour)
    
    def choosecell(self):
        return choice(self.__neighbours)
    
    def removewall(self, neighbour):
        x,y=neighbour.getcoords()
        change_in_x=self.__x-x
        change_in_y=self.__y-y
        if change_in_y == self.__height:#if we are moving to cell above
            self.__walls["top"]=False
            neighbour.removeindividualwall("bottom")
        if change_in_y == -self.__height:
            self.__walls["bottom"]=False
            neighbour.removeindividualwall("top")
        if change_in_x == self._WIDTH:#if we are moving to cell below
            self.__walls["left"]=False
            neighbour.removeindividualwall("right")
        if change_in_x == -self._WIDTH:
            self.__walls["right"]=False
            neighbour.removeindividualwall("left")
        

    
    def removeindividualwall(self, wall):
        self.__walls[wall]=False
             """
        
        
    
    

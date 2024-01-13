""" from PygameUtil import PygameUtil as py #how to import from other files
class Cell:
    def __init__(self,x,y,width,height):#x and y of bottom left coordinates#
        self.__x=x
        self.__y=y
        self._WIDTH=width
        self._screen=height
        self.__walls={"top":True, "right":True, "left":True, "bottom":True}#dictionary to allow for room walls to be removed by having a record of each cell

    def getcoords (self):#by passing in self, we pass in all the __init__ attributes
        return self.__x, self.__y
    
    def getwidth (self):
        return self._WIDTH
    
    def getheight (self):
        return self._screen

    
    
 """
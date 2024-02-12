import pygame  as py

class PygameUtil:#central class in which everything inherits from

    def __init__(self):
        #basic set up
        py.init()#initialises pygame so i can use library
        self._WIDTH=500
        self._HEIGHT=500
        self._screen=py.display.set_mode([self._WIDTH,self._HEIGHT])
        self._clock=py.time.Clock()#just protected as used throughout 
        
    def createRect(self, x, y, width, height):#creates object for rectangles
        return py.Rect(x,y,width,height)
    
    def drawRect(self,colour,rect,surface=None):#draws rectangle just created
        if surface==None:
            surface=self._screen
         #(if nothing passed in as surface, set it to the screen, if not use the surface give.)
        py.draw.rect(surface,colour,rect)

    def drawline(self,colour,start_pos,end_pos,surface=None):#lines for maze generation to draw grids
        surface=self._screen if None else surface
        py.draw.line(surface,colour,start_pos,end_pos)
        
    def getmouse(self):
        return py.mouse.get_pos()
        
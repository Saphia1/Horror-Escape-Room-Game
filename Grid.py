
from Cell import Cell
from PygameUtil import PygameUtil
class Grid(PygameUtil):
    def __init__ (self,width,height):
        super().__init__()#brackets are what calls it
        self.__width=width#how many cells across
        self.__height=height#how many cells up
        self.__grid=[]#list of all cells
        self.__start_pos=(20,20)#where the generator starts
    def gencells(self):#method to generate the cells within our list
        for r in range(0,self.__height):#dont wnat to start at 0
            self.__grid.append([])#adds empty list so we can have a 2 dimensional array, so makes the collumn for all cellls we will add to this y coordinate. (see notes for more detail)
            for i in range(0, self.__width):
                cell=Cell(self.__start_pos[0]*(i+1),self.__start_pos[1]*(r+1))#setting up the x and y coords to move each time for the next cell #WONT WORK WITH CELLS THAT ARE NOT 20 PIXELS AS ASSUMES EACH CELL A SQUARE
                self.__grid[r].append(cell)
    def buildgrid(self):#method to build the grid, will draw every row and cell in array
        for row in self.__grid:#(row is r it is doing the collumns)
            for cell in row:
                x,y=cell.getcoords()
                w=cell.getwidth()
                h=cell.getheight()
                walls=cell.getwalls()
                if walls["top"]:
                    self.drawline((255,255,255),(x,y),(x+w,y))#end point is gained by x+w,y (add the picture from notes in annotations)
                    






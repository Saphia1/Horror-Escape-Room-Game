
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
        for i in range(0,self.__height):#dont wnat to start at 0
            self.__grid.append([])#adds empty list so we can have a 2 dimensional array, so makes the collumn for all cellls we will add to this y coordinate. (see notes for more detail)
            for j in range(0, self.__width):
                cell=Cell(self.__start_pos[0]*(j+1),self.__start_pos[1]*(i+1))#setting up the x and y coords to move each time for the next cell #WONT WORK WITH CELLS THAT ARE NOT 20 PIXELS AS ASSUMES EACH CELL A SQUARE
                self.__grid[i].append(cell)
        self.depthfirst()
    def buildgrid(self):#method to build the grid, will draw every row and cell in array
        for row in self.__grid:#(row is r it is doing the collumns)
            for cell in row:
                x,y=cell.getcoords()#from cell
                w=cell.getwidth()
                h=cell.getheight()
                walls=cell.getwalls()
                if walls["top"]:
                    self.drawline((255,255,255),(x,y),(x+w,y))#end point is gained by x+w,y (add the picture from notes in annotations in whiteboard)
                if walls["bottom"]:
                    self.drawline((255,255,255),(x,y+h),(x+w,y+h))
                if walls["left"]:
                    self.drawline((255,255,255),(x,y),(x,y+h))
                if walls["right"]:
                    self.drawline((255,255,255),(x+w,y),(x+w,y+h))
        #grid.buildce

    def depthfirst(self):#want to start at first cell, pick random neighbour, from random neighbour, then choose random neighbour and so on. If stuck at nay point, backtrack till you can choose another neighbour.
        cell=self.__grid[0][0]#starting at first cell
        path=[]#created a stack to store the path
        visited=[]#created list of viisted cells
        while len(visited)<=(self.__width*self.__height):#while we havent visisted all the cells 
            i=(cell.getcoords[1]/self.__start_pos[1])-1
            j=(cell.getcoords[0]/self.__start_pos[0])-1
            if cell not in visited:
                visited.append(cell)
            neighbourcheck=self.findneighbours()
            if neighbourcheck:
                neighbour=cell.choosecell()#bad name, change it
                path.append(cell)
                cell.removewall(neighbour)
                self.__grid [i][j]=cell#updates all changes we made to cell
                cell=neighbour#increments to new neighbour
            else:
                path.pop()
        





    def findneighbours(self,cell,visited):
        width=cell.getwidth()
        height=cell.getheight()
        x,y=cell.getcoords()
        possibleneighbours=[(0,-height),(0,+height),(+width,0),(-width,0)]#cell above, cell below, cell right, cell left(+height is the enxt cell as its double the current) doesnt give coordiantes, just gives us what it is in the gris E.g. A1
        
        for i in possibleneighbours:#in dpeth explanation on whitevoard(rearranged an equation from gencells (the for loops to make the grid))
            neighbour_xvalue=x+i[0]#
            neighbour_yvalue=y+i[1]
            #checking if neighbours actually exist
            i=(neighbour_yvalue/self.__start_pos[1])-1
            j=(neighbour_xvalue/self.__start_pos[0])-1
            if 0<=i<=self.__height and 0<=j<=self.__width and self.__grid[i][j] not in visited and self.__grid[i][j] not in cell.getneighbours():#if cell exists and also hasnt been visited
                cell.addneighbour(self.__grid[i][j])
        
        if not cell.getneighbours():#if neighbours is empty
            return False # there are no possible neighbours (go back)
        else:
            return True
                

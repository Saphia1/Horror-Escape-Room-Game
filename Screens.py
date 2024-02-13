#represent all screens, every new screen inherit from here (the general screen) menu will actually run
#the switching from each screen.
#for example a  button being pressed is done here by menu inheriting from screens
from PygameUtil import PygameUtil
import pygame as py #incase need to use pygame DIRECTLY
#k

class Screens(PygameUtil):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(70, 72, 74)):
        super().__init__()#goes to super class (pygameutil) and use the contructor from there, inherits
        self._bgcolour=bgcolour #protected
        self._font=py.font.Font("BloodBath-Regular.otf", 24)
        self._fontcolour=(255,0,30)
    #def createfont(self,fontsize):
        #self._font=py.font.SysFont("comicsans",fontsize)

    def draw_text(self,text, x , y, fontsize, fontcolour=None):#TO DO:add font do same thing as fontcolour=None
        self._font=py.font.Font("BloodBath-Regular.otf", fontsize)#can caheng efficiency to justa dd a string placeholder variable instead incase font changes
        self._fontcolour=(255,0,30)
        if fontcolour==None:
            fontcolour=self._fontcolour
        text=self._font.render(text, True, fontcolour)
        self._screen.blit (text,(x,y))

    def display_button(self,btn,colour, surface=None):#btn= button
        if surface== None:
            surface=self._screen
            #surface=self._screen if None else surface
        py.draw.rect(surface,colour,btn)

    def get_button(self,btn):
        return(btn)
    
    def drawimg(self,img,size,coords):
        imp = py.image.load(img).convert_alpha()
        imp = py.transform.smoothscale(imp, (size)) 
        self._screen.blit(imp, (coords[0], coords[1]))

    def draw_textline(self,text, x , y, fontsize, fontcolour=None):#TO DO:add font do same thing as fontcolour=None
        self._font=py.font.Font("BloodBath-Regular.otf", fontsize)
        #self._fontcolour=(255,0,30)
        if fontcolour==None:
            fontcolour=self._fontcolour
        text=text.split("\n")#spliyts up text into a list every time it sees a \n
        for line in text:
            line=self._font.render(line, True, fontcolour)
            self._screen.blit (line,(x,y))
            linewidth,lineheight=line.get_size()
            y+=lineheight#y=y+lineheight

        

    

        

#textsize,
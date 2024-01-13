#make class inherits from screens
#have an update fucntion that will act as running loop, like while running
#want to make a running loop for each self._screen
#test by making object, class menu 
#m=menu()
#m.update()
#want that at bottom of program
import pygame as py
from Screens import Screens
from gameloop import run_loop
#from Instructions import Instructions_screen



class Menuscreen(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(70, 72, 74)):
        super().__init__(bgcolour)#goes to parent class (Screens) and use the contructor from there, inherits
        self._playbutton={"Play":{"Button":self.createRect(160,130,160,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Play Game",
                               "Colour":(0,0,0),
                               "Textcolour":(255,255,255),
                               "Textcoords":(170,130),
                               "Textsize":(30)},}
        self._instructionbutton={"Instructions":{"Button":self.createRect(145,200,190,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Instructions",
                               "Colour":(0,0,0),
                               "Textcolour":(255,255,255),
                               "Textcoords":(150,200),
                               "Textsize":(30)},}
        self._controlsbutton={"Controls":{"Button":self.createRect(170,270,140,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Controls",
                               "Colour":(0,0,0),
                               "Textcolour":(255,255,255),
                               "Textcoords":(180,270),
                               "Textsize":(30)}}
        



    
    def Update(self):#problem we encountered with inheriting from screens and pygame util for  draw.text display button and create rect as we forgot self__
        print("Accessed menu")
        running=True
        WIDTH=500
        HEIGHT=500
        self._screen=py.display.set_mode([WIDTH,HEIGHT])
        py.event.get()
        while running:
            self._screen.fill((158, 158, 158))
            self.draw_text("ATTACKSHI", 10 , 20, 80, (170, 0, 29))#x,y,size,colour
           
            #if x in corner is clicked, the game stops running
            for event in py.event.get():
                if event.type==py.QUIT:
                    running=False
            for key, value in self._playbutton.items():
                self.display_button(value["Button"],value["Colour"], self._screen)
                self.draw_text(value["Text"],value["Textcoords"][0],value["Textcoords"][1], value["Textsize"],value["Textcolour"])
                #0 says first value in coordinate pair in dictioanry, 1 for second
            for key, value in self._instructionbutton.items():
                self.display_button(value["Button"],value["Colour"], self._screen)
                self.draw_text(value["Text"],value["Textcoords"][0],value["Textcoords"][1], value["Textsize"],value["Textcolour"])
            for key, value in self._controlsbutton.items():
                self.display_button(value["Button"],value["Colour"], self._screen)
                self.draw_text(value["Text"],value["Textcoords"][0],value["Textcoords"][1], value["Textsize"],value["Textcolour"])
            self.draw_text("o", 319 , 165, 12, (170, 0, 29))
            #for event in py.event.get():
                #if event.type==py.MOUSEBUTTONDOWN:
                    #start_game ==True
                    #run_loop()
                   # for event in py.event.get():
                        #if event.type==py.QUIT:
                           # start_game=False
                           # return start_game  
            py.event.pump
            location=self.getmouse()
            for event in py.event.get():
                if location[0]>=160 and location [0]<=319 and location[1]>=130 and location [1]<=168 and event.type==py.MOUSEBUTTONDOWN:
                    run_loop()            
            #for event in py.event.get():
                #if location[0]>=160 and location [0]<=319 and location[1]>=145 and location [1]<=188 and event.type==py.MOUSEBUTTONDOWN:
                    #Instructions_screen()
            py.display.flip()
            self._clock.tick(30)
        py.quit()



Menuscreen().Update()

#,value["Textsize"]
#make class inherits from screens
#have an update fucntion that will act as running loop, like while running
#want to make a running loop for each self._screen
#test by making object, class menu 
#m=menu()
#m.update()
#want that at bottom of program
import pygame as py
from Screens import Screens
from gameloop import maingame

from Instructions import Instructions
from Controls import controls



class Menuscreen(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(70, 72, 74)):
        super().__init__(bgcolour)#goes to parent class (Screens) and use the contructor from there, inherits
        self._playbutton={"button":self.createRect(160,130,160,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Play Game",
                               "Colour":(158,158,158),
                               "Textcolour":(0, 0, 0),
                               "Textcoords":(167,140),
                               "Textsize":(39),
                               "Screen":(maingame().run_loop)}#change this to update
        
        self._instructionbutton={"button":self.createRect(145,200,190,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Instructions",
                               "Colour":(158,158,158),
                               "Textcolour":(150,20,20),
                               "Textcoords":(150,210),
                               "Textsize":(40),
                               "Screen":(Instructions().Update)}
        self._controlsbutton={"button":self.createRect(170,270,140,50),#created a dictionary for each button that specifies all of the attributes
                               "Text":"Controls",
                               "Colour":(158,158,158),
                               "Textcolour":(150,20,20),
                               "Textcoords":(175,280),
                               "Textsize":(40),
                               "Screen":(controls().Update)}
        self._buttons=[self._playbutton, self._controlsbutton, self._instructionbutton]
        

#impact,

    
    def Update(self):#problem we encountered with inheriting from screens and pygame util for  draw.text display button and create rect as we forgot self__
        running=True
        while running:
            self._screen.fill((0, 0, 0))
            self.drawimg(r"c:\Users\saphi\Pictures\Jpegs\Attackshititle.jpg",(500,300),(20,-50))
            self.drawimg(r"c:\Users\saphi\Pictures\Jpegs\blood.jpg",(220,300),(150,110))
            self.drawimg(r"c:\Users\saphi\Pictures\Jpegs\manrunning.jpg",(110,100),(30,320))
            self.drawimg(r"c:\Users\saphi\Pictures\Jpegs\hand.jpg",(100,150),(380,320))



            #self.draw_text("ATTACKSHI", 40 , 20, 100, (170, 0, 29))#x,y,size,colour
            
            #drawing the buttons via their dictionaries going through loop

            for button in self._buttons:
                  self.display_button(button["button"],button["Colour"], self._screen)
                  self.draw_text(button["Text"],button["Textcoords"][0],button["Textcoords"][1], button["Textsize"], button["Textcolour"])
                  
            


            #self.draw_text("o", 319 , 165, 12, (170, 0, 29))#used for finding coordiantes
            
            #detecting if a button is pressed, gets the mouse position


            #if the mouse is within the button box and its clicked, run the correct parts of the program
            for event in py.event.get():
                #if x in corner is clicked, the game stops running
                if event.type==py.QUIT:
                    running=False
                
                location=self.getmouse()

                if event.type==py.MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button["button"].collidepoint(location):
                            print("clicked")
                            button["Screen"]()#for running a method in a class


            #for the general display, flip it and update it
            py.display.flip()
            self._clock.tick(30)
py.quit()



Menuscreen().Update()
#
"""
elif location[0]>=160 and location [0]<=319 and location[1]>=145 and location [1]<=188 and event.type==py.MOUSEBUTTONDOWN:
                    Instructions()
                                for event in py.event.get():
                if location[0]>=160 and location [0]<=319 and location[1]>=130 and location [1]<=168 and event.type==py.MOUSEBUTTONDOWN:
                    print("clicked")
                    maingame()    
                    """
"""             for key, value in self._playbutton.items():
                self.display_button(value["button"],value["Colour"], self._screen)
                self.draw_text(value["Text"],value["Textcoords"][0],value["Textcoords"][1], value["Textsize"],value["Textcolour"])
                play=self.get_button(value["Playbutton"])
                #0 says first value in coordinate pair in dictioanry, 1 for second
            for key, value in self._instructionbutton.items():
                self.display_button(value["button"],value["Colour"], self._screen)
                self.draw_text(value["Text"],value["Textcoords"][0],value["Textcoords"][1], value["Textsize"],value["Textcolour"])
            for key, value in self._controlsbutton.items():
                self.display_button(value["button"],value["Colour"], self._screen)
                self.draw_text(value["Text"],value["Textcoords"][0],value["Textcoords"][1], value["Textsize"],value["Textcolour"]) """
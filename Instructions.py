import pygame as py
from Screens import Screens
from player import Player
from gameloop import run_loop
class Instructions_screen(Screens):#inheritence, stating class to inherit from
    def __init__(self,bgcolour=(70, 72, 74)):
        super().__init__(bgcolour)

    def Updateinstructions(self):#problem we encountered with inheriting from screens and pygame util for  draw.text display button and create rect as we forgot self__
        running=True
        WIDTH=500
        HEIGHT=500
        self._screen=py.display.set_mode([WIDTH,HEIGHT])
        while running:
            self._screen.fill((158, 158, 158))
            self.draw_text("Instructions", 10 , 20, 80, (170, 0, 29))#x,y,size,colour
            self.draw_text("You've been woken up in a mysterious place, the name Sakshi runs through your mind like a wild animal feasting for prey", 10 , 20, 15, (170, 0, 29))
        py.display.flip()
        self._clock.tick(30)
        py.quit()



Instructions_screen().Updateinstructions()
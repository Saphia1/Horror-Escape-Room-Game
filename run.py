# from ... import run_game
# from menu import menu
from gameloop import maingame
from Menu import Menuscreen as Menu
import pygame as py

#running=True
#run_loop()
#running.Menu()

#if __name__ == '__main__':#Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module

py.init()
start_game = False
while start_game == False:
    Menu()
    py.event.get()
    for event in py.event.get():
                    if event.type==py.QUIT:
                        start_game=False



    #if start_game==True:
        #run_loop()
        #for event in py.event.get():
            #if event.type==py.QUIT:
                #start_game=False
                
                
          


# # game loop

# import player ... 


# while game:
#     setup()
#     lskdjflj()


# def square(x:int):
#     return x^2

# assert square(2) == 4





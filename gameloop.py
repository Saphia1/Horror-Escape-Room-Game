from player import Player
import pygame as py
import sys



def run_loop():
    from player import Player
    import pygame as py
    import sys
    """
    Subroutine to run the main loop of the game
    
    """
    py.init()
    WIDTH=500
    HEIGHT=500
    screen=py.display.set_mode([WIDTH,HEIGHT])
    screen.fill((158, 158, 158))
    start_game=True
    p1=Player(100,400,20,20,3)
    Clock=py.time.Clock()
    #ensures game can be quit, draws the screen.
    while start_game==True:
        screen.fill((158, 158, 158))
        #if x in corner is clicked, the game stops running
        for event in py.event.get():
            if event.type==py.QUIT:
                start_game=False
                py.quit()
        keys=py.key.get_pressed()
        rect=py.Rect(300,200,50,50)
        py.draw.rect(screen,(255,0,0),rect)
        p1.movement(keys,rect)
        p1.draw(screen)
        #py.draw.circle(surface(you can have screen, smaller surfaces for text, having multiple different screens),colour E.g.(0,0,0),the coordinates of the centre to place it(250,250),radius75)
        py.display.flip()
        Clock.tick(30)
    #py.quit()
    sys.quit()


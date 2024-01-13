import pygame as py
py.init()
WIDTH=500
HEIGHT=500
screen=py.display.set_mode([WIDTH,HEIGHT])
screen.fill((158, 158, 158))

start_game=True
Clock=py.time.Clock()
#ensures game can be quit, draws the screen.
while start_game==True:
    screen.fill((158, 158, 158))
    #if x in corner is clicked, the game stops running
    for event in py.event.get():
        if event.type==py.QUIT:
            start_game=False
            py.quit()
    fonts=py.font.get_fonts()
    for i in range (0,len(fonts)):
        fonty=str(fonts[i])
        font=py.font.SysFont(fonty, 10)
        fontcolour=(255,0,30)
        text=font.render("Attackshi", True, fontcolour,)
        x=10
        y=10
        screen.blit (text,(x+100,y))



    #py.draw.circle(surface(you can have screen, smaller surfaces for text, having multiple different screens),colour E.g.(0,0,0),the coordinates of the centre to place it(250,250),radius75)
    py.display.flip()
    Clock.tick(30)
        #py.quit()



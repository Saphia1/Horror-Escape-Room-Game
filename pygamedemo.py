""" import sys
import pygame as py

from Menu import draw_text 
class player:
    #setting up attributes being used
    def __init__(self,x,y,w,h,speed):
        self.__speed=speed
        self.__rect=py.Rect(x,y,w,h)
        self.__colour=(129,45,247)
    #the movement method of my player
    def movement(self,keys,obj=None):#if dont pass in obj, then automatically pass in as none
        newplayer=self.__rect.copy() #copies position of player
        #basic logic: if the key is pressed move in that direction
        if keys[py.K_UP]:
            newplayer.move_ip(0,-self.__speed)
        if keys[py.K_DOWN]:
            newplayer.move_ip(0,self.__speed)
        if keys[py.K_LEFT]:
            newplayer.move_ip(-self.__speed,0)
        if keys[py.K_RIGHT]:
            newplayer.move_ip(self.__speed,0)
        #setting up boundries for player leaving screen
        if newplayer.left<0:
            newplayer.left=0
        if newplayer.top<=0:
            newplayer.top=0
        if newplayer.right>WIDTH:
            newplayer.right=WIDTH
        if newplayer.bottom>HEIGHT:
            newplayer.bottom=HEIGHT
            #function that provides true and false for if two rectangles collide
        if obj and newplayer.colliderect(obj):
            return #if rectangles collide then dont make any changes (dont update clock so they dotn move)
        
        self.__rect=newplayer#making actual player equal to the location of copy so it does update as NOT collided

        
        
#draws the player
    def draw(self,surf):
        py.draw.rect(surf,self.__colour,self.__rect)




###database connection
##import sqlite3
##con=sqlite3.connect("Database.db")
##cur=con.cursor()
##cur.execute("CREATE TABLE users(username,password,experience,level)")
##con.commit()#used to save changes
###database connection
##import sqlite3
##con=sqlite3.connect("Database.db")
##cur=con.cursor()
##cur.execute("CREATE TABLE users(username,password,experience,level)")
##con.commit()#used to save changes

#basic set up
py.init()
WIDTH=500
HEIGHT=500
screen=py.display.set_mode([WIDTH,HEIGHT])
running=True
p1=player(100,400,20,20,3)
Clock=py.time.Clock()
#ensures game can be quit, draws the screen.
while running:
    screen.fill((255,255,255))
    #if x in corner is clicked, the game stops running
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
    keys=py.key.get_pressed()
    rect=py.Rect(300,200,50,50)
    py.draw.rect(screen,(255,0,0),rect)
    p1.movement(keys,rect)
    p1.draw(screen)
    #py.draw.circle(surface(you can have screen, smaller surfaces for text, having multiple different screens),colour E.g.(0,0,0),the coordinates of the centre to place it(250,250),radius75)
    py.display.flip()
    Clock.tick(30)
py.quit()
sys.quit()
 """
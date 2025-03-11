import pygame as pg
import game_math as gmath
class Player:
    img = pg.image.load('Images/smolDuck.png')
    position = (50,50)
    def __init__(self,position) -> None:
        self.position= position
    def jump(self):
        x,y = self.position
        self.position= (x,y-70)
    ## Player movement
    def move(self,GROUND):
        x,y = self.position
        if y < GROUND:
            y += 5
        self.position= (x,y)
    def draw(self,screen:pg.Surface):
        dx, dy = self.img.get_size()
        offset = (-dx/2,-dy)
        screen.blit(self.img,gmath.add2(self.position,offset))
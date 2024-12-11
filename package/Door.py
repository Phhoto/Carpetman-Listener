from .Interactor import *
import pygame as pg
import os

from .everywhere import *
from .functions import *

class Door(Interactor):

    def __init__(self, x, y, locked, facing):
        self.x = x
        self.y = y
        self.locked = locked
        self.state = locked

        if facing == FACINGDOWN or facing == FACINGUP:
            self.width = 100
            self.height = 50
        else:
            self.width = 50
            self.height = 100

        self.getsprite(locked, facing, x, y)
        
        
    #also makes collider
    def getsprite(self, locked, facing, x, y):
        #named like door_locked_left.png etc

        if facing == FACINGDOWN:
            spritename = "down.png"
            self.rect = pg.Rect(x + self.width/3, y + self.height-5, self.width/3, 5)
        elif facing == FACINGLEFT:
            spritename = "left.png"
            self.rect = pg.Rect(x, y+ self.height/3, 5, self.height/3)
        elif facing == FACINGRIGHT:
            spritename = "right.png"
            self.rect = pg.Rect(x + self.width-5, y+ self.height/3, 5, self.height/3)
        else:
            spritename = "up.png"
            self.rect = pg.Rect(x + self.width/3, y, self.width/3, 5)

        self.image = pg.transform.scale( pg.image.load(os.path.join('assets', "door_open_" + spritename)) , (self.width,self.height) )
        self.imagelocked = pg.transform.scale( pg.image.load(os.path.join('assets', "door_locked_" + spritename)) , (self.width,self.height) )

        if(locked > 1):
            self.imagelocked2 = pg.transform.scale( pg.image.load(os.path.join('assets', "door_locked_up_2.png")) , (self.width,self.height) )
            self.imagelocked3 = pg.transform.scale( pg.image.load(os.path.join('assets', "door_locked_up_3.png")) , (self.width,self.height) )
            self.imagelocked4 = pg.transform.scale( pg.image.load(os.path.join('assets', "door_locked_up_4.png")) , (self.width,self.height) )

    def draw(self):
        if(self.state <= 0):
            WIN.blit(self.image, (self.x, self.y))
        elif self.state == 1:
            WIN.blit(self.imagelocked, (self.x, self.y))
        elif self.state == 2:
            WIN.blit(self.imagelocked2, (self.x, self.y))
        elif self.state == 3:
            WIN.blit(self.imagelocked3, (self.x, self.y))
        else:
            WIN.blit(self.imagelocked4, (self.x, self.y))

    def interact(self, player):
        self.state = self.locked - player.keys
        if looking_at_npc(player.facing, player.rect, self.rect) and self.state <= 0:
            pg.event.post(pg.event.Event(EXITROOM))
        return 1
    

    
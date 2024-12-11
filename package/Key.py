import pygame as pg
from .everywhere import *
from .functions import *
from .Interactor import *


class Key(Interactor):

    def __init__(self, x, y, box=None):
        self.height = 30
        self.width = 15
        self.rect = pg.Rect(x,y,self.width,self.height)
        self.image = self.image = pg.transform.scale( pg.image.load(os.path.join('assets', 'key.png')) , (self.width,self.height) )
        if box != None:
            self.inbox = True
            self.parentbox = box
        else:
            self.inbox = False

    def draw(self):
        if self.inbox and TEXTBOXES.count(self.parentbox) == 0:
            return
        WIN.blit(self.image, (self.rect.x, self.rect.y))

    def get_collider(self):
        return pg.Rect(0,0,0,0)
    
    def interact(self, player):
        if self.inbox and TEXTBOXES.count(self.parentbox) == 0:
            return 1
        
        if(OBJECTSOVERTEXTBOXES.count(self) == 0):
            OBJECTSOVERTEXTBOXES.append(self)
        
        if player.rect.colliderect(self.rect):
            pg.event.post(pg.event.Event(KEYGET))
            OBJECTS.remove(self)
            if(OBJECTSOVERTEXTBOXES.count(self) == 1):
                OBJECTSOVERTEXTBOXES.remove(self)
            return 0
        
        return 1
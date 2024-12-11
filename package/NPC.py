from .Interactor import *
import pygame as pg
import os

from .everywhere import *
from .functions import *

class NPC(Interactor):
    
    def __init__(self, x, y):
        #super().__init__(x,y)
        self.width = 50
        self.height = 100
        self.rect = pg.Rect(x,y,self.width,self.height)
        #self.colliderrect = pg.Rect(x,y+50,self.width,self.height - 50)
        self.image = pg.transform.scale( pg.image.load(os.path.join('assets', 'npc_blank.png')) , (self.width,self.height) )
        
        self.textboxes = []
        self.tb_cnt = 0
        self.speaking = False
        self.current_tb = -1
        self.bump = False
        self.hasSpokenOnce = 0
        self.totaltbs = None
        self.no_count = False

    def get_collider(self):
        return self.rect
        
    def draw(self):
        if self.totaltbs is None:
            self.totaltbs = GAMETXT.render(str(len(self.textboxes)), 1, WHITE)
        
        if self.bump:
            self.bump = False
        WIN.blit(self.image, (self.rect.x, self.rect.y))

        if not self.no_count:
            if not self.hasSpokenOnce == 2:
                pg.draw.circle(WIN, RED, (self.rect.x+50-5, self.rect.y + 5), 15)
            else:
                pg.draw.circle(WIN, DGREY, (self.rect.x+50-5, self.rect.y + 5), 15)
            WIN.blit(self.totaltbs, (self.rect.x + 47 - self.totaltbs.get_width()//2, self.rect.y -18))
        
    def interact(self, player):
        if self.bump:
            self.bump = False
            self.do_next_textbox()
            return 1
        
        if self.hasSpokenOnce == 0 and self.current_tb > -1:
            self.hasSpokenOnce = 1
        elif self.hasSpokenOnce == 1 and self.current_tb == -1:
            self.hasSpokenOnce = 2

        if self.speaking and player.interacting:
            #print("next")
            self.do_next_textbox()
        
        elif player.interacting and looking_at_npc(player.facing, player.rect, self.rect) and self.tb_cnt > 0:
            #print("Triggered convo!")
            self.bump = True
            bump_object_in_order(self)
            return 0
        
        return 1
            
    def do_next_textbox(self):
        if self.current_tb == -1:
            STARTREADINGSOUND.play()
            self.speaking = True
            TEXTBOXES.append(self.textboxes[0])
            self.current_tb = 0
            
        else:
            CONTREADINGSOUND.play()
            TEXTBOXES.remove(self.textboxes[self.current_tb])
            self.current_tb = self.current_tb + 1
            if self.current_tb >= self.tb_cnt:
                #print("gone")
                self.current_tb = -1
                self.speaking = False
            else:
                TEXTBOXES.append(self.textboxes[self.current_tb])
            
    def give_textbox(self, next_tb):
        self.textboxes.append(next_tb)
        self.tb_cnt = self.tb_cnt + 1
        next_tb.number = self.tb_cnt

    def give_textboxes(self, next_tbs):
        for tb in next_tbs:
            self.give_textbox(tb)
        #self.textboxes.extend(next_tbs)
        #self.tb_cnt = self.tb_cnt + len(next_tbs)
        
    def can_interact(self, player):
        return looking_at_npc(player.facing, player.rect, self.rect)
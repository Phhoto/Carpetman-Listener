import pygame as pg
import os

from .everywhere import *
from .functions import *

class Player:
    width=50
    height=80
    speed=7
    diagonal_spd = 5
    interacing = False
    facing = 0
    is_stuck = False
    stuckfor = 0
    keys = 0
    pic = 0
    bumppic = 0
    
    def __init__(self, x, y):
        self.rect = pg.Rect(x,y,self.width,self.height)
        # self.image = pg.transform.scale( pg.image.load(os.path.join('assets', 'carpetman.png')) , (self.width,self.height) )
        # self.up_image = pg.transform.scale( pg.image.load(os.path.join('assets', 'carpetman_up.png')) , (self.width,self.height) )
        # self.down_image = pg.transform.scale( pg.image.load(os.path.join('assets', 'carpetman_down.png')) , (self.width,self.height) )
        # self.right_image = pg.transform.scale( pg.image.load(os.path.join('assets', 'carpetman_right.png')) , (self.width,self.height) )
        # self.left_image = pg.transform.scale( pg.image.load(os.path.join('assets', 'carpetman_left.png')) , (self.width,self.height) )

        self.up_images = [pg.transform.scale( pg.image.load(os.path.join('assets', 'cmu1.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cmu2.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cmu3.png')) , (self.width,self.height) )]
        self.down_images = [pg.transform.scale( pg.image.load(os.path.join('assets', 'cmd1.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cmd2.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cmd3.png')) , (self.width,self.height) )]
        self.right_images = [pg.transform.scale( pg.image.load(os.path.join('assets', 'cmr1.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cmr2.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cmr3.png')) , (self.width,self.height) )]
        self.left_images = [pg.transform.scale( pg.image.load(os.path.join('assets', 'cml1.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cml2.png')) , (self.width,self.height) ), pg.transform.scale( pg.image.load(os.path.join('assets', 'cml3.png')) , (self.width,self.height) )]
        # self.up_image2 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cmu2.png')) , (self.width,self.height) )
        # self.down_image2 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cmd2.png')) , (self.width,self.height) )
        # self.right_image2 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cmr2.png')) , (self.width,self.height) )
        # self.left_image2 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cml2.png')) , (self.width,self.height) )
        # self.up_image3 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cmu3.png')) , (self.width,self.height) )
        # self.down_image3 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cmd3.png')) , (self.width,self.height) )
        # self.right_image3 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cmr3.png')) , (self.width,self.height) )
        # self.left_image3 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cml3.png')) , (self.width,self.height) )
        self.imagesuite = self.down_images
        
    def draw(self):
        self.pic = (self.pic + 1)%30
        if(self.pic < 15):
            WIN.blit(self.imagesuite[0], (self.rect.x, self.rect.y))
        elif(self.pic < 30):
            WIN.blit(self.imagesuite[1], (self.rect.x, self.rect.y))
        else:
            WIN.blit(self.imagesuite[2], (self.rect.x, self.rect.y))

    def move(self, keys):
        active_speed = self.speed
        self.bumppic = 0
        if self.interacting:
            COLLIDERS.clear()
            COLLIDERS.extend(produce_colliders())
            
        if self.is_stuck:
            self.stuckfor = self.stuckfor + 1
        
        collide_up, collide_down, collide_left, collide_right = self.stuck()
        self.is_stuck = collide_up and collide_down and collide_left and collide_right
        
        #if multiple keys pressed slow down
        if (keys[pg.K_w] + keys[pg.K_d] + keys[pg.K_s] + keys[pg.K_a] + keys[pg.K_UP] + keys[pg.K_DOWN] + keys[pg.K_LEFT] + keys[pg.K_RIGHT]) > 1:
            active_speed = self.diagonal_spd
        
        #resolve move, move out of walls if colliding
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.bumppic = 1
            if active_speed == self.speed: self.change_direction(pg.K_w)
            self.rect.y -= active_speed
            back_cnt = 0
            while self.rect.collidelist(COLLIDERS) != -1 and back_cnt < active_speed:
                self.rect.y += 1
                back_cnt += 1

        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.bumppic = 1
            if active_speed == self.speed: self.change_direction(pg.K_s)
            self.rect.y += active_speed
            back_cnt = 0
            while self.rect.collidelist(COLLIDERS) != -1 and back_cnt < active_speed:
                self.rect.y -= 1
                back_cnt += 1

        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.bumppic = 1
            if active_speed == self.speed: self.change_direction(pg.K_a)
            self.rect.x -= active_speed
            back_cnt = 0
            while self.rect.collidelist(COLLIDERS) != -1 and back_cnt < active_speed:
                self.rect.x += 1
                back_cnt += 1

        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.bumppic = 1
            if active_speed == self.speed: self.change_direction(pg.K_d)
            self.rect.x += active_speed
            #if any(self.rect.colliderect(wall) for wall in walls):
            #    self.rect.x -= active_speed
            back_cnt = 0
            while self.rect.collidelist(COLLIDERS) != -1 and back_cnt < active_speed:
                self.rect.x -= 1
                back_cnt += 1

        self.pic = (self.pic + self.bumppic)%30
                
    def change_direction(self, key):
        if key == pg.K_w or key == pg.K_UP:
            self.imagesuite = self.up_images
            self.facing = FACINGUP
        if key == pg.K_s or key == pg.K_DOWN:
            self.imagesuite = self.down_images
            self.facing = FACINGDOWN
        if key == pg.K_d or key == pg.K_RIGHT:
            self.imagesuite = self.right_images
            self.facing = FACINGRIGHT
        if key == pg.K_a or key == pg.K_LEFT:
            self.imagesuite = self.left_images
            self.facing = FACINGLEFT
            
    def stuck(self):
        self.rect.y -= self.speed
        collide_up = (self.rect.collidelist(COLLIDERS) != -1)
        self.rect.y += self.speed
        self.rect.y += self.speed
        collide_down = (self.rect.collidelist(COLLIDERS) != -1)
        self.rect.y -= self.speed
        self.rect.x += self.speed
        collide_right = (self.rect.collidelist(COLLIDERS) != -1)
        self.rect.x -= self.speed
        self.rect.x -= self.speed
        collide_left = (self.rect.collidelist(COLLIDERS) != -1)
        self.rect.x += self.speed
        return collide_up, collide_down, collide_left, collide_right
    


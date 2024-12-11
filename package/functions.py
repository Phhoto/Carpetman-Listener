import pygame as pg
import os

from .everywhere import *

#use this to make and object (and therefore its textboxes) be rendered last (on top)
def bump_object_in_order(obj):
    OBJECTS.append(obj)
    OBJECTS.remove(obj)
    
#pass npc to textbox constructor 
def tbx(npc):
    return npc.rect.x + (npc.width/2)

def tby(npc):
    return npc.rect.y

#based on walls, objects, textboxes, find all current collision rects:
def produce_colliders():
    colliders = WALLS + [obj.get_collider() for obj in OBJECTS]  + GAMEBORDERS
    coll_to_add = []
    coll_to_remove = []
    
    for tb in TEXTBOXES:
        if tb.type == BLOCK:
            walkable_zone = tb.body
            colliders.append(tb.border)
        else:
            walkable_zone = tb.border
        
        for collider in colliders:
            overlap = collider.clip(walkable_zone)
            if overlap.size != 0:
                #pg.draw.rect(WIN, (200,250,200), overlap)
                upperrect = collider.clip(pg.Rect(0, 0, SCRN_WIDTH, overlap.y))
                lowerrect = collider.clip(pg.Rect(0, overlap.bottomleft[1], SCRN_WIDTH, SCRN_HEIGHT))
                leftrect = collider.clip(pg.Rect(0, 0, overlap.x, SCRN_HEIGHT))
                rightrect = collider.clip(pg.Rect(overlap.topright[0], 0, SCRN_WIDTH, SCRN_HEIGHT))
                coll_to_add.extend([upperrect, lowerrect, leftrect, rightrect])
                coll_to_remove.append(collider)
                
                #pg.draw.rect(WIN, (100,250,100), upperrect)
                #pg.draw.rect(WIN, (50,50,100), lowerrect)
                #pg.draw.rect(WIN, (250,20,150), leftrect)
                #pg.draw.rect(WIN, (200,100,200), rightrect)
                
        for r in coll_to_remove:
            colliders.remove(r)
        colliders.extend(coll_to_add)
        coll_to_remove.clear()
        coll_to_add.clear()
        
    #for c in colliders:
        #pg.draw.rect(WIN, (100,250,100), c)
        
        #may want to move gameborders up to allow textbox bypass ???
    return colliders + [pg.Rect(0,0,1200,1)]


#determine if player is facing npc
def looking_at_npc(facing, player, npc):
    left_rect = pg.Rect(npc.x-TALKDIST, npc.y, TALKDIST, npc.height)
    right_rect = pg.Rect(npc.x+npc.width, npc.y, TALKDIST, npc.height)
    #extra to prevent clipping into block objects
    top_rect = pg.Rect(npc.x, npc.y-TALKDIST+5, npc.width, TALKDIST-5)
    bottom_rect = pg.Rect(npc.x, npc.y+npc.height, npc.width, TALKDIST*2)
    
    if facing == FACINGDOWN and player.colliderect(top_rect):
        return True
    
    if facing == FACINGUP and player.colliderect(bottom_rect):
        return True
    
    if facing == FACINGLEFT and player.colliderect(right_rect):
        return True
    
    if facing == FACINGRIGHT and player.colliderect(left_rect):
        return True
    
    return False


def drawForTesting(facing, player, npc):
    left_rect = pg.Rect(npc.x-TALKDIST, npc.y, TALKDIST, npc.height)
    right_rect = pg.Rect(npc.x+npc.width, npc.y, TALKDIST, npc.height)
    top_rect = pg.Rect(npc.x, npc.y-TALKDIST, npc.width, TALKDIST)
    bottom_rect = pg.Rect(npc.x, npc.y+npc.height, npc.width, TALKDIST*2)
    pg.draw.rect(WIN, (200,10,10), left_rect)
    pg.draw.rect(WIN, (200,10,10), right_rect)
    pg.draw.rect(WIN, (200,10,10), top_rect)
    pg.draw.rect(WIN, (200,10,10), bottom_rect)


def draw_UI(player):
    
    leftx = 120
    center = SCRN_WIDTH/2
    
    if interaction_available(player):
        #print("interaction available")
        pg.draw.rect(WIN, GREY, pg.Rect(520, 827, 158, 43))
    else:
        #print("x")
        pg.draw.rect(WIN, DGREY, pg.Rect(520, 827, 158, 43))
    
    if player.is_stuck:
        if player.stuckfor%20 < 10:
            pg.draw.rect(WIN, RED, pg.Rect(97, 827, 43, 43))
        else:
            pg.draw.rect(WIN, DGREY, pg.Rect(97, 827, 43, 43))
    else:
        pg.draw.rect(WIN, DGREY, pg.Rect(97, 827, 43, 43))
    
    WIN.blit(HOLD_text, (leftx - HOLD_text.get_width()//2, 792))
    WIN.blit(R_text, (leftx - R_text.get_width()//2, 802))
    WIN.blit(TORESTART_text, (leftx - TORESTART_text.get_width()//2, 860))
    
    WIN.blit(PRESS_text, (center - PRESS_text.get_width()//2, 792))
    if len(TEXTBOXES) == 0:
        WIN.blit(SPACE_text_white, (center - SPACE_text_white.get_width()//2, 802))
    else:
        WIN.blit(SPACE_text_cyan, (center - SPACE_text_cyan.get_width()//2, 802))
    
    WIN.blit(TOINTERACT_text, (center - TOINTERACT_text.get_width()//2, 860))
    
    
def interaction_available(player):
    for npc in OBJECTS:
        if npc.can_interact(player):
            return True
    return False

def draw_UI_updated(player, tb):
    leftx = 120
    center = SCRN_WIDTH/2
    offset = 100
    
    if interaction_available(player):
        #print("interaction available")
        pg.draw.rect(WIN, GREY, pg.Rect(520-offset, 827, 158, 43))
    else:
        #print("x")
        pg.draw.rect(WIN, DGREY, pg.Rect(520-offset, 827, 158, 43))

    pg.draw.rect(WIN, DGREY, pg.Rect(520+offset, 827, 158, 43))
    
    if player.is_stuck:
        if player.stuckfor%20 < 10:
            pg.draw.rect(WIN, RED, pg.Rect(97, 827, 43, 43))
        else:
            pg.draw.rect(WIN, DGREY, pg.Rect(97, 827, 43, 43))
    else:
        pg.draw.rect(WIN, DGREY, pg.Rect(97, 827, 43, 43))
    
    WIN.blit(HOLD_text, (leftx - HOLD_text.get_width()//2, 792))
    WIN.blit(R_text, (leftx - R_text.get_width()//2, 802))
    WIN.blit(TORESTART_text, (leftx - TORESTART_text.get_width()//2, 860))
    
    

    WIN.blit(PRESS_text, (center -offset - PRESS_text.get_width()//2, 792))
    b = bool(len(TEXTBOXES) == 1 and TEXTBOXES.count(tb) == 1)
    if len(TEXTBOXES) == 0 or b:
        WIN.blit(SPACE_text_white, (center -offset - SPACE_text_white.get_width()//2, 802))
    else:
        WIN.blit(SPACE_text_cyan, (center -offset - SPACE_text_cyan.get_width()//2, 802))
    
    WIN.blit(TOINTERACT_text, (center -offset - TOINTERACT_text.get_width()//2, 860))

    WIN.blit(PRESS_text, (center +offset - PRESS_text.get_width()//2, 792))
    WIN.blit(ENTER_text_white, (center +offset- ENTER_text_white.get_width()//2, 802))
    
    WIN.blit(TOTALK_text, (center +offset- TOTALK_text.get_width()//2, 860))


def draw_UI_updating(player, cnt):
    leftx = 120
    center = SCRN_WIDTH/2
    if(cnt < 0):
        offset = 0
    elif(cnt < 21):
        offset = cnt*5
    else:
        offset = 100
    
    if interaction_available(player):
        #print("interaction available")
        pg.draw.rect(WIN, GREY, pg.Rect(520-offset, 827, 158, 43))
    else:
        #print("x")
        pg.draw.rect(WIN, DGREY, pg.Rect(520-offset, 827, 158, 43))

    
    
    if player.is_stuck:
        if player.stuckfor%20 < 10:
            pg.draw.rect(WIN, RED, pg.Rect(97, 827, 43, 43))
        else:
            pg.draw.rect(WIN, DGREY, pg.Rect(97, 827, 43, 43))
    else:
        pg.draw.rect(WIN, DGREY, pg.Rect(97, 827, 43, 43))
    
    WIN.blit(HOLD_text, (leftx - HOLD_text.get_width()//2, 792))
    WIN.blit(R_text, (leftx - R_text.get_width()//2, 802))
    WIN.blit(TORESTART_text, (leftx - TORESTART_text.get_width()//2, 860))
    

    WIN.blit(PRESS_text, (center -offset - PRESS_text.get_width()//2, 792))
    if len(TEXTBOXES) == 0:
        WIN.blit(SPACE_text_white, (center -offset - SPACE_text_white.get_width()//2, 802))
    else:
        WIN.blit(SPACE_text_cyan, (center -offset - SPACE_text_cyan.get_width()//2, 802))
    
    WIN.blit(TOINTERACT_text, (center -offset - TOINTERACT_text.get_width()//2, 860))

    
    if(cnt > 20):
        cnt -= 20
        

        pg.draw.rect(WIN, DGREY, pg.Rect(520+offset, 827, 158, 43))
        WIN.blit(PRESS_text, (center +offset - PRESS_text.get_width()//2, 792))
        WIN.blit(ENTER_text_white, (center +offset- ENTER_text_white.get_width()//2, 802))
        WIN.blit(TOTALK_text, (center +offset- TOTALK_text.get_width()//2, 860))

        pg.draw.rect(WIN, UIBACKGROUND, pg.Rect(520+offset-10, 800+cnt, 158+20, 100-cnt))

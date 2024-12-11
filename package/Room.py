import pygame as pg
import os

from .everywhere import *
from .functions import *
from .Player import *
from .Key import *
from .Textbox import *

class Room:
    def __init__(self, player_x, player_y):
        self.walls = []
        self.objects = []
        self.playerx = player_x
        self.playery = player_y

    def addobjs(self, o):
        self.objects.extend(o)

    def addwalls(self, w):
        self.walls.extend(w)


    def run_room(self, num):
        player = Player(self.playerx, self.playery)
        self.roomtext = GAMETXTMED.render("ROOM " + str(num+1), 1, WHITE)
        try:
            f = open(os.path.join('assets', 'save.txt'), 'w')
        except Exception:
            pass
        else:
            f.write(str(num))
            f.close()

        OBJECTS.clear()
        OBJECTS.extend(self.objects)

        WALLS.clear()
        WALLS.extend(self.walls)

        TEXTBOXES.clear()
        OBJECTSOVERTEXTBOXES.clear()

        COLLIDERS.clear()
        COLLIDERS.extend(produce_colliders())

        run = True
        clock = pg.time.Clock()
        reset_counter = 0
        STARTSOUND.play()
        while run:
            clock.tick(FPS)
            player.interacting = False
            
            #event loop
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    return -1000
                if event.type == RESET:
                    return 0
                if event.type == EXITROOM:
                    return 1
                if event.type == KEYGET:
                    KEYSOUND.play()
                    player.keys = player.keys + 1
                    OBJECTS.append(Key(925 + player.keys*50, 820))
                    OBJECTSOVERTEXTBOXES.append(Key(925 + player.keys*50, 820))
                
                #key presses
                if event.type == pg.KEYDOWN:
                    # is player interacting? (is space pressed)
                    if event.key == pg.K_SPACE:
                        player.interacting = True
                        
                    if event.key == pg.K_w or event.key == pg.K_a or event.key == pg.K_d or event.key == pg.K_s or event.key == pg.K_UP or event.key == pg.K_DOWN or event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        player.change_direction(event.key)

                if event.type == pg.MOUSEBUTTONUP:
                    print(pg.mouse.get_pos())
                
            #object interaction loop
            i = 0
            while i < len(OBJECTS):
                i += OBJECTS[i].interact(player)
            
            #updates
            keys = pg.key.get_pressed()
            player.move(keys)
            
            if keys[pg.K_r]:
                reset_counter += 1
                if reset_counter > 65:
                    pg.event.post(pg.event.Event(RESET))
            else:
                reset_counter == 0
            
            self.draw_room(player)

    # background < walls < UI < borderwalls < entities < textboxes < player < special entites
    def draw_room(self, player):
        WIN.fill(BLUE)
        pg.draw.rect(WIN, UIBACKGROUND, MENUBG)
        
        for wall in WALLS:
            pg.draw.rect(WIN, BORDERCOLOUR, wall)

        draw_UI(player)
        WIN.blit(self.roomtext, (SCRN_WIDTH - 10 - self.roomtext.get_width(), 850))

        for gamewall in GAMEBORDERS:
            pg.draw.rect(WIN, BORDERCOLOUR, gamewall)
            
        for obj in OBJECTS:
            obj.draw()
            #drawForTesting(player.facing, player.rect, obj.rect)
            
        
        for tb in TEXTBOXES:
            tb.draw()

        player.draw()

        for obj in OBJECTSOVERTEXTBOXES:
            obj.draw()
        
        pg.display.update()

    
class UpdatedRoom(Room):
    def __init__(self, player_x, player_y):
        self.walls = []
        self.objects = []
        self.playerx = player_x
        self.playery = player_y
        self.wantsanimation = False
        self.counter = -3
        self.run_animation = -1
        self.tb = None

    def addobjs(self, o):
        self.objects.extend(o)

    def addwalls(self, w):
        self.walls.extend(w)


    def run_room(self, num):
        player = Player(self.playerx, self.playery)
        self.roomtext = GAMETXTMED.render("ROOM " + str(num+1), 1, WHITE)
        try:
            f = open(os.path.join('assets', 'save.txt'), 'w')
        except Exception:
            pass
        else:
            f.write(str(num))
            f.close()


        OBJECTS.clear()
        OBJECTS.extend(self.objects)

        WALLS.clear()
        WALLS.extend(self.walls)

        TEXTBOXES.clear()
        OBJECTSOVERTEXTBOXES.clear()

        COLLIDERS.clear()
        COLLIDERS.extend(produce_colliders())

        run = True
        clock = pg.time.Clock()
        reset_counter = 0
        STARTSOUND.play()
        while run:
            clock.tick(FPS)
            player.interacting = False
            
            #event loop
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    return -1000
                if event.type == RESET:
                    return 0
                if event.type == EXITROOM:
                    return 1
                if event.type == KEYGET:
                    KEYSOUND.play()
                    player.keys = player.keys + 1
                    OBJECTS.append(Key(940 + player.keys*50, 820))
                    OBJECTSOVERTEXTBOXES.append(Key(940 + player.keys*50, 820))
                
                #key presses
                if event.type == pg.KEYDOWN:
                    # is player interacting? (is space pressed)
                    if event.key == pg.K_SPACE:
                        player.interacting = True
                        self.counter = self.counter + 1

                    if self.wantsanimation == False and event.key == pg.K_RETURN:
                        self.talk(player)
                        COLLIDERS.clear()
                        COLLIDERS.extend(produce_colliders())
                        
                    if event.key == pg.K_w or event.key == pg.K_a or event.key == pg.K_d or event.key == pg.K_s or event.key == pg.K_UP or event.key == pg.K_DOWN or event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        player.change_direction(event.key)

                if event.type == pg.MOUSEBUTTONUP:
                    print(pg.mouse.get_pos())
                
            #object interaction loop
            i = 0
            while i < len(OBJECTS):
                i += OBJECTS[i].interact(player)
            
            #updates
            keys = pg.key.get_pressed()
            player.move(keys)
            
            if keys[pg.K_r]:
                reset_counter += 1
                if reset_counter > 65:
                    pg.event.post(pg.event.Event(RESET))
            else:
                reset_counter == 0
            
            self.draw_room(player)

    def talk(self, player):
        if player.facing == FACINGDOWN:
            tb = Textbox(player.rect.x + 25, player.rect.y + 175 + TEXTGAP, 700, WALK, "you", "Hello?")
        elif player.facing == FACINGLEFT:
            tb = Textbox(player.rect.x - 97 - TEXTGAP, player.rect.y + 97, 700, WALK, "you", "Hello?")
        elif player.facing == FACINGRIGHT:
            tb = Textbox(player.rect.x +50 + 97 + TEXTGAP, player.rect.y + 97, 700, WALK, "you", "Hello?")
        elif player.facing == FACINGUP:
            tb = Textbox(tbx(player), tby(player) + 10, 700, WALK, "you", "Hello?")
        else:
            return

        SENDSOUND.play()
        if self.tb is not None:
            TEXTBOXES.remove(self.tb)
        self.tb = tb
        TEXTBOXES.append(tb)
        return

    # background < walls < UI < borderwalls < entities < textboxes < player < special entites
    def draw_room(self, player):
        WIN.fill(BLUE)
        pg.draw.rect(WIN, UIBACKGROUND, MENUBG)
        
        for wall in WALLS:
            pg.draw.rect(WIN, BORDERCOLOUR, wall)

        if self.wantsanimation:
            if(self.run_animation > 98):
                self.wantsanimation = False
            if(self.run_animation > -1):
                draw_UI_updating(player, self.run_animation)
                self.run_animation = self.run_animation + 1
            else:
                draw_UI_updating(player, self.counter)
            if self.run_animation == -1 and self.counter == 20:
                self.run_animation = 21
        else:
            draw_UI_updated(player, self.tb)
        WIN.blit(self.roomtext, (SCRN_WIDTH - 10 - self.roomtext.get_width(), 850))

        for gamewall in GAMEBORDERS:
            pg.draw.rect(WIN, BORDERCOLOUR, gamewall)
            
        for obj in OBJECTS:
            obj.draw()
            #drawForTesting(player.facing, player.rect, obj.rect)
            
        
        for tb in TEXTBOXES:
            tb.draw()

        player.draw()

        for obj in OBJECTSOVERTEXTBOXES:
            obj.draw()
        
        pg.display.update()
import pygame as pg
from .everywhere import *
from .functions import *

class Interactor:
    width=50
    height=50
    
    def __init__(self, x, y):
        self.rect = pg.Rect(x,y,self.width,self.height)
        #self.image = pg.transform.scale( pg.image.load(os.path.join('assets', 'carpetman.bmp')) , (self.width,self.height) )
        
    def draw(self):
        pg.draw.rect(WIN, (150,150,150), self.rect)
        
    def get_collider(self):
        return self.rect
        
    def interact(self, player):
        return 1
    
    def can_interact(self, player):
        return False
    

#rect that kills you when touched
class Hazard(Interactor):
    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x,y,w,h)
        self.rectlist = [self.rect]

    def draw(self):
        for r in self.rectlist:
            pg.draw.rect(WIN, RED, r)

    def get_collider(self):
        self.rectlist.clear()
        split = False
        for tb in TEXTBOXES:
            overlap = self.rect.clip(tb.border)
            if overlap.size != 0:
                split = True
                upperrect = self.rect.clip(pg.Rect(0, 0, SCRN_WIDTH, overlap.y))
                lowerrect = self.rect.clip(pg.Rect(0, overlap.bottomleft[1], SCRN_WIDTH, SCRN_HEIGHT))
                leftrect = self.rect.clip(pg.Rect(0, 0, overlap.x, SCRN_HEIGHT))
                rightrect = self.rect.clip(pg.Rect(overlap.topright[0], 0, SCRN_WIDTH, SCRN_HEIGHT))
                self.rectlist.extend([upperrect, lowerrect, leftrect, rightrect])
            
        if not split:
            self.rectlist.append(self.rect)

        return pg.Rect(0,0,0,0)
    

    def interact(self, player):
        if player.rect.collidelist(self.rectlist) != -1:
            #maybe add death frames here? or custom death event
            pg.event.post(pg.event.Event(RESET))
        return 1

    def can_interact(self, player):
        return super().can_interact(player)
    


class BeamShooter(Interactor):
    def __init__(self, x, y, face, receivers):
        self.rect = pg.Rect(x,y,self.width,self.height)
        self.r = receivers
        self.facing = face
        self.timer = 0
        if face == FACINGDOWN:
            self.spitter = pg.Rect(self.rect.centerx-5, self.rect.bottom-5, 10,10)
            self.beamx = self.rect.centerx-2
            self.beamy = self.rect.bottom
        elif face == FACINGUP:
            self.spitter = pg.Rect(self.rect.centerx-5, self.rect.y-5, 10,10)
            self.beamx = self.rect.centerx-2
            self.beamy = self.rect.y+10
        elif face == FACINGLEFT:
            self.spitter = pg.Rect(self.rect.x, self.rect.centery-5, 10,10)
            self.beamx = self.rect.x - 10
            self.beamy = self.rect.centery-2
        elif face == FACINGRIGHT:
            self.spitter = pg.Rect(self.rect.right-10, self.rect.centery-5, 10,10)
            self.beamx = self.rect.right
            self.beamy = self.rect.centery-2
        

    def draw(self):
        pg.draw.rect(WIN, DRED, self.rect)
        pg.draw.rect(WIN, DGREY, self.spitter)

    def interact(self, player):
        self.timer += 1
        if(self.timer > 20):
            beam = Beam(self.beamx, self.beamy, self.facing, self.r)
            OBJECTS.append(beam)
            OBJECTSOVERTEXTBOXES.append(beam)
            self.timer = 0
        return 1


class Beam(Interactor):
    def __init__(self, x, y ,face, receivers):
        self.facing = face
        self.r = receivers
        if face == FACINGDOWN:
            self.rect = pg.Rect(x,y, 4,10)
            self.xspd = 0
            self.yspd = 7
        elif face == FACINGUP:
            self.rect = pg.Rect(x,y-15, 4,10)
            self.xspd = 0
            self.yspd = -7
        elif face == FACINGLEFT:
            self.rect = pg.Rect(x,y, 10,4)
            self.xspd = -7
            self.yspd = 0
        elif face == FACINGRIGHT:
            self.rect = pg.Rect(x,y, 10,4)
            self.xspd = 7
            self.yspd = 0


    def draw(self):
        pg.draw.rect(WIN, YELLOW, self.rect)

    def get_collider(self):
        return pg.Rect(0,0,0,0)
    
    def interact(self, player):
        self.rect.x += self.xspd
        self.rect.y += self.yspd

        if self.rect.collidelist(COLLIDERS) != -1:
            for rec in self.r:
                if self.rect.colliderect(rec.triggerzone):
                    rec.triggered = True
            OBJECTSOVERTEXTBOXES.remove(self)
            OBJECTS.remove(self)
        return 1

class Receiver(Interactor):
    def __init__(self, bodyrect, receiverrect, time):
        self.rect = bodyrect
        self.triggerzone = receiverrect
        self.timer = time
        self.time = time
        self.triggered = False
        self.col = GREY
        self.starton = []
        self.startoff = []

    def draw(self):
        pg.draw.rect(WIN, DRED, self.rect)
        pg.draw.rect(WIN, self.col, self.triggerzone)

    def get_collider(self):
        return self.rect
    
    def interact(self, player):
        self.timer += 1
        if self.triggered:
            self.timer = 0
            self.triggered = False

        if self.timer == self.time:
            self.col = GREY
            self.deactivate()
        elif self.timer == 0 and self.col != CYAN:
            self.col = CYAN
            self.activate()
        return 1

    #add starton objects directly to OBJECT list of room
    def give_starton(self, objs):
        self.starton.extend(objs)

    def give_startoff(self, objs):
        self.startoff.extend(objs)

    def activate(self):
        SWTICHSOUND.play()
        for obj in self.starton:
            OBJECTS.remove(obj)
        OBJECTS.extend(self.startoff)

    def deactivate(self):
        SWTICHSOUND.play()
        for obj in self.startoff:
            OBJECTS.remove(obj)
        OBJECTS.extend(self.starton)

class Light(Interactor):
    def __init__(self, x, y, num):
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.collider = pg.Rect(0,0,0,0)
        self.text = GAMETXT.render(str(num), 1, WHITE)
        self.textx = x - 20
        self.texty = y - 10
        self.isOn = False

    def draw(self):
        if self.isOn:
            pg.draw.rect(WIN, YELLOW, self.rect)
        else:
            pg.draw.rect(WIN, GREY, self.rect)
        WIN.blit(self.text, (self.textx, self.texty))

    def get_collider(self):
        return self.collider
    


class OrderedLights(Interactor):
    def __init__(self, receivers, lights, hazards):
        self.recs = receivers
        self.lights = lights
        self.check = []
        self.state = []
        self.collider = pg.Rect(0,0,0,0)
        self.len = len(lights)
        self.activated = False
        self.hazards = hazards

        for r in self.recs:
            i = Interactor(SCRN_WIDTH,0)
            self.check.append(i)
            self.state.append(False)
            r.give_startoff([i])

    def draw(self):
        for l in self.lights:
            l.draw()

    def get_collider(self):
        return self.collider
    
    def interact(self, player):
        if self.activated:
            return 1
        
        for i in range(self.len):
            if self.state[i] == False and OBJECTS.count(self.check[i]) > 0:
                self.state[i] = True
                can_activate = True
                for j in range(i):
                    if not self.lights[j].isOn:
                        can_activate = False
                if can_activate:
                    self.lights[i].isOn = True
                    for j in range(i+1, self.len):
                        self.lights[j].isOn = False
                    if i+1 == self.len:
                        self.activated = True
                        for h in self.hazards:
                            OBJECTS.remove(h)
                else:
                    for j in range(self.len):
                        self.lights[j].isOn = False
            elif self.state[i] == True and OBJECTS.count(self.check[i]) == 0:
                self.state[i] = False

        return 1




    

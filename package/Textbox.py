import pygame as pg

from .everywhere import *
from .functions import *
from .Key import *




# ' @ ' produces key inside textbox
class Textbox:
    
    padding = 5
    
    def __init__(self, center_x, top_y, width_cap, t, name, text):
        self.lines = []
        self.cap = 600
        self.w = 10
        self.h = 100
        self.type = t
        self.keyx = -1
        self.number = 0
        self.numtext = None

        
        if(width_cap > 100 and width_cap <= 800):
            self.cap = width_cap

        self.create_text(text)
        self.name = NAMEFONT.render(name, 1, WHITE)

        self.h = TEXTGAP*(len(self.lines) + 1) + SPEECH_HEIGHT*len(self.lines) + BDRWIDTH*2 + EXTRATOPPADDING

        x = center_x - (self.w/2)
        y = top_y - GAP - self.h

        if(self.keyx != -1):
            self.key = Key(x + self.keyx, y + self.keyy, self)

        self.border = pg.Rect(x, y, self.w, self.h)
        self.body = pg.Rect(x+BDRWIDTH, y+BDRWIDTH, self.w-(BDRWIDTH*2), self.h-(BDRWIDTH*2))
        self.pic = pg.Rect(x+BDRWIDTH, y+BDRWIDTH, PICSIZE, PICSIZE)
        self.namebox = pg.Rect(x+BDRWIDTH, y+BDRWIDTH, PICSIZE, NAMESIZE + PICSIZE)
        
    def draw(self):
        if self.numtext is None:
            self.numtext = GAMETXT.render(str(self.number), 1, WHITE)
        if self.type == BLOCK:
            pg.draw.rect(WIN, BLOCK_BORDER, self.border)
        else:
            pg.draw.rect(WIN, WALK_BORDER, self.border)
        pg.draw.rect(WIN, TEXTBOX_BODY, self.body)
        pg.draw.rect(WIN, WHITE, self.pic)
        #WIN.blit(self.image, (self.body.x, self.body.y))
        pg.draw.rect(WIN, DBLUE, self.namebox)

        offsetx = self.padding + PICSIZE
        offsety = TEXTGAP + EXTRATOPPADDING
        for txt in self.lines:
            WIN.blit(txt, (self.body.x + offsetx, self.body.y + offsety))
            offsetx = self.padding
            offsety += SPEECH_HEIGHT + TEXTGAP
            
        if self.number == 0:
            WIN.blit(self.name, (self.namebox.x + PICSIZE/2 - self.name.get_width()/2, self.namebox.y + 15))
        else:
            WIN.blit(self.name, (self.namebox.x + PICSIZE/2 - self.name.get_width()/2, self.namebox.y))
            WIN.blit(self.numtext, (self.namebox.x + PICSIZE/2 - self.numtext.get_width()/2, self.namebox.y + 15))
        #WIN.blit(ST, (self.border.x+BDRWIDTH+PICSIZE, self.body.y+10))

    def create_text(self, text):
        arr = text.split()
        line = ""
        used_space = 0 + PICSIZE
        for s in arr:
            if s == "@":
                self.keyx = len(line)*SPEECH_WIDTH + used_space + 4
                self.keyy = TEXTGAP*len(self.lines) + TEXTGAP + SPEECH_HEIGHT*len(self.lines) + BDRWIDTH + EXTRATOPPADDING + 3
                line = line + " "
            elif len(line + s)*SPEECH_WIDTH + used_space < self.cap or len(line) == 0:
                line = line + s + " "
            else:
                new_text = SPEECH.render(line, 1, WHITE)
                if new_text.get_width() + BDRWIDTH + used_space > self.w:
                    self.w = new_text.get_width() + used_space + BDRWIDTH
                self.lines.append(new_text)
                used_space = 0
                line = s + " "

        new_text = SPEECH.render(line, 1, WHITE)
        if new_text.get_width() + 0 + BDRWIDTH > self.w:
            self.w = new_text.get_width() + used_space + BDRWIDTH
        self.lines.append(SPEECH.render(line, 1, WHITE))

#0

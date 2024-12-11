import pygame as pg
import os

# events
RESET = pg.USEREVENT + 1
EXITROOM = pg.USEREVENT + 2
KEYGET = pg.USEREVENT + 3


# ______ CONSTANTS ______

FPS = 60
SCRN_WIDTH, SCRN_HEIGHT = 1200, 900
FACINGUP = 1
FACINGDOWN = 2
FACINGLEFT = 3
FACINGRIGHT = 4
WALK = 1
BLOCK = 2
TALKDIST = 25
#gap between npcs head and textbox
GAP = 20
#width of textbox coloured border
BDRWIDTH = 8
PICSIZE = 44
NAMESIZE = 14

TEXTGAP = 10
EXTRATOPPADDING = 2


# store static rects in ere for drawing purposes
WALLS = []

#store interactors rects for collision
OBJECTS = []

#store textboxes ???
TEXTBOXES = []

# objects to be drawn on top. also need to be in OBJECTS list
OBJECTSOVERTEXTBOXES = []

#store colliders. Produce with produce_colliders()
COLLIDERS = []


# ______ COLOURS ______

#BLUE = (30,30,180)
BLUE = (0,93,133)
DBLUE = (0,70,99)
WHITE = (250,250,250)
#BORDERCOLOUR = (102, 95, 107)
BORDERCOLOUR = (50,50,50)
GREY = (150, 150, 150)
DGREY = (105, 105, 105)
CYAN = (52, 232, 235)
YELLOW = (246, 252, 56)
HIGHLIGHTSPACE = (203, 204, 171)
RED = (212, 39, 36)
DRED = (165, 30, 28)
WALK_BORDER = (252, 186, 3)
#BLOCK_BORDER = (20, 55, 143)
BLOCK_BORDER = (98, 21, 99)
#TEXTBOX_BODY = (79, 144, 194)
TEXTBOX_BODY = (0, 162, 232)
UIBACKGROUND = (10,10,10)


GAMEBORDERS = [
    pg.Rect(0, 0, 5, SCRN_HEIGHT),
    pg.Rect(SCRN_WIDTH - 5, 0, 5, SCRN_HEIGHT),
    pg.Rect(0, 0, SCRN_WIDTH, 5),
    pg.Rect(0, 795, SCRN_WIDTH, 5),
    pg.Rect(0, SCRN_HEIGHT-5, SCRN_WIDTH, 5)
]

MENUBG = pg.Rect(0,800, SCRN_WIDTH, 100)


#initialise and go!!!
WIN = pg.display.set_mode((SCRN_WIDTH, SCRN_HEIGHT))
pg.display.set_caption("Carpetman Listener")

#text setup
pg.font.init()
# SPEECH is monospaced and .get_height() is accurate
SPEECH = pg.font.Font(os.path.join('assets','FakeReceipt.otf'), 30)
#FONTB = pg.font.Font(os.path.join('assets','PixelDigivolve.otf'), 10)
GAMETXT = pg.font.Font(os.path.join('assets','Masaaki-Regular.otf'), 26)
GAMETXTBIG = pg.font.Font(os.path.join('assets','Masaaki-Regular.otf'), 55)
GAMETXTMED = pg.font.Font(os.path.join('assets','Masaaki-Regular.otf'), 35)
FONT = pg.font.SysFont(None, 48)
#NAMEFONT = pg.font.Font(os.path.join('assets','Masaaki-Regular.otf'), 18)
NAMEFONT = pg.font.Font(os.path.join('assets','FakeReceipt.otf'), 16)

HOLD_text = GAMETXT.render("HOLD", 1, WHITE)
R_text = GAMETXTBIG.render("R", 1, WHITE)
TORESTART_text = GAMETXT.render("TO RESTART", 1, WHITE)


PRESS_text = GAMETXT.render("PRESS", 1, WHITE)
SPACE_text_white = GAMETXTBIG.render("SPACE", 1, WHITE)
SPACE_text_grey = GAMETXTBIG.render("SPACE", 1, GREY)
SPACE_text_cyan = GAMETXTBIG.render("SPACE", 1, WALK_BORDER)
#TOINTERACT_text = GAMETXT.render("TO INTERACT", 1, WHITE)
TOINTERACT_text = GAMETXT.render("TO READ", 1, WHITE)

ENTER_text_white = GAMETXTBIG.render("ENTER", 1, WHITE)
#ENTER_text_grey = GAMETXTBIG.render("ENTER", 1, GREY)
#ENTER_text_cyan = GAMETXTBIG.render("ENTER", 1, WALK_BORDER)
TOTALK_text = GAMETXT.render("TO TALK", 1, WHITE)

SPEECHTEST = SPEECH.render("A", 1, WHITE)
SPEECH_WIDTH = SPEECHTEST.get_width()
SPEECH_HEIGHT = SPEECHTEST.get_height()
#print(SPEECH_HEIGHT)
#print(SPEECH_WIDTH)

ST = SPEECH.render("HELLO THERE EVERYBODY!", 1, WHITE)
NAME = NAMEFONT.render("guy", 1, WHITE)

playtext = GAMETXTBIG.render("play from start", 1, GREY)
continuegame = GAMETXTBIG.render("continue game", 1, GREY)
quitgame = GAMETXTBIG.render("quit", 1, GREY)

pg.mixer.init()
TALKSOUND = pg.mixer.Sound(os.path.join("assets","interact.mp3"))
STARTREADINGSOUND = pg.mixer.Sound(os.path.join("assets","openmessage.mp3"))
CONTREADINGSOUND = pg.mixer.Sound(os.path.join("assets","contmessage.mp3"))
KEYSOUND = pg.mixer.Sound(os.path.join("assets","pickup.mp3"))
STARTSOUND = pg.mixer.Sound(os.path.join("assets","levelstart.mp3"))
SWTICHSOUND = pg.mixer.Sound(os.path.join("assets","switch.mp3"))
SENDSOUND = pg.mixer.Sound(os.path.join("assets","send.mp3"))
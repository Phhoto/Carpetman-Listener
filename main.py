import pygame as pg
import os

from package import *


def draw_testroom(player):
    WIN.fill(BLUE)
    pg.draw.rect(WIN, (10,10,10), MENUBG)
    
    for wall in WALLS:
        pg.draw.rect(WIN, (10,10,10), wall)
        
    for obj in OBJECTS:
        obj.draw()
        #drawForTesting(player.facing, player.rect, obj.rect)
        
    for gamewall in GAMEBORDERS:
        pg.draw.rect(WIN, BORDERCOLOUR, gamewall)
    
    for tb in TEXTBOXES:
        tb.draw()
    
    player.draw()
    
    draw_UI(player)
    
    pg.display.update()
    
def testroom():
    player = Player(200,200)
    npc_a = NPC(600,500)
    npc_b = NPC(100,600)
    npc_c = NPC(800,500)
    npc_list = [npc_a, npc_b, npc_c]
    
    OBJECTS.clear()
    OBJECTS.extend(npc_list)
    
    WALLS.clear()
    WALLS.extend([
        pg.Rect(100, 100, 600, 50),
        pg.Rect(300, 200, 50, 400),
        pg.Rect(650, 200, 50, 400),
        pg.Rect(200, 500, 400, 50)
    ])
    
    tb = Textbox(tbx(npc_a), tby(npc_a), 450, 150)
    tb2 = Textbox(tbx(npc_a), tby(npc_a), 400, 150)
    tb3 = Textbox(tbx(npc_c), tby(npc_c), 450, 150)
    tb4 = Textbox(tbx(npc_c), tby(npc_c), 400, 150)
    TEXTBOXES.clear()
    #TEXTBOXES.extend([tb, tb2])
    npc_a.give_textbox(tb)
    npc_a.give_textbox(tb2)
    npc_c.give_textbox(tb3)
    npc_c.give_textbox(tb4)
    
    COLLIDERS.clear()
    COLLIDERS.extend(produce_colliders())
        
    run = True
    #clock required in all game loops for fps control plz
    clock = pg.time.Clock()
    reset_counter = 0
    stuck_counter = 0
    while run:
        clock.tick(FPS)
        player.interacting = 0
        
        
        #event loop
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                return -1
            
            #key presses
            if event.type == pg.KEYDOWN:
                # is player interacting? (is space pressed)
                if event.key == pg.K_SPACE:
                    player.interacting = True
                    
                if event.key == pg.K_w or event.key == pg.K_a or event.key == pg.K_d or event.key == pg.K_s:
                    player.change_direction(event.key)
            
        #object interaction loop
        for obj in OBJECTS:
            obj.interact(player)
        
        #updates
        keys = pg.key.get_pressed()
        player.move(keys)
        
        if keys[pg.K_r]:
            reset_counter += 1
            if reset_counter > 65:
                return 0
        else:
            reset_counter == 0
        
        draw_testroom(player)

def maketestroom():
    testing = Room(200,200)
    testing.addwalls([
        pg.Rect(100, 100, 600, 50),
        pg.Rect(300, 200, 50, 400),
        pg.Rect(650, 200, 50, 400),
        pg.Rect(200, 500, 400, 50)
    ])
    
    npc_a = NPC(600,500)
    npc_b = NPC(100,600)
    npc_c = NPC(800,500)
    tb = Textbox(tbx(npc_a), tby(npc_a), 600, WALK, "guy", "Hello! This is a test to see if textboxes are working correctly so im going to write loads of stuff and see what comes out!")
    tb2 = Textbox(tbx(npc_a), tby(npc_a), 400, WALK, "guy", "Hi! Here is more test but this ones smaller.")
    tb3 = Textbox(tbx(npc_c), tby(npc_c), 400, 2, "jake", "EXCuseme what is up hello boys hello my guy waht is occuring even does this format nicely i hope it does whoopie")
    tb4 = Textbox(tbx(npc_c), tby(npc_c), 600, WALK, "jake", "shortlong")
    tb5 = Textbox(tbx(npc_c), tby(npc_c), 400, 2, "jake", "EXCuseme what is up hello boys hello my guy waht is occuring even does this format nicely i hope it does whoopie")
    npc_a.give_textbox(tb)
    npc_a.give_textbox(tb2)
    npc_c.give_textbox(tb3)
    npc_c.give_textbox(tb4)
    npc_c.give_textbox(tb5)
    exitdoor = Door(SCRN_WIDTH-50, 320, 0, FACINGRIGHT)
    haz = Hazard(1000, 50, 200, 30)
    testing.addobjs([npc_a, npc_b, npc_c, exitdoor, haz])

    return testing

def make_room1():
    room = Room(575, 360)

    npc1 = NPC(425, 210)
    tb1 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "Dana", "Hey guys :)")
    npc1.give_textboxes([tb1])
    npc2 = NPC(725, 210)
    tb2 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Amit", "Alright team")
    npc2.give_textboxes([tb2])
    npc3 = NPC(425, 510)
    tb3 = Textbox(tbx(npc3), tby(npc3), 400, WALK, "Kat", "What's up boys and girls")
    npc3.give_textboxes([tb3])
    npc4 = NPC(725, 510)
    tb4 = Textbox(tbx(npc4), tby(npc4), 700, WALK, "Joey", "Hi guys!! lol")
    npc4.give_textboxes([tb4])
    door = Door(SCRN_WIDTH-50, 620, 0, FACINGRIGHT)

    room.addobjs([npc1, npc2, npc3, npc4, door])
    return room

#walk over textbox
def make_room2():
    room = Room(25, 620)

    npc1 = NPC(400,300)
    door = Door(SCRN_WIDTH-50, 620, 0, FACINGRIGHT)

    tb1 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "Dana", "Hey, it's dana :)")
    tb2 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "Dana", "Just checking in!!!")
    tb3 = Textbox(tbx(npc1), tby(npc1), 800, WALK, "Dana", "I know you're going through a crazy time at the minute but please lmk if you need anything!")
    tb4 = Textbox(tbx(npc1), tby(npc1), 500, WALK, "Dana", "What are you up to today :)")
    npc1.give_textboxes([tb1,tb2,tb3,tb4])

    room.addwalls([pg.Rect(650,0,75,800)])
    room.addobjs([npc1, door])

    return room

#two person bridge
def make_room3():
    room = Room(25, 620)

    npc1 = NPC(320, 400)
    npc2 = NPC(700, 400)
    door = Door(1035, 0, 0, FACINGUP)

    tb1 = Textbox(tbx(npc1), tby(npc1), 350, WALK, "Kat", "Group call sounds good to me I'm wicked at quizzing")


    # tb2 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "guy", "Whats up? This box should be ok to walk across, but you can't use it")
    # tb3 = Textbox(tbx(npc2), tby(npc2), 350, WALK, "guy", "This is teeny but can we do two lines")
    # tb4 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "This one should be plenty large enough to traverse I hope!!")

    tb2 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Joey", "Do you guys want to start doing an online quiz night or something?")
    tb3 = Textbox(tbx(npc2), tby(npc2), 350, WALK, "Joey", "If we are all free one evening")
    tb4 = Textbox(tbx(npc2), tby(npc2), 450, WALK, "Joey", "We could all take it in turns making one each week maybe?")

    npc1.give_textbox(tb1)
    npc2.give_textboxes([tb2, tb3, tb4])

    room.addwalls([
        pg.Rect(210,0,650,390),
        pg.Rect(860,0,100,800)
    ])
    room.addobjs([npc1, npc2, door])
    return room

#bullet flow
def make_room4():
    room = Room(1040, 675)

    npc1 = NPC(600, 350)
    tb1 = Textbox(tbx(npc1), tby(npc1), 500, WALK, "Dana", "Hey!! We missed you at the quiz, will you join next week?? :)")
    npc1.give_textboxes([tb1])

    receiva = Receiver(pg.Rect(700, 745, 50,50), pg.Rect(705,745,40,40), 30)
    haz2 = Hazard(50,100,255, 30)
    haz1 = Hazard(50, 300, 255, 30)
    receiva.give_startoff([haz2])
    receiva.give_starton([haz1])
    shoota = BeamShooter(700,50,FACINGDOWN, [receiva])

    door = Door(127,0,0,FACINGUP)

    room.addwalls([
        pg.Rect(305, 0, 50, 600),
        pg.Rect(0,0,50,600),
        pg.Rect(350,190,400,50)
    ])
    room.addobjs([npc1, receiva, shoota, haz1, door])
    
    return room

#bullets and walkthrough wall
def make_room5():
    room = Room(100, 700)

    room.addwalls([
        pg.Rect(845, 0, 50, 600),
        pg.Rect(1150,0,50,600),
        pg.Rect(250,190,595,50),
        pg.Rect(450,600,445,50)
    ])

    haz1 = Hazard(895, 530, 255, 30)
    haz2 = Hazard(895, 330, 255, 30)
    haz3 = Hazard(895, 130, 255, 30)
    rec = Receiver(pg.Rect(680, 600, 50,50), pg.Rect(685,600,40,40), 50)
    rec.give_starton([haz2])
    rec.give_startoff([haz1, haz3])
    sht = BeamShooter(680,50,FACINGDOWN, [rec])
    npc1 = NPC(590,410)
    # tb1 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "guy", "This is a distance test to let someone get to laser")
    # tb2 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "guy", "Put small one")
    # tb3 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "guy", "And then a nice tall box for prosperity so the beam can pass thanks")

    tb3 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "Amit", "Wazzup do you want to pitch in for a bday present for Kat")
    tb2 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "Amit", "Like 5 quid ish")
    tb1 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "Amit", "I want to get her a pillow with my face on but im getting mixed feedback")
    #edited
    npc1.give_textboxes([tb3,tb2,tb1])
    door = Door(972,0,0,FACINGUP)

    room.addobjs([haz2, npc1, sht, rec, door])

    return room

#walk on and off over pit
def make_room6():
    room = Room(985, 700)

    npc1 = NPC(575, 550)
    tb1 = Textbox(tbx(npc1), tby(npc1), 550, WALK, "Joey", "Has anyone heard of game of thrones before its a tv show")
    tb2 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "Joey", "Ive just started watching it with my mum and i really like it")
    npc1.give_textboxes([tb1,tb2])

    npc2 = NPC(800, 250)
    # tb3 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "Whats up lets make this one quite long I suppose")
    # tb4 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "Lets make this a bit smaller")
    # tb5 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "This one can be any size I suppose")
    # tb6 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "This is small")
    # tb7 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "This one has to be nice and long so they can use this one")
    # tb8 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "guy", "Small to confuse")
    tb3 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "Amit", "Joey are you on crack what are you talking about")
    tb4 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "Amit", "Have I heard of game of thrones")
    tb5 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "Amit", "It released in 2011")
    tb6 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "Amit", "its not new")
    tb7 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "Amit", "It was a cultural phenomenon for a decade")
    tb8 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "Amit", "youre tapped")
    npc2.give_textboxes([tb3,tb4,tb5,tb6,tb7, tb8])

    npc3 = NPC(350, 250)
    tb9 = Textbox(tbx(npc3), tby(npc3), 600, WALK, "Dana", "Joe do not watch game of thrones with your mum lol")
    tb10 = Textbox(tbx(npc3), tby(npc3), 600, WALK, "Dana", "please trust me")
    npc3.give_textboxes([tb9, tb10])

    door = Door(1060,0,0,FACINGUP)

    room.addwalls([
        pg.Rect(190, 0, 820, 470),
        pg.Rect(1010, 300, 190, 170)
    ])

    room.addobjs([npc1, npc2, npc3, door])
    return room

#block tutorial
def make_room7():
    room = Room(1080, 700)

    npc1 = NPC(860,645)
    tb1 = Textbox(tbx(npc1), tby(npc1), 500, BLOCK, "K", "Guys there's a skip on the road and its blocking my driveway")
    tb2 = Textbox(tbx(npc1), tby(npc1), 350, BLOCK, "K", "What am I supposed to do I can't ask them to move it you need like a lorry or smth")
    tb3 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "K", "Actually maybe I can squeeze if I do some dangerous driving quickly")
    tb4 = Textbox(tbx(npc1), tby(npc1), 450, BLOCK, "K", "Wish me luck")
    npc1.give_textboxes([tb1,tb2,tb3,tb4])

    npc2 = NPC(510, 360)
    tb6 = Textbox(tbx(npc2), tby(npc2), 600, 2, "A", "Oh yeah I ordered that you're welcome")
    tb5 = Textbox(tbx(npc2), tby(npc2), 600, BLOCK, "A", "Hop inside and they'll take you to the dump and cover you in landfill xoxo")
    npc2.give_textboxes([tb6,tb5])

    npc3 = NPC(175, 455)
    tb7 = Textbox(tbx(npc3), tby(npc3), 400, WALK, "J", "I got inside a dumpster once it was gross")
    npc3.give_textboxes([tb7])

    door = Door(SCRN_WIDTH-50, 180, 0, FACINGRIGHT)

    room.addobjs([npc1,npc2,npc3,door])
    room.addwalls([
        pg.Rect(710, 375, 490, 50),
        pg.Rect(710, 0, 50, 795)
    ])

    return room

#get within block box to bridge
def make_room7o5():
    room = Room(30, 475)

    npc1 = NPC(300,410)
    tb1 = Textbox(tbx(npc1), tby(npc1), 600, BLOCK, "D", "Are we doing a party for halloween at all? :)")
    tb2 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "D", "or meeting at all")
    tb3 = Textbox(tbx(npc1), tby(npc1), 600, BLOCK, "D", "I want to dress up as zombie mary berry >:)")
    npc1.give_textboxes([tb1,tb2,tb3])

    npc2 = NPC(665,410)
    tb4 = Textbox(tbx(npc2), tby(npc2), 600, WALK, "J", "Yeah I can hpst it at mine thats fine")
    tb5 = Textbox(tbx(npc2), tby(npc2), 450, WALK, "J", "*hpst")
    tb6 = Textbox(tbx(npc2), tby(npc2), 450, WALK, "J", "**host")
    tb7 = Textbox(tbx(npc2), tby(npc2), 450, WALK, "J", "Come over whenever you guys want")
    npc2.give_textboxes([tb4,tb5,tb6,tb7])

    door = Door(1150,475,0,FACINGRIGHT)

    room.addobjs([npc1, npc2, door])

    room.addwalls([
        pg.Rect(250,0,600,400),
        pg.Rect(850,0,50,800)
    ])

    return room

#confusing 3-long bridge
def make_room8():
    room = Room(1080, 700)

    npc1 = NPC(300,300)
    # tb1 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "guy", "Stock text to make the box 1")
    # tb2 = Textbox(tbx(npc1), tby(npc1), 450, BLOCK, "guy", "Stock text to make the box 2")
    # tb3 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "guy", "Stock text to make the box 3")
    # tb4 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "guy", "Stock text to make the box 4")
    tb1 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "Hey! Haven't heard from you for ages?")
    tb2 = Textbox(tbx(npc1), tby(npc1), 450, BLOCK, "", "Do you want go out somewhere soon?")
    tb3 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "Hey! Haven't heard from you for ages?")
    tb4 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "Hey! Haven't heard from you for ages?")
    npc1.give_textboxes([tb1,tb2,tb3,tb4])

    npc2 = NPC(575, 300)
    tb5 = Textbox(tbx(npc2), tby(npc2), 450, WALK, "", "Hey! Haven't heard from you for ages?")
    tb6 = Textbox(tbx(npc2), tby(npc2), 450, BLOCK, "", "Do you want go out somewhere soon?")
    tb10 = Textbox(tbx(npc2), tby(npc2), 450, WALK, "", "Hey! Haven't heard from you for ages?")
    tb11 = Textbox(tbx(npc2), tby(npc2), 450, BLOCK, "", "Do you want go out somewhere soon?")
    npc2.give_textboxes([tb5,tb6,tb10,tb11])

    npc3 = NPC(850,300)
    tb7 = Textbox(tbx(npc3), tby(npc3), 450, BLOCK, "", "Do you want go out somewhere soon?")
    tb8 = Textbox(tbx(npc3), tby(npc3), 450, BLOCK, "", "Do you want go out somewhere soon?")
    tb9 = Textbox(tbx(npc3), tby(npc3), 450, WALK, "", "Hey! Haven't heard from you for ages?")
    npc3.give_textboxes([tb7,tb8,tb9])

    npc1.hasSpokenOnce = 2
    npc2.hasSpokenOnce = 2
    npc3.hasSpokenOnce = 2

    door = Door(0,170,0,FACINGLEFT)

    room.addobjs([npc1,npc2,npc3,door])
    room.addwalls([
        pg.Rect(110,0,980,400),
        pg.Rect(0,335,110,65),
        pg.Rect(0,0,1200,100)
    ])

    return room

#beam travel and block
def make_room9():
    room = Room(1080, 170)

    haz1 = Hazard(5, 700, 265, 15)
    haz2 = Hazard(5, 500, 265, 15)
    haz3 = Hazard(5, 300, 265, 15)
    rec = Receiver(pg.Rect(600, 5, 50,50), pg.Rect(605,15,40,40), 50)
    rec.give_starton([haz2])
    rec.give_startoff([haz1, haz3])
    sht = BeamShooter(600,700,FACINGUP, [rec])

    npc1 = NPC(460,240)
    tb1 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "D", "Do you guys want to go to the park this week? :)")
    tb2 = Textbox(tbx(npc1), tby(npc1), 600, WALK, "D", "It would be nice to meet up in person again")
    tb3 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "D", "And also you can all pet my dog :)")
    npc1.give_textboxes([tb1,tb2,tb3])

    npc2 = NPC(740,240)
    tb4 = Textbox(tbx(npc2), tby(npc2), 450, BLOCK, "A", "Sounds good to me")
    npc2.give_textboxes([tb4])

    door = Door(95,750,0,FACINGDOWN)

    room.addobjs([haz2, sht, rec, npc1, npc2, door])

    room.addwalls([
        pg.Rect(400,150,300,50),
        pg.Rect(270,0,50,800)
    ])

    return room

#2 step to key with backtrack
def make_room10():
    room = Room(25, 500)

    key = Key(1050, 200)

    npc1 = NPC(280,450)
    tb1 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "K", "I'm gonna drive to the park")
    tb2 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "K", "If anyone needs a lift")
    npc1.give_textboxes([tb1,tb2])

    npc2 = NPC(680,300)
    tb3 = Textbox(tbx(npc2), tby(npc2), 400, BLOCK, "J", "Yes please if thats ok")
    tb4 = Textbox(tbx(npc2), tby(npc2), 400, WALK, "J", "Every warning light in my car is on lol")
    tb5 = Textbox(tbx(npc2), tby(npc2), 400, WALK, "J", "I think it's going to fall to pieces")
    npc2.give_textboxes([tb3,tb4,tb5])

    door = Door(0,170,1,FACINGLEFT)

    room.addobjs([key, npc1,door, npc2])

    room.addwalls([
        pg.Rect(400,0,50,800),
        pg.Rect(800,0,50,800)
    ])

    return room

#FINISH THIS key in textbox
def make_room11():
    room = Room(25, 400)

    key = Key(600, 300)
    key2 = Key(600, 350)

    npc1 = NPC(900,400)
    tb1 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "guy", "Hello pretty large and @ long")
    key3 = tb1.key
    npc1.give_textboxes([tb1])

    door = Door(0,170,2,FACINGLEFT)

    room.addobjs([key, key2, npc1,door, key3])

    return room

#simple switch-switch-switch to get past lasers
def make_room12():
    room = Room(25, 300)

    rec = Receiver(pg.Rect(800, 100, 50,50), pg.Rect(800,105,40,40), 25)
    haz1 = Hazard(170,600,10, 195)
    haz2 = Hazard(360,600,10, 195)
    haz3 = Hazard(550,600,10, 195)
    haz4 = Hazard(740,600,10, 195)
    haz5 = Hazard(930,600,10, 195)
    haz6 = Hazard(1120,600,10, 195)
    rec.give_starton([haz2, haz4, haz6])
    rec.give_startoff([haz1, haz3, haz5])
    sht = BeamShooter(350,100,FACINGRIGHT, [rec])

    npc1 = NPC(575,240)
    tb0 = Textbox(tbx(npc1), tby(npc1), 300, WALK, "D", "Hey, it's dana :)")
    tb1 = Textbox(tbx(npc1), tby(npc1), 350, WALK, "D", "You've not been responding to much aha")
    tb2 = Textbox(tbx(npc1), tby(npc1), 300, WALK, "D", "Did you want to meet up soon? :)")
    tb3 = Textbox(tbx(npc1), tby(npc1), 300, BLOCK, "D", "We could meet up for coffee?")
    tb4 = Textbox(tbx(npc1), tby(npc1), 300, WALK, "D", "Or go to a movie?")
    tb5 = Textbox(tbx(npc1), tby(npc1), 300, WALK, "D", "Or do badminton again?")
    tb6 = Textbox(tbx(npc1), tby(npc1), 300, BLOCK, "D", "Or just go to the park?")
    tb7 = Textbox(tbx(npc1), tby(npc1), 300, BLOCK, "D", "...")
    tb8 = Textbox(tbx(npc1), tby(npc1), 350, BLOCK, "D", "Anything, really")
    npc1.give_textboxes([tb0, tb1,tb2,tb3,tb4,tb5,tb6,tb7,tb8])

    door = Door(1150,650,0,FACINGRIGHT)

    room.addobjs([rec,sht,npc1, haz2, haz4, haz6, door])

    room.addwalls([
        pg.Rect(140,550,1060,50)
    ])

    return room

#its raining outside
def make_room13():
    room = Room(25, 450)

    rec1 = Receiver(pg.Rect(75, 675+15, 50,50), pg.Rect(80,675+15,40,40), 30)
    rec2 = Receiver(pg.Rect(325, 675, 50,50), pg.Rect(330,675,40,40), 30)
    rec3 = Receiver(pg.Rect(575, 675-25, 50,50), pg.Rect(580,675-25,40,40), 30)
    rec4 = Receiver(pg.Rect(825, 675, 50,50), pg.Rect(830,675,40,40), 30)
    rec5 = Receiver(pg.Rect(1075, 675+15, 50,50), pg.Rect(1080,675+15,40,40), 30)
    haz1 = Hazard(475,610,250, 5)
    rec1.give_startoff([haz1])
    haz2 = Hazard(475,615,250, 5)
    rec2.give_starton([haz2])
    haz3 = Hazard(475,620,250, 5)
    rec3.give_startoff([haz3])
    haz4 = Hazard(475,625,250, 5)
    rec4.give_startoff([haz4])
    haz5 = Hazard(475,630,250, 5)
    rec5.give_startoff([haz5])
    sht1 = BeamShooter(75,5,FACINGDOWN, [rec1])
    sht2 = BeamShooter(325,5,FACINGDOWN, [rec2])
    sht3 = BeamShooter(575,5,FACINGDOWN, [rec3])
    sht4 = BeamShooter(825,5,FACINGDOWN, [rec4])
    sht5 = BeamShooter(1075,5,FACINGDOWN, [rec5])

    npc1 = NPC(250,250)
    tb11 = Textbox(tbx(npc1), tby(npc1), 500, BLOCK, "", "It's raining outside")
    tb12 = Textbox(tbx(npc1), tby(npc1), 500, WALK, "", "Do ppl still want to go out?")
    tb13 = Textbox(tbx(npc1), tby(npc1), 500, BLOCK, "", "Feel like rescheduling?")
    tb14 = Textbox(tbx(npc1), tby(npc1), 500, WALK, "", "We could do tomorrow or I always have mondays free")
    tb15 = Textbox(tbx(npc1), tby(npc1), 500, BLOCK, "", "Why dont we move it")
    npc1.give_textboxes([tb11,tb12,tb13,tb14,tb15])

    npc2 = NPC(475,250)
    tb21 = Textbox(tbx(npc2), tby(npc2), 500, BLOCK, "", "It's raining outside.")
    tb22 = Textbox(tbx(npc2), tby(npc2), 500, WALK, "", "Do ppl still want to go out today?")
    tb23 = Textbox(tbx(npc2), tby(npc2), 550, BLOCK, "", "Feel like rescheduling?")
    tb24 = Textbox(tbx(npc2), tby(npc2), 530, WALK, "", "We could do tomorrow or I always have mondays free")
    tb25 = Textbox(tbx(npc2), tby(npc2), 500, BLOCK, "", "Why dont we move it")
    npc2.give_textboxes([tb21,tb22,tb23,tb24,tb25])

    npc3 = NPC(655,250)
    tb31 = Textbox(tbx(npc3), tby(npc3), 500, BLOCK, "", "It's raining outside")
    tb32 = Textbox(tbx(npc3), tby(npc3), 500, WALK, "", "Do ppl still want to go out?")
    tb33 = Textbox(tbx(npc3), tby(npc3), 550, BLOCK, "", "Feel like rescheduling?")
    tb34 = Textbox(tbx(npc3), tby(npc3), 500, WALK, "", "We could do tomorrow or I always have mondays free")
    tb35 = Textbox(tbx(npc3), tby(npc3), 500, BLOCK, "", "Why dont we move it")
    npc3.give_textboxes([tb31,tb32,tb33,tb34,tb35])

    npc4 = NPC(880,250)
    tb41 = Textbox(tbx(npc4), tby(npc4), 500, BLOCK, "", "It's raining outside")
    tb42 = Textbox(tbx(npc4), tby(npc4), 500, WALK, "", "Do ppl still want to go out?")
    tb43 = Textbox(tbx(npc4), tby(npc4), 500, BLOCK, "", "Feel like rescheduling?")
    tb44 = Textbox(tbx(npc4), tby(npc4), 500, WALK, "", "We could do tomorrow or I always have mondays free")
    tb45 = Textbox(tbx(npc4), tby(npc4), 500, BLOCK, "", "Why dont we move it")
    npc4.give_textboxes([tb41,tb42,tb43,tb44,tb45])

    door = Door(550,750,0,FACINGDOWN)

    npc1.no_count = True
    npc2.no_count = True
    npc3.no_count = True
    npc4.no_count = True

    room.addobjs([sht1,sht2,sht3,sht4,sht5, rec1,rec2,rec3,rec4,rec5,haz2,npc1,npc2,npc3,npc4,door])

    room.addwalls([
        pg.Rect(0,750,475,50), pg.Rect(725,750,475,50),
        pg.Rect(0,600,95,25), pg.Rect(105,600,240,25), pg.Rect(355,600,120,25),
        pg.Rect(0,625,50,125), pg.Rect(150,625,150,125), pg.Rect(400,625,75,125),
        pg.Rect(1105,600,95,25), pg.Rect(855,600,240,25), pg.Rect(725,600,120,25),
        pg.Rect(1150,625,50,125), pg.Rect(900,625,150,125), pg.Rect(725,625,75,125)
    ])

    return room

#4 keys behind lasers simple sol
def make_room14():
    room = Room(25, 380)

    rec1 = Receiver(pg.Rect(230, 50, 50,50), pg.Rect(230,55,40,40), 30)
    rec2 = Receiver(pg.Rect(430, 50, 50,50), pg.Rect(430,55,40,40), 30)
    rec3 = Receiver(pg.Rect(630, 50, 50,50), pg.Rect(630,55,40,40), 30)
    rec4 = Receiver(pg.Rect(830, 50, 50,50), pg.Rect(830,55,40,40), 30)
    haz1 = Hazard(205,580,100,10)
    haz2 = Hazard(405,580,100,10)
    haz3 = Hazard(605,580,100,10)
    haz4 = Hazard(805,580,100,10)
    rec1.give_starton([haz1])
    rec2.give_starton([haz2])
    rec3.give_starton([haz3])
    rec4.give_starton([haz4])
    sht = BeamShooter(5,50,FACINGRIGHT, [rec1,rec2,rec3,rec4])

    npc1 = NPC(275,200)
    #optional
    tb1 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "J", "Does anyone have photos from last year?")
    #optional
    tb2 = Textbox(tbx(npc1), tby(npc1), 250, WALK, "J", "The xmas party")
    tb3 = Textbox(tbx(npc1), tby(npc1), 300, BLOCK, "J", "lol")
    tb4 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "J", "I need one of me as santa")
    tb5 = Textbox(tbx(npc1), tby(npc1), 200, WALK, "J", "and elf amit lol")
    tb6 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "J", "We should do one again this year")
    tb7 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "J", "If all five of us can arrange a day")
    #optional
    tb8 = Textbox(tbx(npc1), tby(npc1), 200, WALK, "J", "maybe")
    npc1.give_textboxes([tb1,tb2,tb3,tb4,tb5,tb6,tb7,tb8])

    npc2 = NPC(580, 200)
    #tb14 = Textbox(tbx(npc2), tby(npc2), 200, WALK, "guy", "Small and tall")
    tb9 = Textbox(tbx(npc2), tby(npc2), 450, BLOCK, "D", "I thought I had some hmm")
    tb10 = Textbox(tbx(npc2), tby(npc2), 200, WALK, "D", "Let me check")
    tb11 = Textbox(tbx(npc2), tby(npc2), 300, BLOCK, "D", "...")
    tb12 = Textbox(tbx(npc2), tby(npc2), 500, WALK, "D", "None of you Joe but my brother will have some")
    tb13 = Textbox(tbx(npc2), tby(npc2), 500, BLOCK, "D", "And yeah we will do something this year for sure :)")
    npc2.give_textboxes([tb9, tb10, tb11,tb12,tb13])

    key1 = Key(248,675)
    key2 = Key(448,675)
    key3 = Key(648,675)
    key4 = Key(848,675)

    door = Door(1050,345,4,FACINGUP)

    room.addobjs([rec1,rec2,rec3,rec4,sht,npc1, npc2, haz1, haz2, haz3, haz4, key1, key2, key3, key4, door])

    room.addwalls([
        pg.Rect(0,125,1200,125),
        pg.Rect(0,575,205,220), pg.Rect(305,575,100,220), pg.Rect(505,575,100,220), pg.Rect(705,575,100,220), pg.Rect(905,575,295,220),
        pg.Rect(0,745,1200,50), pg.Rect(1000,250,200,100)
    ])

    return room
    

#ordered switches
def make_room15():
    room = Room(25, 380)

    rec1 = Receiver(pg.Rect(230, 50, 50,50), pg.Rect(230,55,40,40), 30)
    rec2 = Receiver(pg.Rect(430, 50, 50,50), pg.Rect(430,55,40,40), 30)
    rec3 = Receiver(pg.Rect(630, 50, 50,50), pg.Rect(630,55,40,40), 30)
    rec4 = Receiver(pg.Rect(830, 50, 50,50), pg.Rect(830,55,40,40), 30)
    haz1 = Hazard(930,610,220, 20)
    sht = BeamShooter(5,50,FACINGRIGHT, [rec1,rec2,rec3,rec4])

    lights = [Light(530,610,1), Light(630,610,2), Light(730,610,3), Light(830,610,4)]
    ol = OrderedLights([rec1,rec2,rec3,rec4], lights, [haz1])

    npc1 = NPC(275,200)
    #optional
    tb1 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "Does anyone have photos from last year?")
    #optional
    tb2 = Textbox(tbx(npc1), tby(npc1), 250, WALK, "", "The xmas party")
    tb3 = Textbox(tbx(npc1), tby(npc1), 300, BLOCK, "", "lol")
    tb4 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "I need one of me as santa")
    tb5 = Textbox(tbx(npc1), tby(npc1), 200, WALK, "", "and elf amit lol")
    tb6 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "We should do one again this year")
    tb7 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "", "If all five of us can arrange a day")
    #optional
    tb8 = Textbox(tbx(npc1), tby(npc1), 200, WALK, "", "maybe")
    npc1.give_textboxes([tb1,tb2,tb3,tb4,tb5,tb6,tb7,tb8])

    npc2 = NPC(580, 200)
    #tb14 = Textbox(tbx(npc2), tby(npc2), 200, WALK, "guy", "Small and tall")
    tb9 = Textbox(tbx(npc2), tby(npc2), 450, BLOCK, "", "I thought I had some hmm")
    tb10 = Textbox(tbx(npc2), tby(npc2), 200, WALK, "", "Let me check")
    tb11 = Textbox(tbx(npc2), tby(npc2), 300, BLOCK, "", "...")
    tb12 = Textbox(tbx(npc2), tby(npc2), 500, WALK, "", "None of you Joe but my brother will have some")
    tb13 = Textbox(tbx(npc2), tby(npc2), 500, BLOCK, "", "And yeah we will do something this year for sure :)")
    npc2.give_textboxes([tb9, tb10, tb11,tb12,tb13])

    door = Door(990, 750, 0, FACINGDOWN)

    npc1.hasSpokenOnce = 2
    npc2.hasSpokenOnce = 2

    room.addobjs([rec1,rec2,rec3,rec4, ol, sht,npc1, npc2, haz1, door])

    room.addwalls([
        pg.Rect(0,125,1200,125),
        pg.Rect(0,600,930,200), pg.Rect(1150,600,50,200)
    ])

    return room

#up and across
def make_room16():
    room = Room(25, 620)

    npc1 = NPC(375,475)
    door = Door(SCRN_WIDTH-50, 620, 1, FACINGRIGHT)

    # tb1 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "guy", "Hi! Is this too small?")
    # tb2 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "guy", "Hi! This maybe is a bit bigger?")
    # tb3 = Textbox(tbx(npc1), tby(npc1), 800, WALK, "guy", "And then if we do quite a long one you can bridge the gap hopefully")
    # tb4 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "guy", "Did that work?")
    # tb5 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "guy", "And then if we do quite a long one you can bridge the gap hopefully")
    # tb6 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "guy", "Did that work?")
    # npc1.give_textboxes([tb1,tb2,tb3,tb4,tb5,tb6])

    tb1 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "Amit", "This is ridiculous")
    tb2 = Textbox(tbx(npc1), tby(npc1), 800, WALK, "Amit", "My bathroom locks with a real @ .")
    tb3 = Textbox(tbx(npc1), tby(npc1), 800, WALK, "Amit", "but because it's a bathroom door everything is warped beyond belief")
    tb4 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "Amit", "Every time I use it is like breaking into a bank vault")
    tb5 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "Amit", "i'm stood there like a geriatric locksmith shaking bc i need to pee so bad")
    tb6 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "Amit", "its hell")
    npc1.give_textboxes([tb1,tb2,tb3,tb4,tb5,tb6])

    npc2 = NPC(855,220)
    tb7 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Joey", "get a new @ lol")
    npc2.give_textboxes([tb7])

    key = Key(175,100)

    room.addobjs([npc1, npc2, door, key, tb7.key, tb2.key])

    room.addwalls([
        pg.Rect(650,0,75,800), pg.Rect(0,250,650,75), pg.Rect(820,0,380,210)
    ])

    return room

def make_room17():
    room = Room(25, 620)

    npc1 = NPC(600, 350)
    tb1 = Textbox(tbx(npc1), tby(npc1), 500, WALK, "guy", "I need a big textbox to let the bullets flow nice and lovely please")
    npc1.give_textboxes([tb1])

    rec = Receiver(pg.Rect(400, 745, 50,50), pg.Rect(405,745,40,40), 30)
    haz1 = Hazard(900, 100, 250, 10)
    haz2 = Hazard(900, 300, 250, 10)
    haz3 = Hazard(900, 500, 250, 10)
    rec.give_startoff([haz2])
    rec.give_starton([haz1, haz3])
    shoota = BeamShooter(400,50,FACINGDOWN, [rec])

    door = Door(975,0,0,FACINGUP)

    room.addwalls([
        pg.Rect(850, 0, 50, 600), pg.Rect(1150,0,50,600)
    ])
    room.addobjs([npc1, rec, shoota, haz1, haz3, door])
    
    return room

def make_room18():
    room = Room(1000,700)

    npc1 = NPC(575,675)
    #tb1 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "guy", "Small to start")
    tb2 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "Dana", "Happy birthday Kat!! Hope you have a great day today :)")
    tb3 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "Dana", "Sorry we can't celebrate in person but hopefully we can soon!!")
    npc1.give_textboxes([tb2,tb3])

    npc2 = NPC(822,465)
    tb21 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Kat", "Thanks guys I'm going to eat an entire childrens birthday cake including the candles")
    tb22 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Kat", "Oh and thanks you three for my present! Very kind and thoughtful I love it")
    tb23 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Kat", "On the other hand Amit I detest the pillow you decided to also send and will be burning it")
    tb24 = Textbox(tbx(npc2), tby(npc2), 700, WALK, "Kat", "Also are we still doing quiz this week? I have a family dinner on sat but can do sunday?")
    npc2.give_textboxes([tb21,tb22,tb23,tb24])

    npc3 = NPC(428, 300)
    tb31 = Textbox(tbx(npc3), tby(npc3), 400, WALK, "Joey", "Happy brithday Kat have a good one!")
    #i can
    tb32 = Textbox(tbx(npc3), tby(npc3), 500, WALK, "Joey", "*birthday* lol")
    tb33 = Textbox(tbx(npc3), tby(npc3), 500, WALK, "Joey", "Yeah we can change to sunday I'm sure thats fine")
    npc3.give_textboxes([tb31,tb32,tb33])

    npc4 = NPC(850, 200)
    #can add i can
    tb41 = Textbox(tbx(npc4), tby(npc4), 500, WALK, "Amit", "I hope it keeps you warm either way")
    npc4.give_textboxes([tb41])

    door = Door(1150,25, 0, FACINGRIGHT)

    room.addobjs([npc1,npc2, npc3, npc4, door])
    room.addwalls([
        pg.Rect(0,150,1200,500), pg.Rect(0,0,1000,150)
    ])

    return room

def make_room19():
    room = Room(25, 360)

    npc1 = NPC(590, 660)
    tb1 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "A", "A big walk is good for the soul")
    tb2 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "A", "Not our fault you have small legs")
    tb3 = Textbox(tbx(npc1), tby(npc1), 450, WALK, "A", "You will wake up with huge muscles")
    npc1.give_textboxes([tb1,tb2,tb3])

    npc2 = NPC(620, 200)
    tb6 = Textbox(tbx(npc2), tby(npc2), 630, 2, "D", "Ahaha sorry I set a pretty quick pace :)")
    tb5 = Textbox(tbx(npc2), tby(npc2), 630, BLOCK, "D", "I think maybe it didn't help that you also sprinted away from that swan aha")
    npc2.give_textboxes([tb6,tb5])

    npc3 = NPC(250, 350)
    tb7 = Textbox(tbx(npc3), tby(npc3), 350, WALK, "K", "Guys my legs hurt so much help me")
    tb8 = Textbox(tbx(npc3), tby(npc3), 500, WALK, "K", "Why did we do an entire loop of the park")
    npc3.give_textboxes([tb7, tb8])

    door = Door(SCRN_WIDTH-50, 180, 0, FACINGRIGHT)

    room.addobjs([npc1,npc2,npc3,door])
    room.addwalls([
        pg.Rect(825, 0, 50, 795), pg.Rect(450, 0, 50, 795)
    ])

    return room

def make_room20():
    room = Room(25, 360)

    npc1 = NPC(500, 400)
    tb1 = Textbox(tbx(npc1), tby(npc1), 700, WALK, "", "Hey, it's dana :)")
    tb2 = Textbox(tbx(npc1), tby(npc1), 700, BLOCK, "", "Contacts didn't transfer but this is my new number so lmk who you are and I'll add you!!")
    npc1.give_textboxes([tb1,tb2])

    haz = Hazard(583,600,10,195)
    rec = Receiver(pg.Rect(1145,230,50,50), pg.Rect(1145,235,40,40), 30)
    rec.give_starton([haz])
    sht = BeamShooter(5,230,FACINGRIGHT,[rec])

    door = Door(1150,650,0,FACINGRIGHT)

    room.addobjs([npc1, sht, door, haz, rec])

    room.addwalls([
        pg.Rect(575,0,25,600), pg.Rect(600,550,600,50)
    ])

    return room

def make_room21():
    room = Room(25,650)

    npc1 = NPC(150,300)
    npc4 = NPC(750,325)
    npc5 = NPC(950,390)
    npc6 = NPC(435, 445)

    tb = Textbox(tbx(npc4), tby(npc4), 300, WALK, "", "are we still using this gc?")
    npc4.give_textboxes([tb])

    door = Door(1150,50,0,FACINGRIGHT)

    npc1.no_count = True
    npc5.no_count = True
    npc6.no_count = True
    npc4.no_count = True

    room.addwalls([pg.Rect(0,200,1200,75)])

    room.addobjs([npc1,npc4,npc5,npc6,door])

    return room

def make_room22():
    room = UpdatedRoom(25,50)
    room.wantsanimation = True

    npc1 = NPC(415,200)
    npc2 = NPC(700,375)
    npc3 = NPC(1000,440)
    npc4 = NPC(375,690)

    key = Key(100,715)
    door = Door(1050,0,1,FACINGUP)

    npc1.no_count = True
    npc2.no_count = True
    npc3.no_count = True
    npc4.no_count = True

    room.addobjs([npc1,npc2,npc3,npc4,key,door])

    room.addwalls([
        pg.Rect(0,500,280,25), pg.Rect(255,525,25,275),
        pg.Rect(550,0,25,300), pg.Rect(550,275,650,25)
    ])

    return room

def make_room23():
    room = UpdatedRoom(1060,710)

    npc1 = NPC(185,685)
    tb0 = Textbox(tbx(npc1), tby(npc1), 400, BLOCK, "", "...")
    tb05 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "", "Hello?")
    tb1 = Textbox(tbx(npc1), tby(npc1), 400, WALK, "", "Are you still there?")
    npc1.give_textboxes([tb0,tb1])

    npc2 = NPC(970,515)
    npc3 = NPC(450,165)
    npc4 = NPC(585,640)

    npc1.no_count = True
    npc2.no_count = True
    npc3.no_count = True
    npc4.no_count = True

    key = Key(150,250)
    door = Door(750,0,3,FACINGUP)

    room.addobjs([npc1, npc2, npc3, npc4, key, door])

    room.addwalls([
        pg.Rect(300,0,50,795), pg.Rect(350,745,600,50), pg.Rect(900,200,50,545), pg.Rect(600, 200, 300, 50), pg.Rect(600, 0, 50, 200)
    ])

    return room

def make_room24():
    room = Room(25,650)

    npc1 = NPC(495,295)
    npc2 = NPC(200,400)

    tb1 = Textbox(tbx(npc1), tby(npc1), 600, BLOCK, "K", "Guys I've locked myself out of my house")
    tb2 = Textbox(tbx(npc1), tby(npc1), 600, BLOCK, "K", "I'm in me pyjamas I look like I've escaped the ward")
    tb13 = Textbox(tbx(npc1), tby(npc1), 650, BLOCK, "K", "Gonna freeze to death now ok I'll miss you all")
    tb14 = Textbox(tbx(npc1), tby(npc1), 430, BLOCK, "K", "I can see my @ on the table inside fml")
    npc1.give_textboxes([tb1,tb2,tb13,tb14])

    tb3 = Textbox(tbx(npc2), tby(npc2), 400, WALK, "J", "ahahaha")
    tb4 = Textbox(tbx(npc2), tby(npc2), 400, WALK, "J", "Do you want me to come over and give u a leg up to a window or smth lmao")
    key2 = tb14.key
    npc2.give_textboxes([tb3,tb4])

    key1 = Key(893,260)

    door = Door(850,445,1,FACINGUP)

    x= 725
    y = 100
    l = 350
    room.addwalls([
        pg.Rect(x,y,l,25),pg.Rect(x,y,25,l),pg.Rect(x+l-25,y,25,l),pg.Rect(x,y+l-25,l,25)
    ])

    room.addobjs([npc1,npc2,door,key2,key1])

    return room

def make_room25():
    room = UpdatedRoom(775,710)
    door = Door(550,0,0,FACINGUP)

    npc1 = NPC(830,500)
    tb1 = Textbox(tbx(npc1), tby(npc1), 600, BLOCK, "Amit", "Oh hey bro whats up")
    tb2 = Textbox(tbx(npc1) - 250, tby(npc1) + 125, 400, WALK, "Amit", "Come outside and hang out")
    npc1.give_textboxes([tb1,tb2])

    npc2 = NPC(320,500-270)
    tb3 = Textbox(tbx(npc2), tby(npc2), 600, BLOCK, "Joey", "Hi bddy!")
    tb4 = Textbox(tbx(npc2), tby(npc2), 600, BLOCK, "Joey", "*buddy* lol")
    tb5 = Textbox(tbx(npc2) + 165, tby(npc2) +125, 200, WALK, "Joey", "Come outside!")
    npc2.give_textboxes([tb3,tb4,tb5])

    npc3 = NPC(830, 500-270)
    tb6 = Textbox(tbx(npc3), tby(npc3), 600, BLOCK, "Kat", "Yo long time no see!")
    tb7 = Textbox(tbx(npc3) -165, tby(npc3) +125, 200, WALK, "Kat", "Come outside!")
    npc3.give_textboxes([tb6,tb7])

    npc4 = NPC(415,100)
    tb88 = Textbox(tbx(npc4), tby(npc4), 600, BLOCK, "Dana", "...")
    tb8 = Textbox(tbx(npc4), tby(npc4), 600, BLOCK, "Dana", "Welcome back")
    tb9 = Textbox(tbx(npc4), tby(npc4), 600, WALK, "Dana", "Come outside :)")
    npc4.give_textboxes([tb88, tb8,tb9])

    room.addobjs([door,npc1,npc2,npc3,npc4])
    room.addwalls([
        pg.Rect(800,600,400,50), pg.Rect(0,500,1200,100), pg.Rect(0,600,400,50),
        pg.Rect(1200-565,600-270,565,50), pg.Rect(0,500-270,1200,100), pg.Rect(0,600-270,565,50)
    ])
    return room

def start_screen():
    background1 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cover.png')) , (SCRN_WIDTH,SCRN_HEIGHT) )
    background2 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cover2.png')) , (SCRN_WIDTH,SCRN_HEIGHT) )
    background3 = pg.transform.scale( pg.image.load(os.path.join('assets', 'cover3.png')) , (SCRN_WIDTH,SCRN_HEIGHT) )


    playrect = pg.Rect(590 - playtext.get_width()//2, 425, playtext.get_width() + 15, playtext.get_height()//3 * 2)
    rect1 = pg.Rect(540 - playtext.get_width()//2, 375, playtext.get_width() + 115, playtext.get_height()//3 * 2 + 100)
    contrect = pg.Rect(590 - continuegame.get_width()//2, 575, continuegame.get_width() + 15, continuegame.get_height()//3 * 2)
    rect2 = pg.Rect(540 - continuegame.get_width()//2, 525, continuegame.get_width() + 115, continuegame.get_height()//3 * 2 +100)
    quitrect = pg.Rect(590 - quitgame.get_width()//2, 725, quitgame.get_width() + 15, quitgame.get_height()//3 * 2)
    rect3 = pg.Rect(540 - quitgame.get_width()//2, 675, quitgame.get_width() + 115, quitgame.get_height()//3 * 2 + 100)

    hl1 = pg.transform.scale( pg.image.load(os.path.join('assets', 'selecthighlight.png')) , (rect1.w,rect1.h) )
    hl2 = pg.transform.scale( pg.image.load(os.path.join('assets', 'selecthighlight.png')) , (rect2.w,rect2.h) )
    hl3 = pg.transform.scale( pg.image.load(os.path.join('assets', 'selecthighlight.png')) , (rect3.w,rect3.h) )

    run = True
    clock = pg.time.Clock()
    bgtimer = 0
    freq = 60

    while run:
        clock.tick(FPS)
        bgtimer = (bgtimer+1)%freq
        if(bgtimer < freq/3):
            WIN.blit(background1, (0,0))
        elif(bgtimer < 2*freq/3):
            WIN.blit(background2, (0,0))
        else:
            WIN.blit(background3, (0,0))

        if playrect.collidepoint(pg.mouse.get_pos()):
            WIN.blit(hl1, (rect1.x,rect1.y))
        if contrect.collidepoint(pg.mouse.get_pos()):
            WIN.blit(hl2, (rect2.x,rect2.y))
        if quitrect.collidepoint(pg.mouse.get_pos()):
            WIN.blit(hl3, (rect3.x,rect3.y))

        WIN.blit(playtext, (600 - playtext.get_width()//2, 400))
        WIN.blit(continuegame, (600 - continuegame.get_width()//2, 550))
        WIN.blit(quitgame, (600 - quitgame.get_width()//2, 700))

        for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    return -1000
                
                if event.type == pg.MOUSEBUTTONUP:
                    if playrect.collidepoint(pg.mouse.get_pos()):
                        return 0
                    if contrect.collidepoint(pg.mouse.get_pos()):
                        return 1
                    if quitrect.collidepoint(pg.mouse.get_pos()):
                        return -1000
                
        pg.display.update()
    


def testing_only_main(rm):
    
    runstate = 0
    while(runstate == 0):
        room = rm()
        runstate = room.run_room(0)
    pg.quit()


def main():
    # testing_only_main(make_room25)
    # return

    room_list = [make_room1, make_room2, make_room16, make_room3, make_room4, make_room5, make_room18, make_room6, make_room7, make_room12, make_room9, make_room14, make_room10, make_room19, make_room24, make_room7o5, make_room8, make_room15, make_room13, make_room20, make_room21, make_room22, make_room23, make_room25]
    i = start_screen()
    if(i == 1):
        try:
            f = open(os.path.join('assets', 'save.txt'))
        except Exception:
            i = 0
            pass
        else:
            i = int(f.readline())
            f.close()
    while(i >= 0):
        if i >= len(room_list):
            i = start_screen()
        else:
            room = room_list[i]()
            i += room.run_room(i)
        
    pg.quit()


if __name__ == "__main__":
    main()
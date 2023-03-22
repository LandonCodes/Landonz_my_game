#file created by landon zafiropoulo (test)

# import libray
import pygame as pg
import random
import os

from os import path
# import settings
from setting import *
from sprites import *
from random import randint
# from pg.sprite import Sprite
vec = pg.math.Vector2

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)


# init pg and create window
pg.init()
# starts or initalizes the sound mixer
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("my first game")
clock = pg.time.Clock() 

player_img = pg.image.load(path.join(img_folder, "bell-ar-man.png")).convert()

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
# defines player as player
player = Player(player_img)
invader = Mob()
invader.image.fill((0,0,255))
invader.vel = vec(randint (1,8), randint (8,10))

for i in range(0,10):
    m = Mob()
    m.vel = vec(randint (1,8), randint (8,10))
    all_sprites.add(m)
    enemies.add(m)

                 
# testSprite = Sprite()
# testSprite.image = pg.Surface((50,50))
# testSprite.image.fill(GREEN)
# testSprite.rect = testSprite.image.get_rect()
# testSprite.rect.center = (WIDTH / 2, HEIGHT / 2)
all_sprites.add(player)
all_sprites.add(invader)
# all_sprites.add(testSprite)

# game loop

while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
            # break
    # print(get_mouse_now())
    all_sprites.update()

    blocks_hit_list = pg.sprite.spritecollide(player, enemies, False)
    for block in blocks_hit_list:
        print(enemies)
        pass
    # draw and render section of game loop
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # double buffering draws frames for entire screen
    pg.display.flip()
    # pg.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()
#file created by landon zafiropoulo

import pygame as pg

from pygame.sprite import Sprite

from setting import *

vec = pg.math.Vector2

# create a player

class Player(Sprite):
    def __init__(self, image_file):
        Sprite.__init__(self)
        self.image_file = image_file
        self.image=pg.surface.scale(image_file, (50, 38))
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(5,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def behavior(self):
        #going to add velocity to it
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y > HEIGHT or self.rect.y < 0:
            self.vel.y *= -1
    

    def update(self):
        self.behavior()
        self.pos += self.vel
        self.rect.center = self.pos

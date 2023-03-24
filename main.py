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
class Game:
    def __int__(self):
        pg.init()
        pg.mixer.init()
        self.scree = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("MY GAME")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for i in range(1,10):
            e = Mob()
            self.all_sprites.add(e)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    # def get_mouse_now():
    #     x,y = pg.mouse.get_pos()
    #     return (x,y)
    def update(self):
        self.all_sprites.update()
    def draw(self):
        self.screen.fill(BLUE)
        self.draw_text("Hello there!", 42, WHITE, WIDTH/2, HEIGHT/10)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

vec = pg.math.Vector2

# game loop

g = Game()

while g.running:
    g.new()

pg.quit()
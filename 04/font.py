# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

sys_fonts = pygame.font.get_fonts()
num_of_fonts = len(sys_fonts)
font = pygame.font.SysFont("SimHei", 40)
text_surface = font.render("你好", True, (0, 255, 255))

idx_font = 0
x = (640 - text_surface.get_width())/2
y = (480 - text_surface.get_height())/2


background = pygame.image.load("../resources/bg_black_01.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 0.6
    if x < -text_surface.get_width():
        idx_font = (idx_font + 1) % num_of_fonts
        text = '你好 - %s' % sys_fonts[idx_font]
        font = pygame.font.SysFont(sys_fonts[idx_font], randint(50, 70))
        text_surface = font.render(text, True, (randint(0, 255), randint(0, 255), randint(0, 255)))
        x = 640 - text_surface.get_width()
        y = (480 - text_surface.get_height())/2
        
    screen.blit(text_surface, (x, y))

    pygame.display.update()
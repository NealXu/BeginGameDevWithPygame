# -*- coding: utf-8 -*-


import pygame
from pygame.locals import QUIT
from sys import exit

bg_img_file = '../resources/bg_black_01.png'
mouse_file = '../resources/mouse.png'

# initialized pygame to prepare to access hardwares
pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Hello World!")

background = pygame.image.load(bg_img_file).convert()
mouse_cursor = pygame.image.load(mouse_file).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background, (0, 0))
    
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    
    screen.blit(mouse_cursor, (x, y))
    
    pygame.display.update()

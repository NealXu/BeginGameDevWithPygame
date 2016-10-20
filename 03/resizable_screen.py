# -*- coding: utf-8 -*-

import pygame
from sys import exit
from pygame.constants import QUIT, VIDEORESIZE, RESIZABLE, HWSURFACE

bg_file = '../resources/slam_dunk_02.png'

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | RESIZABLE, 32)
back_ground = pygame.image.load(bg_file).convert()

while True:
    
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
        
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to " + str(event.size))
    
    screen_width, screen_height=SCREEN_SIZE

    for y in range(0, screen_height, back_ground.get_height()):
        for x in range(0, screen_width, back_ground.get_width()):
            screen.blit(back_ground, (x, y))
            
    pygame.display.update()
    
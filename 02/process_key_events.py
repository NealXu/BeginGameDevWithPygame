# -*- coding: utf-8 -*-

import pygame
from sys import exit
from pygame.constants import QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

bg_file = '../resources/slam_dunk_01.jpg'

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
back_ground = pygame.image.load(bg_file).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
    
    x += move_x
    y += move_y
    
    screen.fill((0,0,0))
    screen.blit(back_ground, (x, y))
    pygame.display.update()
            
                
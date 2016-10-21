# -*- coding: utf-8 -*-

import pygame

pygame.init()

fonts = pygame.font.get_fonts()
for font in sorted(fonts):
    print(font)
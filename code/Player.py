#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.key
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDGHT
from code.Entity import Entity


class Player(Entity):

    def __init__(self,name:str, position: tuple):
        super().__init__(name, position)

    def move(self):

        pressed_key=pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top>0:
            self.rect.centery -= ENTITY_SPEED[self.name]
            self.rect.centery -= 1
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
            self.rect.centery +=1
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDGHT:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.rect.centerx +=1
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.rect.centerx -=1
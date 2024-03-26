#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

    def run(self, ):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play()
        pygame.mixer_music.set_volume(1)
        while True:
            clock.tick(75)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
        pass


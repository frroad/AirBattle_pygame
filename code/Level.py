#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface

from code.Const import MENU_OPTION, EVENT_ENEMY, C_GREEN, C_RED
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 3000)

    def run(self, ):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play()
        pygame.mixer_music.set_volume(1)
        while True:
            # limitar fps do game
            clock.tick(75)

            # atualizar tela
            pygame.display.flip()

            # Verificar relacionamento de entidades
            EntityMediator.verif_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # for para desenhar todas entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(15, f'Player1 - Health:{ent.health} | Score: {ent.score}', C_GREEN, (10, 10))
                if ent.name == 'Player2':
                    self.level_text(15, f'Player2 - Health:{ent.health} | Score: {ent.score}', C_RED, (10, 30))

            # Conferir eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font = pygame.font.SysFont(None, text_size)
        text_surface = font.render(text, True, text_color)
        self.window.blit(text_surface, text_pos)

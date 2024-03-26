#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDGHT, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=tuple):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDGHT, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10,WIN_HEIGHT/2-30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2+30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDGHT+20, random.randint(0 +40, WIN_HEIGHT-60)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDGHT +10, random.randint(0 +40, WIN_HEIGHT-80)))
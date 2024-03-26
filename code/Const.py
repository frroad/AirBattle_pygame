import pygame

WIN_WIDGHT = 576
WIN_HEIGHT = 324

COLOR_BLUE = (135, 206, 250)
COLOR_WHITE = (255, 255, 255)
COLOR_DARKYELLOW = (255, 140, 0)

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

ENTITY_SPEED = {'Level1Bg0':0,
                'Level1Bg1':1,
                'Level1Bg2':2,
                'Player1':3,
                'Player2':3,
                'Enemy1':2,
                'Enemy2':3,
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}


EVENT_ENEMY =pygame.USEREVENT+1

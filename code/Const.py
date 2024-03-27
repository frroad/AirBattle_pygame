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
                'Player1':2,
                'Player2':2,
                'Enemy1':2,
                'Enemy2':3,
                'Player1Shot':4,
                'Player2Shot':2,
                'Enemy1Shot':4,
                'Enemy2Shot':5,
                }

ENTITY_SHOT_DELAY={'Player1':20,
                   'Player2':30,
                   'Enemy1':60,
                   'Enemy2':70}

ENTITY_HEALTH= {'Level1Bg0':999,
                'Level1Bg1':999,
                'Level1Bg2':999,
                'Player1':300,
                'Player2':300,
                'Enemy1':200,
                'Enemy2':200,
                'Player1Shot':1,
                'Player2Shot':1,
                'Enemy1Shot':3,
                'Enemy2Shot':3,
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1':pygame.K_p,
                    'Player2':pygame.K_SPACE}


EVENT_ENEMY =pygame.USEREVENT+1

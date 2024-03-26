#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDGHT, COLOR_BLUE, MENU_OPTION, COLOR_WHITE, COLOR_DARKYELLOW


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/menuMusic.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.1)
        menu_option=0

        while (True):
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "AIR BATTLE", COLOR_BLUE, (WIN_WIDGHT / 2, 70))
            self.menu_text(50, "SHOTTER GAME", COLOR_BLUE, (WIN_WIDGHT / 2, 120))



            for i in range(len(MENU_OPTION)):
               if i == menu_option:
                self.menu_text(20, MENU_OPTION[i], COLOR_DARKYELLOW, (WIN_WIDGHT / 2, 200 + 30 * i))
               else:
                 self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDGHT / 2, 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option > len(MENU_OPTION)-1:
                            menu_option =0
                    if event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = 3
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lacida Sans Typewriter", size=text_size)

        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

import pygame as pg
from pydoom import PyDoom
from render_manager import *
from globals import FONT, SCREEN_WIDTH, SCREEN_HEIGHT, MENU_SPACING


class Menu(PyDoom):
    def __init__(self):
        super().__init__()
        self.active = 0
        self.options = ["New Game", "Options", "Exit"]
        self.font = pg.font.Font(FONT, 30)

    def draw(self, surface, clock=None):
        for o in self.options:
            color = pg.Color("Dark grey")
            if self.options.index(o) == self.active:
                color = pg.Color("Light grey")
            text = self.font.render(o, True, color)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH / 2,
                                SCREEN_HEIGHT / 2 - (len(self.options) * MENU_SPACING / 2) + MENU_SPACING * self.options.index(o))
            surface.blit(text, text_rect)

    def change_active(self, move):
        if 0 <= self.active + move <= len(self.options) - 1:
            self.active += move

    def event(self, event, event_timer=0.0):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_UP):
                self.change_active(-1)
            elif event.key in (pg.K_s, pg.K_DOWN):
                self.change_active(1)
            if event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 0:
                return 1  # Whoa look how bad this is


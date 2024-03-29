import pygame as pg

from PyDoom.globals import FONT, SCREEN_WIDTH, SCREEN_HEIGHT, MENU_SPACING, \
    MENU_OPTIONS_MAIN, MENU_OPTIONS_OPTION, SCREEN_MENU, SCREEN_OPTIONS
from PyDoom.imageutilities import get_image
from PyDoom.pydoom import PyDoom


class Menu(PyDoom):
    def __init__(self, menu_type):
        super().__init__()
        self.active = 0
        if menu_type == "Main":
            self.options = MENU_OPTIONS_MAIN
        elif menu_type == "Options":
            self.options = MENU_OPTIONS_OPTION
        self.font = pg.font.Font(FONT, 30)
        self.main_image = get_image("MainLogo.png")

    def draw(self, surface):
        surface.blit(self.main_image, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        for option in self.options:
            color = pg.Color("Dark grey")
            if self.options.index(option) == self.active:
                color = pg.Color("Light grey")
            text = self.font.render(option, True, color)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH / 2,
                                SCREEN_HEIGHT * 0.60 - (len(self.options) * MENU_SPACING / 2)
                                + MENU_SPACING * self.options.index(option))
            surface.blit(text, text_rect)

    def change_active(self, move):
        if 0 <= self.active + move <= len(self.options) - 1:
            self.active += move

    def event(self, event, pydoomobj=None):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_UP):
                self.change_active(-1)
            elif event.key in (pg.K_s, pg.K_DOWN):
                self.change_active(1)
            if pydoomobj.active is SCREEN_MENU:
                if event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 0 and pydoomobj:
                    pydoomobj.change_to_game()
                elif event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 1 and pydoomobj:
                    pydoomobj.change_to_options()
                elif event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 2 and pydoomobj:
                    pg.event.post(pg.event.Event(pg.QUIT))
            elif pydoomobj.active is SCREEN_OPTIONS:
                if event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 0 and pydoomobj:
                    pass  # Change graphics resolution
                elif event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 1 and pydoomobj:
                    pass  # Change volume level
                elif event.key in (pg.K_SPACE, pg.K_RETURN) and self.active == 2 and pydoomobj:
                    pydoomobj.change_to_menu()



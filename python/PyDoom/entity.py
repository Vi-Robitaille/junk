import pygame as pg

from math import pi, cos, sin
from globals import PLAYER_TEAM, LEVEL_SIZE


class Entity:
    def __init__(self, pos, sprite, team, game):
        # This entity's position
        self.pos = pos
        # This entity's facing angle
        self.angle = pi / 2

        # The players FOV
        self.fov = pi / 4

        # This entity's sprite (Image Utilities are not implemented yet)
        #self.sprite = iu.images[sprite]
        self.team = team

        # local variable for time between things
        self.tick = 0.0

        self.dead = False

        self.game = game

        # List for W, A, S, D
        self.wasd_held = [False, False, False, False]
        #
        self.health = 100

    def update(self):
        if self.health < 0:
            self.dead = True
        self.move()

    def do_damage(self, target, amount):
        pass

    def take_damage(self, amount):
        pass

    def move(self):
        pass

    def event(self, event, timer):
        self.tick = timer

    def move_check(self, pos):
        return False if self.game.level.map[int(pos[0] * LEVEL_SIZE + pos[1])] == "#" else True


class Player(Entity):
    def __init__(self, game):
        super().__init__(pos=(3.0, 3.0), sprite=None, team=PLAYER_TEAM, game=game)

    def do_damage(self, target, amount):
        pass

    def damage(self):
        pass

    def move(self):
        if self.wasd_held[0]:
            tmp_pos = (self.pos[0] + (sin(self.angle) * 1.0 * self.tick),
                       self.pos[1] + (cos(self.angle) * 1.0 * self.tick))
            self.pos = tmp_pos if self.move_check(tmp_pos) else self.pos
        if self.wasd_held[1]:
            self.angle -= 1.0 * self.tick
        if self.wasd_held[2]:
            tmp_pos = (self.pos[0] - (sin(self.angle) * 1.0 * self.tick),
                       self.pos[1] - (cos(self.angle) * 1.0 * self.tick))
            self.move_check(tmp_pos)
            self.pos = tmp_pos if self.move_check(tmp_pos) else self.pos
        if self.wasd_held[3]:
            self.angle += 1.0 * self.tick

    def event(self, event, timer):
        super().event(event, timer)
        if event.type in (pg.KEYDOWN, pg.KEYUP):
            if event.key == pg.K_w:
                self.wasd_held[0] = not self.wasd_held[0]
            if event.key == pg.K_a:
                self.wasd_held[1] = not self.wasd_held[1]
            if event.key == pg.K_s:
                self.wasd_held[2] = not self.wasd_held[2]
            if event.key == pg.K_d:
                self.wasd_held[3] = not self.wasd_held[3]

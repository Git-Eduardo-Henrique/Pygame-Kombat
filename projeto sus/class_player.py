import pygame as pg
from os import getcwd


class Player:
    def __init__(self):
        # files
        self.diretorio = getcwd()
        # images
        self.imposter_sprite = pg.image.load(f'{self.diretorio}\\images\\ciano.png')
        # pos
        self.x_imposter = 250
        self.y_imposter = 250
        # others
        self.flip = False

    def flip_sprite(self):
        pg.transform.flip(self.imposter_sprite, True, False)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y_imposter -= 1
        if keys[pg.K_s]:
            self.y_imposter += 1

        if keys[pg.K_a]:
            self.x_imposter -= 1
            if self.flip:
                pass
            else:
                # pg.transform.flip(self.imposter_sprite, True, False)
                self.flip = True

        if keys[pg.K_d]:
            self.x_imposter += 1
            if self.flip:
                # pg.transform.flip(self.imposter_sprite, True, False)
                self.flip = False
            else:
                pass

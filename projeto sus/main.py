from class_player import Player

import pygame as pg
from random import randint
from os import getcwd
from sys import exit

pg.init()
pg.mixer.init()

diretorio = getcwd()  # remover dps
# classe
player = Player()
# images
roxo_sprite = pg.image.load(f'{diretorio}\\images\\roxo.png')
roxo_body_sprite = pg.image.load(f'{diretorio}\\images\\body_roxo.png')
icon = pg.image.load(f'{diretorio}\\images\\icone.png')

resolution = [1280, 720]
window = pg.display.set_mode((resolution[0], resolution[1]))
fundo = pg.Color(128, 128, 128)
font = pg.font.SysFont('arial.ttf', 50)
x_roxo = randint(10, resolution[0] - 60)
y_roxo = randint(10, resolution[1] - 60)

pg.display.set_caption('THE FINAL SUS AMONGUS CRAFT NITE THE DEFINETIVE EDITON PRO MAX 11')
pg.display.set_icon(icon)

death_sound = pg.mixer.Sound(f'{diretorio}\\sounds\\death.wav')

points = 0


while True:
    timer = (pg.time.get_ticks()) / 1000
    window.fill(fundo)

    text_points = font.render(f'Points: {points}', True, (255, 255, 255), fundo)
    text_timer = font.render(f'Timer: {10 - timer:.0f}', True, (255, 255, 255), fundo)
    window.blit(text_points, (1000, 50))
    window.blit(text_timer, (1000, 100))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    player.move()

    cian = window.blit(player.imposter_sprite, (player.x_imposter, player.y_imposter))
    roxo = window.blit(roxo_sprite, (x_roxo, y_roxo))

    if cian.colliderect(roxo):
        x_roxo = randint(10, resolution[0] - 60)
        y_roxo = randint(10, resolution[1] - 60)

        pg.mixer.Sound.play(death_sound)
        points += 1

    # if timer > 1000:
        # pg.quit()
        # exit()
    pg.display.flip()

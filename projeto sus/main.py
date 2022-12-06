import pygame as pg
from random import randint
pg.init()
pg.mixer.init()
# images
ciano_sprite = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\ciano.png')
roxo_sprite = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\roxo.png')
roxo_body_sprite = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\body_roxo.png')
icon = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\icone.png')

# window config
resolution = [1280, 720]
x_ciano = 250
y_ciano = 250
x_roxo = randint(10, resolution[0]-60)
y_roxo = randint(10, resolution[1]-60)
virou = False

window = pg.display.set_mode((resolution[0], resolution[1]))
pg.display.set_caption('SUS')
pg.display.set_icon(icon)

fundo = pg.Color(128, 128, 128)
# sounds
death_sound = pg.mixer.Sound('C:\\Users\\887382\\Downloads\\projeto sus\\sounds\\death.mp3')

# textos
font = pg.font.SysFont('arial.ttf', 50)

# vars
points = 0
life = True

while True:
    window.fill(fundo)
    text_points = font.render(f'Points: {points}', True, (255, 255, 255), fundo)
    window.blit(text_points, (1000, 50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                y_ciano -= 45
            if event.key == pg.K_s:
                y_ciano += 45

            if event.key == pg.K_a:
                x_ciano -= 45
                if virou:
                    pass
                else:
                    ciano_sprite = pg.transform.flip(ciano_sprite, True, False)
                    virou = True

            if event.key == pg.K_d:
                x_ciano += 45
                if virou:
                    ciano_sprite = pg.transform.flip(ciano_sprite, True, False)
                    virou = False
                else:
                    pass

    ciano = window.blit(ciano_sprite, (x_ciano, y_ciano))
    roxo = window.blit(roxo_sprite, (x_roxo, y_roxo))

    if ciano.colliderect(roxo):
            x_roxo_body = x_roxo
            y_roxo_body = y_roxo
            window.blit(roxo_body_sprite, (x_roxo_body, y_roxo_body))
            x_roxo = randint(10, resolution[0] - 60)
            y_roxo = randint(10, resolution[1] - 60)

            pg.mixer.Sound.play(death_sound)

            points += 1
            life = False

    pg.display.flip()

import pygame as pg
# images
ciano = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\ciano.png')
roxo = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\roxo.png')
icon = pg.image.load('C:\\Users\\887382\\Downloads\\projeto sus\\images\\icone.png')

# window config
resolution = [1280, 720]
x_ciano = 250
y_ciano = 250
virou = False

window = pg.display.set_mode((resolution[0], resolution[1]))
pg.display.set_caption('SUS')
pg.display.set_icon(icon)

fundo = pg.Color(128, 128, 128)

while True:
    window.fill(fundo)
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
                    ciano = pg.transform.flip(ciano, True, False)
                    virou = True

            if event.key == pg.K_d:
                x_ciano += 45
                if virou:
                    ciano = pg.transform.flip(ciano, True, False)
                    virou = False
                else:
                    pass

    window.blit(ciano, (x_ciano, y_ciano))
    window.blit(roxo, (250, 0))

    pg.display.flip()


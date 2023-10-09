# modulos normais
import pygame
from os import getcwd

# modulos de classes do game
from menu import menu
from fight.fight import Fight

# iniciar pygame
pygame.init()

# guarda o diretorio onde o jogo foi salvo
diretorio = getcwd() 

# configurações da tela
screen_resolution = [1080, 480]
screen = pygame.display.set_mode((screen_resolution[0], screen_resolution[1]))

# define o icone e nome da janela
icon = pygame.image.load(f"{diretorio}\\pygame-kombat\\midias\\images\\icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Pygame Kombat")

# variavel para definir o fps
clock = pygame.time.Clock()  

# objetos
menu = menu(
    screen=screen,
    screen_width=screen_resolution[0],
    screen_height=screen_resolution[1]
)

fight = Fight(
    screen=screen,
    screen_width=screen_resolution[0],
    screen_height=screen_resolution[1]
)

running = True
while running:
    clock.tick(60)  # define o fps do jogo para 60

    if menu.running:  # se o player estiver no menu
        menu.menu_start()
    else:  # se o player for para a luta
        fight.fight_start()

    pygame.display.update()

pygame.quit()
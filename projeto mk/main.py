import pygame
from os import getcwd

from menu import menu
from fight import Fight

pygame.init()

screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

diretorio = getcwd()
icon = pygame.image.load(f"{diretorio}\\images\\icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Pygame Kombat")

# Loop principal do jogo
clock = pygame.time.Clock()

menu = menu()
fight = Fight(
    screen=screen,
    screen_width=screen_width,
    screen_height=screen_height
)

running = True
while running:
    clock.tick(60)
    if menu.running:
        menu.menu_start(screen=screen)
    else:
        fight.fight_start()

    pygame.display.update()

pygame.quit()

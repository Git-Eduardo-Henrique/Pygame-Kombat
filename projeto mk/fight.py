import pygame
from os import getcwd

from menu import menu
from scorpion import scorpion
from sub_zero import sub_zero
from fight_hud import FightHud

# Inicializar o pygame
pygame.init()
diretorio = getcwd()

# Definir as dimensões da tela
screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load(f"{diretorio}\\images\\stage.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Definir a fonte para mostrar as vidas
final_font = pygame.font.Font(None, 100)

# Loop principal do jogo
clock = pygame.time.Clock()
# vidas
max_life = 1000
player1_life = max_life
player2_life = max_life

scorpion = scorpion(
    screen_height=screen_height)

sub_zero = sub_zero(
    screen_height=screen_height,
    screen_width=screen_width)

menu = menu()

FightHud = FightHud(
    screen=screen
)
running = True
while running:
    clock.tick(60)
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    FightHud.in_fight(
        player1_life=player1_life,
        player2_life=player2_life,
        max_life=max_life
    )

    sub_zero.update(screen=screen)
    sub_zero.move()

    scorpion.events(
        screen=screen
    )

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_l]:
        player1_life -= 10
    elif pressed_keys[pygame.K_p]:
        player2_life -= 10

    if player1_life <= 0 or player2_life <= 0:
        game_over_text = final_font.render("finish him", True, (255, 255, 255))
        screen.blit(game_over_text, (
            screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()

import pygame
from os import getcwd
from scorpion import scorpion
from sub_zero import sub_zero

# Inicializar o pygame
pygame.init()
diretorio = getcwd()

# Definir as dimensões da tela
screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load(f"{diretorio}\\images\\stage.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Definir as vidas iniciais dos personagens
max_life = 1000
player1_life = max_life
player2_life = max_life

# Definir a fonte para mostrar as vidas
life_font = pygame.font.Font(None, 30)
final_font = pygame.font.Font(None, 100)

# Loop principal do jogo
clock = pygame.time.Clock()
running = True

# Definir a cor da barra de vida
health_color = (0, 255, 0)
demage_color = (255, 0, 0)

# Definir a posição e dimensões da barra de vida
health_rect = pygame.Rect(10, 25, 440, 20)
health_rect_2 = pygame.Rect(550, 25, 440, 20)

scorpion = scorpion(screen_height=screen_height)
sub_zero = sub_zero(screen_height=screen_height, screen_width=screen_width)
while running:
    clock.tick(60)
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar entrada do teclado
    pressed_keys = pygame.key.get_pressed()

    sub_zero.update(screen=screen)
    sub_zero.move()

    scorpion.events(
        screen=screen,
        animation_normal=scorpion.scorpion_normal,
        animation_normal_reverse=scorpion.scorpion_normal_inv,
        animation_walking=scorpion.scorpion_walking,
        animation_walking_reverse=scorpion.scorpion_walking_inv
    )

    # Desenhar as vidas dos personagens na tela
    player2_life_text = life_font.render(f"Player 1: {str(player1_life)} Player 2: {str(player2_life)}", True, (255, 255, 255))
    screen.blit(player2_life_text, (10, 50))
    pygame.draw.rect(screen, demage_color, (health_rect.x, health_rect.y, health_rect.width, health_rect.height))
    pygame.draw.rect(screen, health_color,
                     (health_rect.x, health_rect.y, player1_life / max_life * health_rect.width, health_rect.height))

    pygame.draw.rect(screen, demage_color, (health_rect_2.x, health_rect_2.y, health_rect_2.width, health_rect_2.height))
    pygame.draw.rect(screen, health_color,
                     (health_rect_2.x, health_rect_2.y, player2_life / max_life * health_rect_2.width, health_rect_2.height))

    if pressed_keys[pygame.K_l]:
        player1_life -= 10
    elif pressed_keys[pygame.K_p]:
        player2_life -= 10

    # Verificar se algum personagem more
    if player1_life <= 0 or player2_life <= 0:
        game_over_text = final_font.render("finish him", True, (255, 255, 255))
        screen.blit(game_over_text, (
            screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()

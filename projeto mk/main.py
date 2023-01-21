import pygame
from os import getcwd
from scorpion import scorpion
from sub_zero import sub_zero

# Inicializar o pygame
pygame.init()
diretorio = getcwd()

# Definir as dimensões da tela
screen_width = 750
screen_height = 350
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load(f"{diretorio}\\images\\stage.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Definir as vidas iniciais dos personagens
player1_life = 100
player2_life = 100
max_life = 100

# Definir a fonte para mostrar as vidas
life_font = pygame.font.Font(None, 30)
final_font = pygame.font.Font(None, 100)

# Loop principal do jogo
clock = pygame.time.Clock()
running = True

# Definir a cor da barra de vida
health_color = (0, 255, 0)

# Definir a posição e dimensões da barra de vida
health_rect = pygame.Rect(10, 25, 350, 20)

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
    scorpion.update(screen=screen)
    scorpion.move()

    # Desenhar as vidas dos personagens na tela
    player2_life_text = life_font.render("Player 2: " + str(player2_life), True, (255, 255, 255))
    screen.blit(player2_life_text, (screen_width - 150, 50))
    pygame.draw.rect(screen, health_color, (health_rect.x, health_rect.y, player1_life/max_life * health_rect.width, health_rect.height))

    if pressed_keys[pygame.K_l]:
        player1_life -= 1
    elif pressed_keys[pygame.K_p]:
        player2_life -= 10

    # Verificar se algum personagem morreu
    if player1_life <= 0 or player2_life <= 0:
        game_over_text = final_font.render("finish him", True, (255, 255, 255))
        screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - game_over_text.get_height()/2))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()



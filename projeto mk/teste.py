import pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_width = 750
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load("stage.png")
background_image = pygame.transform.scale(background_image,
                                          (background_image.get_width()*2, background_image.get_height()*2))


# Carrega as imagens dos personagens
player_image = pygame.image.load("player.png")
player_x = 50
player_y = (screen_height - player_image.get_height())

enemy_image = pygame.image.load("enemy.gif")
enemy_x = screen_width - enemy_image.get_width() - 50
enemy_y = screen_height - enemy_image.get_height()

# Define a vida dos personagens
player_health = 100
enemy_health = 100
damage_radius = 50

# Define a fonte e o tamanho do texto
font = pygame.font.Font(None, 36)

# definir velocidade de queda do personagem
fall_speed = 0
speed = 3

# definir força do pulo
jump_strength = -20
in_air = False

running = True
while running:
    screen.blit(background_image, (-(screen_width / 2), 0))
    if enemy_health > 0:
        text = font.render(f"life: {enemy_health}", True, (255, 0, 0))
    else:
        text = font.render(f"finish him", True, (255, 0, 0))
    text_rect = text.get_rect()
    # Verifica os eventos do teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Verifica se a tecla clicada é a tecla espaço
            if event.key == pygame.K_g:
                distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
                if distance < damage_radius:
                    # Causa dano no inimigo
                    if enemy_health > 0:
                        enemy_health -= 10
                    else:
                        pass
            elif event.key == pygame.K_w:
                if not in_air:
                    fall_speed = jump_strength
                    in_air = True
                else:
                    in_air = False

        # checar estado do controle de jogo
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        # usando o primeiro controle conectado
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        # obter valores dos eixos do controle
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)
    elif joystick.get_button(0):
        if not in_air:
            fall_speed = jump_strength
            in_air = True
        else:
            in_air = False

            # mover personagem de acordo com os eixos
    player_x += x_axis * speed
    player_y += y_axis * speed
    # detectar tecla de pulo pressionada
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed
    # aplicar velocidade de queda a posição do personagem
    player_y += fall_speed

    if player_y >= (screen_height - player_image.get_height()):
        fall_speed = 0
        player_y = (screen_height - player_image.get_height())
    else:
        # aplicar gravidade
        fall_speed += 1

    # Desenha os personagens na tela
    screen.blit(text, (screen_width - 100, 10))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    pygame.display.flip()

pygame.quit()

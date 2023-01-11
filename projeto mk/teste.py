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
player_y = screen_height - player_image.get_height()

enemy_image = pygame.image.load("enemy.gif")
enemy_x = screen_width - enemy_image.get_width() - 50
enemy_y = screen_height - enemy_image.get_height()

# Define a vida dos personagens
player_health = 100
enemy_health = 100
damage_radius = 50

# Define a fonte e o tamanho do texto
font = pygame.font.Font(None, 36)

# Define o loop do jogo
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
            if event.key == pygame.K_a:
                distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
                if distance < damage_radius:
                    # Causa dano no inimigo
                    if enemy_health > 0:
                        enemy_health -= 10
                    else:
                        pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 0.5
    if keys[pygame.K_RIGHT]:
        player_x += 0.5

    # Atualiza a posição do inimigo
    enemy_x += 0.1
    if enemy_x > screen_width - enemy_image.get_width():
        enemy_x = screen_width - enemy_image.get_width()

    # Desenha os personagens na tela
    screen.blit(text, (screen_width - 100, 10))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    pygame.display.flip()

pygame.quit()


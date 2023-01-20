import pygame
from os import getcwd

# Inicializar o pygame
pygame.init()
diretorio = getcwd()

# Definir as dimensões da tela
screen_width = 750
screen_height = 350
screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load("stage.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Definir as vidas iniciais dos personagens
player1_life = 100
player2_life = 100

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

class scorpion:
    def __init__(self):
        self.scorpion_animation = []
        self.scorpion_animation_inv = []
        for i in range(1, 8):
            image = pygame.image.load(f"{diretorio}\\images\\scorpion\\scorpion_{i}.png")
            self.scorpion_animation.append(image)
            self.scorpion_animation_inv.append(pygame.transform.flip(image, True, False))

        self.scorpion_state = True
        self.animation_index = 0
        self.scorpion_x = 50
        self.scorpion_y = screen_height - self.scorpion_animation[0].get_height() - 25

    def update(self):
        if self.scorpion_state:
            self.animation_index += 0.15
            if self.animation_index >= len(self.scorpion_animation):
                self.animation_index = 0
            screen.blit(self.scorpion_animation[int(self.animation_index)], (self.scorpion_x, self.scorpion_y))
        else:
            self.animation_index += 0.15
            if self.animation_index >= len(self.scorpion_animation_inv):
                self.animation_index = 0
            screen.blit(self.scorpion_animation_inv[int(self.animation_index)], (self.scorpion_x, self.scorpion_y))

    def move(self):
        if pressed_keys[pygame.K_a]:
            self.scorpion_x -= 5
            self.scorpion_state = False
        if pressed_keys[pygame.K_d]:
            self.scorpion_x += 5
            self.scorpion_state = True


class sub_zero:
    def __init__(self):
        self.sub_zero_animation = []
        self.sub_zero_animation_inv = []
        for i in range(1, 11):
            image = pygame.image.load(f"{diretorio}\\images\\sub-zero\\sub_zero-{i}.png")
            self.sub_zero_animation.append(image)
            self.sub_zero_animation_inv.append(pygame.transform.flip(image, True, False))

        self.sub_zero_state = False
        self.animation_index = 0
        self.sub_zero_x = (screen_width - self.sub_zero_animation[0].get_width()) - 50
        self.sub_zero_y = screen_height - self.sub_zero_animation[0].get_height() - 25

    def update(self):
        if self.sub_zero_state:
            self.animation_index += 0.15
            if self.animation_index >= len(self.sub_zero_animation):
                self.animation_index = 0
            screen.blit(self.sub_zero_animation[int(self.animation_index)], (self.sub_zero_x, self.sub_zero_y))
        else:
            self.animation_index += 0.15
            if self.animation_index >= len(self.sub_zero_animation_inv):
                self.animation_index = 0
            screen.blit(self.sub_zero_animation_inv[int(self.animation_index)], (self.sub_zero_x, self.sub_zero_y))

    def move(self):
        if pressed_keys[pygame.K_LEFT]:
            self.sub_zero_x -= 5
            self.sub_zero_state = False
        if pressed_keys[pygame.K_RIGHT]:
            self.sub_zero_x += 5
            self.sub_zero_state = True


scorpion = scorpion()
sub_zero = sub_zero()
while running:
    clock.tick(60)
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar entrada do teclado
    pressed_keys = pygame.key.get_pressed()

    sub_zero.update()
    sub_zero.move()
    scorpion.update()
    scorpion.move()

    # Desenhar as vidas dos personagens na tela
    player1_life_text = life_font.render("Player 1: " + str(player1_life), True, (255, 255, 255))
    player2_life_text = life_font.render("Player 2: " + str(player2_life), True, (255, 255, 255))
    screen.blit(player1_life_text, (50, 50))
    screen.blit(player2_life_text, (screen_width - 150, 50))
    pygame.draw.rect(screen, health_color, (health_rect.x, health_rect.y, health_rect.width, health_rect.height))

    if pressed_keys[pygame.K_l]:
        player1_life -= 10
    elif pressed_keys[pygame.K_p]:
        player2_life -= 10

    # Verificar se algum personagem morreu
    if player1_life <= 0 or player2_life <= 0:
        game_over_text = final_font.render("Acabe com ele!", True, (255, 255, 255))
        screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - game_over_text.get_height()/2))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()



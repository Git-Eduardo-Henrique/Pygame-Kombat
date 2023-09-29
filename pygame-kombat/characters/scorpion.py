import pygame
from os import getcwd


class Scorpion:
    def __init__(self, screen, screen_height):
        self.diretorio = getcwd()  # diretorio onde o jogo está
        self.screen = screen

        # listas para guardar as animações
        self.scorpion_normal = []
        self.scorpion_normal_inv = []
        self.scorpion_walking = []
        self.scorpion_walking_inv = []
        self.scorpion_hp = []
        self.scorpion_hp_inv = []
        # carregar as imagens
        # imagens do scorpion parado
        for i in range(1, 7):  
            image = pygame.image.load(
                f"{self.diretorio}\\pygame-kombat\\midias\\images\\scorpion\\scorpion_normal\\scorpion_normal_{i}.png"
                )  
            image_upscale = pygame.transform.scale(
                image, (image.get_width() * 2, image.get_height() * 2)
                ) 

            # inseri as imagens nas listas
            self.scorpion_normal.append(image_upscale)
            self.scorpion_normal_inv.append(pygame.transform.flip(image_upscale, True, False))


         # imagens do scorpion andando
        for i in range(1, 9): 
            image = pygame.image.load(
                f"{self.diretorio}\\pygame-kombat\\midias\\images\\scorpion\\scorpion_walk\\scorpion_walking_{i}.png"
                )  
            image_upscale = pygame.transform.scale(
                image, (image.get_width() * 2, image.get_height() * 2)
                ) 

            self.scorpion_walking.append(image_upscale)
            self.scorpion_walking_inv.append(pygame.transform.flip(image_upscale, True, False))


        # imagens do scorpion soco alto
        for i in range(1, 8):
            image = pygame.image.load(
                f"{self.diretorio}\\pygame-kombat\\midias\\images\\scorpion\\scorpion_high_punch\\scorpion_hp_{i}.png"
            ) 
            image_upscale = pygame.transform.scale(
                image, (image.get_width() * 2, image.get_height() * 2)
                )
            self.scorpion_hp.append(image_upscale)
            self.scorpion_hp_inv.append(pygame.transform.flip(image_upscale, True, False))


        self.scorpion_state = True  # True para esquerda, False para direita
        self.animation_index = 0  # em qual imagem a animação está

        # posição x e y do scorpion 
        self.scorpion_x = 50
        self.scorpion_y = screen_height - self.scorpion_normal[0].get_height() - 25

    def animation(self, animation): # animação andando e parado
        self.animation_index += 0.15

        if self.animation_index >= len(animation):  # se a animação acabar irá repetir
            self.animation_index = 0

        self.screen.blit(animation[int(self.animation_index)], (self.scorpion_x, self.scorpion_y))

    def atack(self):
        for event in pygame.event.get():
            # Verifica se alguma tecla foi pressionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:

                    if self.scorpion_state:
                        self.animation(screen=self.screen, animation=self.scorpion_hp)
                    else:
                        self.animation(screen=self.screen, animation=self.scorpion_hp_inv)
            

    def events(self):
        pressed_keys = pygame.key.get_pressed()

        # nao permite que o player sair da tela
        if self.scorpion_x < 0:  # se estiver na borda esquerda
            self.scorpion_x = 0
        elif self.scorpion_x > self.screen.get_width() - self.scorpion_normal[0].get_width():  # se estiver na borda direita
            self.scorpion_x = self.screen.get_width() - self.scorpion_normal[0].get_width()

        self.atack()

        if pressed_keys[pygame.K_a]:  # andar para a esquerda
            self.scorpion_x -= 5
            # false se o personagem começar na esquerda
            # true se o personagem começar na direita
            self.scorpion_state = False

            self.animation(
                animation=self.scorpion_walking_inv
            )

        elif pressed_keys[pygame.K_d]:  # andar para a direita
            self.scorpion_x += 5
            # true se o personagem começar na esquerda
            # false se o personagem começar na direita
            self.scorpion_state = True  # aqui estava true

            self.animation(
                animation=self.scorpion_walking
            )

        else:  # se estiver parado
            if self.scorpion_state:
                self.animation(
                    animation=self.scorpion_normal
                    )
            else:
                self.animation(
                    animation=self.scorpion_normal_inv
                )

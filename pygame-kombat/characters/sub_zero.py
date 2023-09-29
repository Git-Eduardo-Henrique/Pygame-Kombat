import pygame
from os import getcwd


class sub_zero:
    def __init__(self, screen_width, screen_height):
        self.diretorio = getcwd()  # diretorio

        # listas para animações
        self.sub_zero_normal = []
        self.sub_zero_normal_inv = []
        self.sub_zero_walking = []
        self.sub_zero_walking_inv = []

        # sub zero parado
        for i in range(1, 8):
            image = pygame.image.load(
                f"{self.diretorio}\\pygame-kombat\\midias\\images\\sub-zero\\sub-zero normal\\sub_zero_{i}.png"
                )
            image_upscale = pygame.transform.scale(
                image, (image.get_width() * 2, image.get_height() * 2)
                )

            self.sub_zero_normal.append(image_upscale)
            self.sub_zero_normal_inv.append(pygame.transform.flip(image_upscale, True, False))
        
        # sub zero andando
        for i in range(1, 8): 
            image = pygame.image.load(
                f"{self.diretorio}\\pygame-kombat\\midias\\images\\sub-zero\\sub-zero walking\\sub_zero_walking_{i}.png"
                )  
            image_upscale = pygame.transform.scale(
                image, (image.get_width() * 2, image.get_height() * 2)
                ) 

            self.sub_zero_walking.append(image_upscale)
            self.sub_zero_walking_inv.append(pygame.transform.flip(image_upscale, True, False))

        self.sub_zero_state = False  # false para direita e true para esquerda
        self.animation_index = 0  # qual imagem esta

        # posições x e y do sub zero
        self.sub_zero_x = (screen_width - self.sub_zero_normal[0].get_width()) - 50
        self.sub_zero_y = screen_height - self.sub_zero_normal[0].get_height() - 25

    def update(self, screen, animation):
        self.animation_index += 0.15
        if self.animation_index >= len(animation):
            self.animation_index = 0
        screen.blit(animation[int(self.animation_index)], (self.sub_zero_x, self.sub_zero_y))

    def events(self, screen):
        pressed_keys = pygame.key.get_pressed()

        # não deixa o jogador sair da tela
        if self.sub_zero_x < 0:
            self.sub_zero_x = 0
        elif self.sub_zero_x > screen.get_width() - self.sub_zero_normal[0].get_width():
            self.sub_zero_x = screen.get_width() - self.sub_zero_normal_inv[0].get_width()

        if pressed_keys[pygame.K_LEFT]:
            self.sub_zero_x -= 5
            self.sub_zero_state = False

            self.update(
                screen=screen,
                animation=self.sub_zero_walking_inv
                )

        elif pressed_keys[pygame.K_RIGHT]:
            self.sub_zero_x += 5
            self.sub_zero_state = True

            self.update(
                screen=screen, 
                animation=self.sub_zero_walking
                )

        else:
            if self.sub_zero_state:
                self.update(
                    screen=screen, 
                    animation=self.sub_zero_normal
                )
            else:
                self.update(
                    screen=screen, 
                    animation=self.sub_zero_normal_inv
                )

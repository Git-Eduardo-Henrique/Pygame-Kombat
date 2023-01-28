import pygame
from os import getcwd


class sub_zero:
    def __init__(self, screen_width, screen_height):
        self.diretorio = getcwd()
        self.sub_zero_animation = []
        self.sub_zero_animation_inv = []
        for i in range(1, 8):
            image = pygame.image.load(f"{self.diretorio}\\midias\\images\\sub-zero\\sub_zero_{i}.png")
            image_upscale = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
            self.sub_zero_animation.append(image_upscale)
            self.sub_zero_animation_inv.append(pygame.transform.flip(image_upscale, True, False))

        self.sub_zero_state = False
        self.animation_index = 0
        self.sub_zero_x = (screen_width - self.sub_zero_animation[0].get_width()) - 50
        self.sub_zero_y = screen_height - self.sub_zero_animation[0].get_height() - 25

    def update(self, screen):
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

    def move(self, screen):
        pressed_keys = pygame.key.get_pressed()

        if self.sub_zero_x < 0:
            self.sub_zero_x = 0
        elif self.sub_zero_x > screen.get_width() - self.sub_zero_animation[0].get_width():
            self.sub_zero_x = screen.get_width() - self.sub_zero_animation[0].get_width()

        if pressed_keys[pygame.K_LEFT]:
            self.sub_zero_x -= 5
            self.sub_zero_state = False
        if pressed_keys[pygame.K_RIGHT]:
            self.sub_zero_x += 5
            self.sub_zero_state = True

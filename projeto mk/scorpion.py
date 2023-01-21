import pygame
from os import getcwd


class scorpion:
    def __init__(self, screen_height):
        self.diretorio = getcwd()
        self.scorpion_animation = []
        self.scorpion_animation_inv = []
        for i in range(1, 8):
            image = pygame.image.load(f"{self.diretorio}\\images\\scorpion\\scorpion_{i}.png")
            self.scorpion_animation.append(image)
            self.scorpion_animation_inv.append(pygame.transform.flip(image, True, False))

        self.scorpion_state = True
        self.animation_index = 0
        self.scorpion_x = 50
        self.scorpion_y = screen_height - self.scorpion_animation[0].get_height() - 25

    def update(self, screen):
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
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.scorpion_x -= 5
            self.scorpion_state = False
        if pressed_keys[pygame.K_d]:
            self.scorpion_x += 5
            self.scorpion_state = True

import pygame
from os import getcwd


class scorpion:
    def __init__(self, screen_height):
        self.diretorio = getcwd()
        self.scorpion_normal = []
        self.scorpion_normal_inv = []

        self.scorpion_walking = []
        self.scorpion_walking_inv = []
        for i in range(1, 7):
            image = pygame.image.load(f"{self.diretorio}\\images\\scorpion\\scorpion_normal\\scorpion_normal_{i}.png")
            image_upscale = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
            self.scorpion_normal.append(image_upscale)
            self.scorpion_normal_inv.append(pygame.transform.flip(image_upscale, True, False))

        for i in range(1, 9):
            image = pygame.image.load(f"{self.diretorio}\\images\\scorpion\\scorpion_walk\\scorpion_walking_{i}.png")
            image_upscale = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
            self.scorpion_walking.append(image_upscale)
            self.scorpion_walking_inv.append(pygame.transform.flip(image_upscale, True, False))

        self.scorpion_state = True
        self.animation_index = 0
        self.scorpion_x = 50
        self.scorpion_y = screen_height - self.scorpion_normal[0].get_height() - 25
        self.walking_state = False

    def update(self, screen, animation, animation_reverse):
        if self.scorpion_state:
            self.animation_index += 0.15
            if self.animation_index >= len(animation):
                self.animation_index = 0
            screen.blit(animation[int(self.animation_index)], (self.scorpion_x, self.scorpion_y))
        else:
            self.animation_index += 0.15
            if self.animation_index >= len(animation_reverse):
                self.animation_index = 0
            screen.blit(animation_reverse[int(self.animation_index)], (self.scorpion_x, self.scorpion_y))

    def events(self, screen):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.scorpion_x -= 5
            self.scorpion_state = False
            self.update(
                screen=screen,
                animation=self.scorpion_walking,
                animation_reverse=self.scorpion_walking_inv
            )

        elif pressed_keys[pygame.K_d]:
            self.scorpion_x += 5
            self.scorpion_state = True
            self.update(
                screen=screen,
                animation=self.scorpion_walking,
                animation_reverse=self.scorpion_walking_inv
            )
        else:
            self.update(
                screen=screen,
                animation=self.scorpion_normal,
                animation_reverse=self.scorpion_normal_inv
            )



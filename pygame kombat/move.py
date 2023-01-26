import pygame


class move:
    def __init__(self, char_x, char_y):
        self.animation_index = 0  # verifica em qual sprite o personagem esta
        self.char_x = char_x
        self.char_y = char_y

    def animation_update(self, screen, char_state, animation, animation_reverse):
        if char_state:  # se o personagem estiver para a frente
            self.animation_index += 0.15

            if self.animation_index >= len(animation):
                self.animation_index = 0

            screen.blit(animation[int(self.animation_index)], (self.char_x, self.char_y))

        else:  # se estiver para atraz
            self.animation_index += 0.15

            if self.animation_index >= len(animation_reverse):
                self.animation_index = 0

            screen.blit(animation_reverse[int(self.animation_index)], (self.char_x, self.char_y))

    def moving(
            self, screen, animation_normal, animation_normal_inv, animation_moving, animation_moving_inv,
            char_state, new_char_state_1, new_char_state_2
               ):
        pressed_keys = pygame.key.get_pressed()

        # nao permite que o player sair da tela
        if self.char_x < 0:  # se estiver na borda esquerda
            self.char_x = 0
        elif self.char_x > screen.get_width() - animation_normal[0].get_width():  # se estiver na borda direita
            self.char_x = screen.get_width() - animation_normal[0].get_width()

        # permite o player andar para a esquerda
        if pressed_keys[pygame.K_a]:
            self.char_x -= 5
            # false se o personagem começar na esquerda
            # true se o personagem começar na direita
            char_state = new_char_state_1

            self.animation_update(
                screen=screen,
                char_state=char_state,
                animation=animation_moving,
                animation_reverse=animation_moving_inv
            )

        elif pressed_keys[pygame.K_d]:
            self.char_x += 5
            # true se o personagem começar na esquerda
            # false se o personagem começar na direita
            char_state = new_char_state_2  # aqui estava true

            self.animation_update(
                screen=screen,
                char_state=char_state,
                animation=animation_moving,
                animation_reverse=animation_moving_inv
            )

        else:
            self.animation_update(
                screen=screen,
                char_state=char_state,
                animation=animation_normal,
                animation_reverse=animation_normal_inv
            )

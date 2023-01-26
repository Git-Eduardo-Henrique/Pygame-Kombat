import pygame


class move:
    def __init__(self):
        self.animation_index = 0  # verifica em qual sprite o personagem esta

    def animation_update(self, screen, char_state, animation, animation_reverse, char_x, char_y):
        if char_state:  # se o personagem estiver para a frente
            self.animation_index += 0.15

            if self.animation_index >= len(animation):
                self.animation_index = 0

            screen.blit(animation[int(self.animation_index)], (char_x, char_y))

        else:  # se estiver para atraz
            self.animation_index += 0.15

            if self.animation_index >= len(animation_reverse):
                self.animation_index = 0

            screen.blit(animation_reverse[int(self.animation_index)], (char_x, char_y))

    def moving(
            self, screen, animation_normal, animation_normal_inv, animation_moving, animation_moving_inv,
            char_x, char_y, char_state, new_char_state_1, new_char_state_2
               ):
        pressed_keys = pygame.key.get_pressed()

        # nao permite que o player sair da tela
        if char_x < 0:  # se estiver na borda esquerda
            char_x = 0
        elif char_x > screen.get_width() - animation_normal[0].get_width():  # se estiver na borda direita
            char_x = screen.get_width() - animation_normal[0].get_width()

        # permite o player andar para a esquerda
        if pressed_keys[pygame.K_a]:
            char_x -= 5
            # false se o personagem começar na esquerda
            # true se o personagem começar na direita
            char_state = new_char_state_1

            self.animation_update(
                screen=screen,
                char_state=char_state,
                animation=animation_moving,
                animation_reverse=animation_moving_inv,
                char_x=char_x,
                char_y=char_y
            )

        elif pressed_keys[pygame.K_d]:
            char_x += 5
            # true se o personagem começar na esquerda
            # false se o personagem começar na direita
            char_state = new_char_state_2  # aqui estava true

            self.animation_update(
                screen=screen,
                char_state=char_state,
                animation=animation_moving,
                animation_reverse=animation_moving_inv,
                char_x=char_x,
                char_y=char_y
            )

        else:
            self.animation_update(
                screen=screen,
                char_state=char_state,
                animation=animation_normal,
                animation_reverse=animation_normal_inv,
                char_x=char_x,
                char_y=char_y
            )

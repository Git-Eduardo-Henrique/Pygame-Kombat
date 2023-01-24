import pygame


class FightHud:
    def __init__(self, screen):
        self.screen = screen
        self.dev_tools_on = False
        # cores
        self.health_color = (0, 255, 0)
        self.demage_color = (255, 0, 0)
        # tamanho das barras de vida
        self.health_rect = pygame.Rect(10, 25, 480, 20)
        self.health_rect_2 = pygame.Rect(590, 25, 480, 20)
        # fontes
        self.life_font = pygame.font.Font(None, 30)

    def devtools(self, player1_life, player2_life):
        dev_text = self.life_font.render(f"dev tools on", True, (0, 255, 0))
        player2_life_text = self.life_font.render(
            f"Player 1: {str(player1_life)} Player 2: {str(player2_life)}", True,(255, 255, 255)
        )

        self.screen.blit(dev_text, (10, 0))
        self.screen.blit(player2_life_text, (10, 50))

    def in_fight(self, player1_life, player2_life, max_life, timer):
        # informações de desenvolvedor
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_1]:
            self.dev_tools_on = True

        if self.dev_tools_on:
            self.devtools(
                player1_life=player1_life,
                player2_life=player2_life
            )
        # timer
        timer_text = self.life_font.render(f"{timer}", True, (255, 255, 255))
        timer_rect = timer_text.get_rect()
        timer_rect.center = (self.screen.get_width() / 2, 35)

        # barras de vida
        pygame.draw.rect(
            self.screen, self.demage_color,
            (self.health_rect.x, self.health_rect.y, self.health_rect.width, self.health_rect.height)
        )
        pygame.draw.rect(
            self.screen, self.health_color,
            (self.health_rect.x, self.health_rect.y, player1_life / max_life * self.health_rect.width,
             self.health_rect.height)
        )
        pygame.draw.rect(
            self.screen, self.demage_color,
            (self.health_rect_2.x, self.health_rect_2.y, self.health_rect_2.width, self.health_rect_2.height)
        )
        pygame.draw.rect(
            self.screen, self.health_color,
            (self.health_rect_2.x, self.health_rect_2.y, player2_life / max_life * self.health_rect_2.width,
             self.health_rect_2.height)
        )

        self.screen.blit(timer_text, timer_rect)

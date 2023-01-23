import pygame
from os import getcwd

from scorpion import Scorpion
from sub_zero import sub_zero
from fight_hud import FightHud


class Fight:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.diretorio = getcwd()

        self.background_image = pygame.image.load(f"{self.diretorio}\\images\\stage.png")
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))

        # Definir a fonte para mostrar as vidas
        self.final_font = pygame.font.Font(None, 50)

        # vidas
        self.max_life = 1000
        self.player1_life = self.max_life
        self.player2_life = self.max_life

        self.scorpion = Scorpion(screen_height=screen_height)

        self.sub_zero = sub_zero(
            screen_height=screen_height,
            screen_width=screen_width
        )

        self.FightHud = FightHud(
             screen=screen
        )

    def fight_start(self):
        self.screen.blit(self.background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.FightHud.in_fight(
                player1_life=self.player1_life,
                player2_life=self.player2_life,
                max_life=self.max_life
        )

        self.sub_zero.update(screen=self.screen)
        self.sub_zero.move(screen=self.screen)

        self.scorpion.events(screen=self.screen)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_l]:
            self.player1_life -= 10
        elif pressed_keys[pygame.K_p]:
            self.player2_life -= 10

        if self.player1_life <= 0 or self.player2_life <= 0:
            game_over_text = self.final_font.render("finish him", True, (255, 255, 255))
            self.screen.blit(game_over_text, (
                self.screen_width / 2 - game_over_text.get_width() / 2, 100))

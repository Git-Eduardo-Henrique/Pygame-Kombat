import pygame
from os import getcwd

from characters.scorpion import Scorpion
from characters.sub_zero import sub_zero
from fight.fight_hud import FightHud


class Fight:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.diretorio = getcwd()

        self.background_image = pygame.image.load(f"{self.diretorio}\\pygame-kombat\\midias\\images\\stage.png")
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))

        # Definir a fonte para mostrar as vidas
        self.final_font = pygame.font.Font(None, 50)

        # vidas
        self.max_life = 1000
        self.player1_life = self.max_life
        self.player2_life = self.max_life

        self.scorpion = Scorpion(
            screen=screen,
            screen_height=screen_height
            )

        self.sub_zero = sub_zero(
            screen_height=screen_height,
            screen_width=screen_width
        )

        self.FightHud = FightHud(
             screen=screen
        )
        self.timer_seconds = 120
        pygame.time.set_timer(pygame.USEREVENT, 1000)

    def fight_start(self):
        self.screen.blit(self.background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.USEREVENT:
                # Decrementando o cronômetro

                if self.timer_seconds <= 0:
                    # Verificando se o jogador tem vidas
                    if self.player1_life < self.player2_life:
                        self.player1_life = 0
                    elif self.player2_life < self.player1_life:
                        self.player2_life = 0
                    else:
                        self.timer_seconds = 30
                else:
                    self.timer_seconds -= 1

        self.FightHud.in_fight(
                player1_life=self.player1_life,
                player2_life=self.player2_life,
                max_life=self.max_life,
                timer=self.timer_seconds
        )

        self.sub_zero.events(screen=self.screen)

        self.scorpion.events()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_l]:
            self.player1_life -= 10
        elif pressed_keys[pygame.K_p]:
            self.player2_life -= 10

        if self.player1_life <= 0 or self.player2_life <= 0:
            game_over_text = self.final_font.render("finish him", True, (255, 255, 255))
            self.timer_seconds = 0
            self.screen.blit(game_over_text, (
                self.screen_width / 2 - game_over_text.get_width() / 2, 100))

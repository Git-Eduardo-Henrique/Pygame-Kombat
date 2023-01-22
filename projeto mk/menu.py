import pygame


class menu:
    def __init__(self):
        # cores
        self.running = True
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        # fontes
        self.font = pygame.font.Font(None, 30)

        # textos para os botões
        self.play_text = self.font.render("Jogar", True, self.white)
        self.quit_text = self.font.render("Sair", True, self.white)

        # retângulos para os botões
        self.play_rect = self.play_text.get_rect()
        self.play_rect.center = (200, 100)

        self.quit_rect = self.quit_text.get_rect()
        self.quit_rect.center = (200, 200)

        # variável para armazenar a opção selecionada
        self.selected = "play"

    def menu_start(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.selected == "play":
                        self.selected = "quit"
                    else:
                        self.selected = "play"
                elif event.key == pygame.K_UP:
                    if self.selected == "play":
                        self.selected = "quit"
                    else:
                        self.selected = "play"
                elif event.key == pygame.K_RETURN:
                    if self.selected == "play":
                        # mudar para a tela de jogo
                        self.running = False
                    else:
                        pygame.quit()
                        exit()

            # desenhar botões na tela
            screen.fill((0, 0, 0))
            if self.selected == "play":
                self.play_text = self.font.render("Start", True, self.red)
                self.quit_text = self.font.render("Quit", True, self.white)
            else:
                self.play_text = self.font.render("Start", True, self.white)
                self.quit_text = self.font.render("Quit", True, self.red)
            screen.blit(self.play_text, self.play_rect)
            screen.blit(self.quit_text, self.quit_rect)



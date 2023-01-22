import pygame

class menu:
    def __init__(self):
        # definir cores
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        # definir fonte
        self.font = pygame.font.Font(None, 30)

        # criar textos para os botões
        self.play_text = self.font.render("Jogar", True, self.white)
        self.quit_text = self.font.render("Sair", True, self.white)

        # criar retângulos para os botões
        self.play_rect = play_text.get_rect()
        play_rect.center = (200, 100)

        quit_rect = quit_text.get_rect()
        quit_rect.center = (200, 200)

        # variável para armazenar a opção selecionada
        self.selected = "play"

    def init(self, screen, font):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selected == "play":
                        selected = "quit"
                    else:
                        selected = "play"
                elif event.key == pygame.K_UP:
                    if selected == "play":
                        selected = "quit"
                    else:
                        selected = "play"
                elif event.key == pygame.K_RETURN:
                    if selected == "play":
                        # mudar para a tela de jogo
                        pass
                    else:
                        running = False

            # desenhar botões na tela
        screen.fill((0, 0, 0))
        if selected == "play":
            play_text = font.render("Jogar", True, red)
            quit_text = font.render("Sair", True, white)
        else:
            play_text = font.render("Jogar", True, white)
            quit_text = font.render("Sair", True, red)
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)
        pygame.display.update()
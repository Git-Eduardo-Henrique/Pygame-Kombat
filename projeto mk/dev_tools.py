
class dev:
    def init(self, screen, life_font, player1_life, player2_life):
        player2_life_text = life_font.render(f"Player 1: {str(player1_life)} Player 2: {str(player2_life)}", True,
                                             (255, 255, 255))
        dev_text = life_font.render(f"dev tools on", True, (0, 255, 0))

        screen.blit(dev_text, (10, 0))
        screen.blit(player2_life_text, (10, 50))


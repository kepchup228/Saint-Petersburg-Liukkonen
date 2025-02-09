import pygame
from gamee import Game
from settingss import *

class StartScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render("Как играть", True, (0, 0, 0))
        self.play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)

    def draw(self, surface):
        surface.fill(WHITE)
        surface.blit(self.text, (WIDTH // 2 - self.text.get_width() // 2, HEIGHT // 2 - 100))
        pygame.draw.rect(surface, (0, 255, 0), self.play_button)
        button_text = pygame.font.Font(None, 36).render("Играть", True, (0, 0, 0))
        surface.blit(button_text, (self.play_button.x + 50, self.play_button.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.collidepoint(event.pos):
                return True  # Начать игру
        return False

# В main.py измените функцию main
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = Game()
    start_screen = StartScreen()

    running = True
    in_game = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not in_game:
                if start_screen.handle_event(event):
                    in_game = True

        if in_game:
            game.level.update()
            game.level.draw(screen)
        else:
            start_screen.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

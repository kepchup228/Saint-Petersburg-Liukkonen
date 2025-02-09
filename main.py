import pygame
from gamee import Game
from settingss import *

class StartScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)  # шрифт для заголовка
        self.text = self.font.render("Как играть", True, (0, 0, 0))  # текст заголовка
        self.play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)  # кнопка "Играть"

    def draw(self, surface):
        surface.fill(WHITE)  # фон начального экрана
        surface.blit(self.text, (WIDTH // 2 - self.text.get_width() // 2, HEIGHT // 2 - 100))
        pygame.draw.rect(surface, (0, 255, 0), self.play_button)  # отрисовка кнопки
        button_text = pygame.font.Font(None, 36).render("Играть", True, (0, 0, 0))  # текст на кнопке
        surface.blit(button_text, (self.play_button.x + 50, self.play_button.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.play_button.collidepoint(event.pos):
            return True  # если нажата кнопка "Играть", то начинаем игру
        return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна
    clock = pygame.time.Clock()
    game = Game()
    start_screen = StartScreen()

    running = True
    in_game = False  # флаг, показывающий, запущена ли игра
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # выход из игры при закрытии окна
            if not in_game and start_screen.handle_event(event):
                in_game = True  # переход в игру при нажатии кнопки "Играть"

        if in_game:
            game.level.update()  # Обновление игрового уровня
            game.level.draw(screen)  # Отрисовка игрового уровня
        else:
            start_screen.draw(screen)  # начальный экран

        pygame.display.flip()  # обновление экрана
        clock.tick(FPS)  # ограничение частоты кадров

    pygame.quit()


if __name__ == "__main__":
    main()  # запуск

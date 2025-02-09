import pygame
from gamee import Game
from settingss import *

class StartScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 74)
        self.instructions = [
            "## Описание игры",
            "",
            "### Цель игры",
            "Ваша задача — управлять персонажем, собирать монеты и избегать столкновений с врагами.",
            "Набирайте очки, повышайте уровень и становитесь сильнее!",
            "",
            "### Управление",
            "- **Стрелки влево/вправо**: Двигайте персонажа влево или вправо.",
            "- **Пробел**: Прыжок (если такая механика предусмотрена).",
            "- **Клавиша 'R'**: Начать игру заново после завершения.",
            "",
            "### Как играть",
            "1. **Начало игры**: После запуска игры вы увидите экран с кнопкой 'Начать'. Нажмите на неё, чтобы начать.",
            "2. **Сбор монет**: Собирайте монеты, которые появляются случайным образом. Каждая собранная монета увеличивает ваш счет.",
            "3. **Избегайте врагов**: Враги будут появляться на уровне. Если вы столкнетесь с врагом, ваш персонаж потеряет здоровье.",
            "4. **Уровни**: После сбора 10 монет ваш персонаж повысит уровень.",
            "5. **Конец игры**: Если здоровье вашего персонажа достигнет нуля, игра закончится.",
            "",
            "### Дополнительные советы",
            "- Старайтесь избегать врагов и планируйте свои движения заранее.",
            "- Следите за количеством собранных монет и старайтесь достичь как можно большего результата.",
            "- Используйте кнопку 'Начать заново', чтобы попробовать снова и улучшить свои навыки!"
        ]
        self.play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50)

    def draw(self, surface):
        surface.fill(WHITE)
        title_text = self.title_font.render("Как играть", True, (0, 0, 0))
        surface.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 300))

        # Отображение инструкций
        for i, line in enumerate(self.instructions):
            instruction_text = self.font.render(line, True, (0, 0, 0))
            surface.blit(instruction_text, (50, HEIGHT // 2 - 200 + i * 30))

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

import pygame
import os
from settingss import *

class Player:
    def __init__(self):
        self.image_path = 'data/images/player.png'
        if not os.path.isfile(self.image_path):
            print(f"Ошибка: файл {self.image_path} не найден!")
            self.image = pygame.Surface((50, 50))
        else:
            original_image = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(original_image, (50, 50))  # Изменение размера

        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)  # Начальная позиция игрока
        self.speed = 5
        self.health = 100
        self.invulnerability_timer = 0  # Время последнего урона
        self.invulnerability_duration = 200  # Длительность неуязвимости в миллисекундах
        self.coins_collected = 0  # Собранные монеты
        self.level = 1  # Уровень игрока
        self.base_speed = 5  # Базовая скорость для роста

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

    def draw(self, surface):
        current_time = pygame.time.get_ticks()
        if current_time - self.invulnerability_timer < self.invulnerability_duration:
            # Рисовать игрока полупрозрачным во время неуязвимости
            self.image.set_alpha(128)
        else:
            self.image.set_alpha(255)  # Полная непрозрачность

        surface.blit(self.image, self.rect)

    def draw_health_bar(self, surface):
        bar_width = 50
        bar_height = 10
        health_ratio = self.health / 100

        bar_x = self.rect.x + (self.rect.width - bar_width) // 2
        bar_y = self.rect.y - 15

        # Рисуем красный фон шкалы
        pygame.draw.rect(surface, RED, (bar_x, bar_y, bar_width, bar_height))
        # Рисуем зеленую часть шкалы
        pygame.draw.rect(surface, GREEN, (bar_x, bar_y, bar_width * health_ratio, bar_height))

    def take_damage(self, damage):
        current_time = pygame.time.get_ticks()
        if current_time - self.invulnerability_timer > self.invulnerability_duration:
            self.health -= damage
            self.invulnerability_timer = current_time  # Устанавливаем время последнего урона
            if self.health < 0:
                self.health = 0  # Чтобы здоровье не уходило в минус

    def level_up(self):
        if self.level < 20:  # Максимальный уровень - 20
            self.level += 1
            self.coins_collected = 0  # Обнуляем счёт монет
            self.speed = self.base_speed * (1 + 0.05 * self.level)  # Увеличиваем скорость
        if self.level >= 20:
            self.level = 20
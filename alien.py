import pygame
from lazer import Lazer
import random


class Alien(pygame.sprite.Sprite):
    def __init__(self, game, x, y, level):
        self.groups = game.all_sprites_list, game.enemy_sprites_list
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(f"alien{level}.png")
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 2
        self.lazers = []
        self.level = level
        self.health = level

    # def draw(self, screen):
    #     print("here")
    #     screen.blit(self.image, self.rect)
    #     self.healthbar(screen)

    def update(self):
        self.rect.y += self.velocity_y
        if random.randint(1,100) == 1:
            self.shoot()
            print('i in')
        if self.rect.y >= 800:
            self.kill()
        if self.health == 0:
            self.kill()
        for lazer in self.lazers:
            lazer.movedown()
            if lazer.off_screen():
                self.lazers.remove(lazer)
                print("remove")
                lazer.kill()

    def shoot(self):
        lazer = Lazer(self.game, self.rect.x, self.rect.y, 0, "img/pixel_laser_yellow.png")
        self.lazers.append(lazer)

    def draw_alien_health(self):
        if self.health == 3:
            col = (0, 255, 0)

        elif self.health == 2:
            col = (255, 255, 0)
        else:
            col = (255, 0, 0)
        width = int(self.rect.width * self.health / 3)
        health_bar = pygame.Rect(0, 0, width, 7)
        pygame.draw.rect(self.image, col, health_bar)

    def off_screen(self):
        return self.rect.y >= 800

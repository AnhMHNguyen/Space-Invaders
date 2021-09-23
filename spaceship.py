import pygame
from lazer import Lazer


class Spaceship(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites_list
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 5
        self.health = 100
        self.lazers = []

    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)
    #     for b in self.lazers:
    #         b.draw(screen)

    def move(self, x):
        self.rect.x = x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 950:
            self.rect.x = 950

    def shoot(self):
        lazer = Lazer(self.game, self.rect.x - 17, self.rect.y - 16, 1, "img/pixel_laser_yellow.png")
        self.lazers.append(lazer)

    def update(self):
        for lazer in self.lazers:
            lazer.moveup()
            if lazer.off_screen():
                self.lazers.remove(lazer)
                lazer.kill()
            elif lazer in self.lazers and not lazer.alive():
                self.lazers.remove(lazer)

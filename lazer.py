import pygame


class Lazer(pygame.sprite.Sprite):

    def __init__(self, game, x, y,shooter, file):
        self.groups = game.all_sprites_list, game.lazer_sprites_list
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.shooter = shooter
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 7

    # def fire(self):
    #     self.status = 1
    #     self.visible = True
    #
    # def update(self):
    #     # if self.status == 1:
    #     #     if self.rect.y <= 0:
    #     #         self.kill()
    #     #     else:
    #     self.rect.y -= self.velocity_y

    # def draw(self, screen):
    #     screen.blit(self.image, (self.rect.x, self.rect.y))

    def moveup(self):
        self.rect.y -= self.velocity_y

    def movedown(self):
        self.rect.y += self.velocity_y

    def off_screen(self):
        return self.rect.y < -100 or self.rect.y >= 1000


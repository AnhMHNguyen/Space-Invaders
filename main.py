import pygame
from spaceship import Spaceship
from alien import Alien
import random

WIDTH = 1000
HEIGHT = 700

def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 65
    BAR_HEIGHT = 10
    fill = pct * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = (0,255,0)
    elif pct > 0.3:
        col = (255, 255, 0)
    else:
        col = (255,0,0)
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 2)


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        self.background = pygame.image.load("img/background1.jpg")
        self.background = pygame.transform.scale(self.background, (1000, 700))
        pygame.display.set_caption("Space Invaders")
        self.level = 0
        self.wave_length = 3
        self.all_sprites_list = pygame.sprite.Group()
        self.enemy_sprites_list = pygame.sprite.Group()
        self.lazer_sprites_list = pygame.sprite.Group()
        # self.spaceship_lazer_sprites_list = pygame.sprite.Group()
        self.playing = True
        self.spaceship = Spaceship(self, x=450, y=600)
        self.clock = pygame.time.Clock()

    # def new(self):

    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def update(self):
        if len(self.enemy_sprites_list) == 0:
            self.level += 1
            self.wave_length +=2
            self.create_aliens()
        pos = pygame.mouse.get_pos()
        self.spaceship.move(pos[0])
        self.all_sprites_list.update()
        # print(self.lazer_sprites_list)
        hit1 = pygame.sprite.groupcollide(self.enemy_sprites_list, self.lazer_sprites_list, False, True, pygame.sprite.collide_mask)
        for enemy, lazer in hit1.items():
            if lazer[0].shooter == 1:
                enemy.health -= 1

        hit2 = pygame.sprite.spritecollide(self.spaceship, self.enemy_sprites_list, True)
        if hit2 or any(alien.off_screen() for alien in self.enemy_sprites_list):
            self.spaceship.lives -= 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.all_sprites_list.draw(self.screen)
        font = pygame.font.SysFont("courier", 25, bold=True)
        text = font.render("Lives: " + str(self.spaceship.lives), 1, (0, 0, 0))
        self.screen.blit(text, (20, 10))
        text = font.render("Level: " + str(self.level), 1, (0, 0, 0))
        self.screen.blit(text, (850, 10))
        for alien in self.all_sprites_list:
            if isinstance(alien, Alien):
                alien.draw_alien_health()
            self.screen.blit(alien.image, alien.rect)
        draw_player_health(self.screen, self.spaceship.rect.x, self.spaceship.rect.y + 70, self.spaceship.health / 100)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceship.shoot()

    def quit_game(self):
        global running
        running = False

    def create_aliens(self):
        if self.level <= 5:
            choices = [1, 2]
        elif 5 < self.level <= 10:
            choices = [1, 2, 3]
        else:
            choices = [2, 3]
        for i in range(self.wave_length):
            Alien(self, random.randint(50, WIDTH - 100), random.randint(-1500, -100), random.choice(choices))


g = Game()
while g.playing:
    g.run()
pygame.quit()

# all_sprites_list.add(spaceship)


# enemy_sprites_list.add(alien)

# running = True
#
#
# while running:
#
#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT:
#     #         running = False
#     #     if event.type ==pygame.KEYDOWN:
#     #         if event.key == pygame.K_SPACE and spaceship in all_sprites_list:
#     #             spaceship.shoot()
#     #
#     # screen.fill((0,0,0))
#     # screen.blit(background, (0,0))
#     #
#     # if len(enemy_sprites_list) == 0:
#     #     level += 1
#     #     wave_length += 2
#     #     create_aliens(level, wave_length)
#     #
#     # pos = pygame.mouse.get_pos()
#     # spaceship.move(pos[0])
#     #
#     # for i in spaceship.lazers:
#     #     all_sprites_list.add(i)
#     #
#     # hit = pygame.sprite.groupcollide(enemy_sprites_list, all_sprites_list, False, False)
#     # for i in hit:
#     #     print(i)
#     #     # if hit[i][0] == spaceship:
#     #     #     lives -= 1
#     #     # else:
#     #     #     hit[i][0].kill()
#     #     # if lives <= 0:
#     #     #     font = pygame.font.SysFont("Courier", 74, bold=True)
#     #     #     text = font.render("GAME OVER", 1, (0,0,0))
#     #     #     screen.blit(text, (300, 300))
#     #     #     pygame.display.flip()
#     #     #     pygame.time.wait(3000)
#     #     #     running = False
#     #
#     # all_sprites_list.draw(screen)
#     # enemy_sprites_list.draw(screen)
#     # font = pygame.font.SysFont("courier", 25, bold=True)
#     # text = font.render("Lives: " + str(lives), 1, (0, 0, 0))
#     # screen.blit(text, (20, 10))
#     # text = font.render("Level: " + str(level), 1, (0, 0, 0))
#     # screen.blit(text, (850, 10))
#     # all_sprites_list.update()
#     # enemy_sprites_list.update()
#     #
#     # pygame.display.update()
#     clock.tick(60)
# pygame.quit()

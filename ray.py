import pygame
import snipets

class Ray(pygame.sprite.Sprite):
    def __init__(self, starting_position, direction, duration, speed, group, index):
        super().__init__(group)
        self.image = pygame.Surface((2, 2))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = starting_position
        self.direction = direction
        self.duration = duration
        self.speed = speed
        self.distance = 0
        self.hit_position = None
        self.hit_distance = None
        self.index = index
    def update(self):
        self.movement()
        self.collisions()

    def movement(self):
        self.rect.center += self.direction * self.speed
        self.distance += self.speed

    def collisions(self):
        self.duration -= 1
        if self.duration <= 0:
            self.kill()
        if self.rect.centerx < 0:
            self.kill()
        if self.rect.centerx > 800:
            self.kill()
        if self.rect.centery < 0:
            self.kill()
        if self.rect.centery > 800:
            self.kill()

        if pygame.sprite.spritecollide(self, snipets.wall_group, False):
            self.hit_position = self.rect.center
            self.hit_distance = self.distance
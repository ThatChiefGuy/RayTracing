import pygame

import snipets


class Player(pygame.sprite.Sprite):
    def __init__(self, position, radius, color, group):
        super().__init__(group)
        self.base_image = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(self.base_image, color, (radius, radius), radius)
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.direction = pygame.math.Vector2(0, -1)
        self.rotation_speed = 4
        self.speed = 0

    def update(self):
        self.movement()
        self.collisions()

    def movement(self):
        keys = pygame.key.get_pressed()
        self.speed = 0
        if keys[pygame.K_LEFT]:
            self.direction.rotate_ip(-self.rotation_speed)
        if keys[pygame.K_RIGHT]:
            self.direction.rotate_ip(self.rotation_speed)
        if keys[pygame.K_UP]:
            self.speed = 5
        if keys[pygame.K_DOWN]:
            self.speed = -5

        self.rect.center += self.direction * self.speed

    def collisions(self):
        for wall in snipets.wall_group:
            hits = pygame.sprite.collide_rect(self, wall)
            if hits:
                self.rect.center -= self.direction * self.speed

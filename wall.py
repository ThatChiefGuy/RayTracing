import pygame
map = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W..................W",
    "W...WWWWWWWWW......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...W..............W",
    "W...W..............W",
    "W...W.......W......W",
    "W...W.......W......W",
    "W...WWWWWWWWW......W",
    "W...W..............W",
    "WWWWWWWWWWWWWWWWWWWW"]

class Wall(pygame.sprite.Sprite):
    def __init__(self, size, position, group):
        super().__init__(group)
        self.image = pygame.Surface(size)
        self.image.fill("cyan")
        self.rect = self.image.get_rect()
        self.rect.topleft = position
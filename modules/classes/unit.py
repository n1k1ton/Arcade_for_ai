from config import *

class Unit(sprite.Sprite):
    def __init__(self, image_path, x, y, size, speed, hp):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (size,size))
        self.size = size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.hp = hp

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, side):
        if side == 'DOWN':
            self.rect.y += self.speed
        if side == 'UP':
            self.rect.y -= self.speed
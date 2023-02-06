from .enemy import *

class Boss(Enemy):
    direction_hor = "left"
    direction_ver = "down"
    def first(self):
        if self.rect.x <= 0:
            self.direction_hor = "right"
        if self.rect.x >= win_rez_x - self.size:
            self.direction_hor = "left"
        if self.direction_hor == "left":
            self.rect.x -= self.speed
        if self.direction_hor == "right":
            self.rect.x += self.speed
    def second(self):
        if self.rect.y <= 0:
            self.direction_ver = "down"
        if self.rect.y >= win_rez_y / 3:
            self.direction_ver = "up"
        if  self.direction_ver == "down":
            self.rect.y += self.speed
        if  self.direction_ver == "up":
            self.rect.y -= self.speed
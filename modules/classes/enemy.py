from .unit import *

class Enemy(Unit):
    def __init__(self, image_path, x, y, size, speed, hp, give_points):
        super().__init__(image_path, x, y, size, speed, hp)
        self.give_points = give_points
        self.shoted = False
        self.shoted_count = 0


    def killed(self):
       self.image = transform.scale(image.load(os.path.join(MEDIA_DIR,'images/boom.png')),(self.size, self.size))
       self.shoted = True
from .unit import *

class Boost(Unit):
    def __init__(self, image_path, x, y, size, speed, hp, boost_type):
        super().__init__(image_path, x, y, size, speed, hp)
        self.boost_type = boost_type
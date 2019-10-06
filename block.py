import arcade
import random


class Block(arcade.Sprite):

    def __init__(self, x, y):

        super().__init__("images/boxCrate_double.png", (1 + random.randrange(3)) * 0.2)
        self.center_x = x
        self.center_y = y
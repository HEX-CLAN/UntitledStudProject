import random
import arcade
import os
from player import Player

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=0.01)

        self.player = Player()
        self.box_list = arcade.SpriteList()

        self.wall_list = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.wall_list = arcade.SpriteList()

        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("images/boxCrate_double.png", (1 + random.randrange(3)) * 0.2)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)

        arcade.set_background_color(arcade.color.AMAZON)

        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)

    def update(self, delta_time):

        self.physics_engine.update()
        self.player.move_view(self)
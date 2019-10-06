import random
import arcade
import os
from player import Player
from block import Block

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=0.01)

        self.player = Player()
        self.block_list = arcade.SpriteList()
        self.view_bottom = 0
        self.view_left = 0

        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    block = Block(x, y)
                    self.block_list.append(block)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.block_list)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        self.block_list.draw()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key)

    def update(self, delta_time):
        self.physics_engine.update()
        self.player.move_view(self)
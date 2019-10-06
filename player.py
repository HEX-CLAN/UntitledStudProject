import arcade

MOVEMENT_SPEED = 5
VIEWPORT_MARGIN = 350
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Player(arcade.Sprite):

    def __init__(self):

        super().__init__("images/character.png", 0.05)
        self.center_x = 64
        self.center_y = 270

    def on_key_press(self, key):

        if key == arcade.key.UP or key == arcade.key.W:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = MOVEMENT_SPEED

    def on_key_release(self, key):

        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S]:
            self.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.change_x = 0

    def move_view(self, window):

        changed = False

        # Scroll left
        left_bndry = window.view_left + VIEWPORT_MARGIN
        if self.left < left_bndry:
            window.view_left -= left_bndry - self.left
            changed = True

        # Scroll right
        right_bndry = window.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.right > right_bndry:
            window.view_left += self.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = window.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.top > top_bndry:
            window.view_bottom += self.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = window.view_bottom + VIEWPORT_MARGIN
        if self.bottom < bottom_bndry:
            window.view_bottom -= bottom_bndry - self.bottom
            changed = True

        if changed:
            arcade.set_viewport(window.view_left,
                                SCREEN_WIDTH + window.view_left,
                                window.view_bottom,
                                SCREEN_HEIGHT + window.view_bottom)
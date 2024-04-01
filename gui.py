import arcade
from settings import SIZE, BG_COLOR, TILE_SIZE
from logic import Grid


class TicTacToe(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color(BG_COLOR)
        self.grid = None
        self.grid_sprite = arcade.Sprite("assets/grid.png")
        self.grid_sprite.set_position(SIZE / 2, SIZE / 2)

    def setup(self) -> None:
        self.grid = Grid(self)
        self.clear()
        self.grid_sprite.draw()

    def stop(self, winner, draw=False):
        arcade.draw_rectangle_filled(SIZE / 2, SIZE / 2, SIZE, SIZE, (0, 0, 0, 128))
        arcade.draw_text(
            "It's a draw" if draw else f"{winner} wins!",
            0,
            SIZE / 2,
            align="center",
            width=SIZE,
            font_size=32,
            font_name="Kenney Pixel Square",
        )
        arcade.draw_text(
            f"Press R to restart",
            0,
            SIZE / 2 - SIZE / 4,
            align="center",
            width=SIZE,
            font_size=16,
            font_name="Kenney Pixel Square",
        )

    def create_figure(self, tile_index: int, which: str):
        x, y = self.grid.get_tile_center(tile_index)
        figure = arcade.Sprite(f"assets/{which}.png")
        figure.set_position(x, y)
        figure.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        aim = x // TILE_SIZE + (2 - y // TILE_SIZE) * 3
        self.grid.do_move(aim)

    def on_key_press(self, symbol, modifiers):
        if chr(symbol) == "r" and self.grid.stop:
            self.setup()

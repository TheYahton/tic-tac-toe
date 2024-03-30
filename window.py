import arcade
from settings import SIZE, BG_COLOR, TILE_SIZE
from logic import Grid


class Tictactoe(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color(BG_COLOR)
        self.grid = None
        self.move = None
        self.grid_sprite = None
        self.figure_list = None

    def setup(self) -> None:
        self.grid = Grid(self)
        self.grid_sprite = arcade.Sprite("assets/grid.png")
        self.grid_sprite.set_position(SIZE / 2, SIZE / 2)
        self.figure_list = arcade.SpriteList()

    def create_figure(self, tile_index: int, which: str):
        x, y = self.grid.get_tile_center(tile_index)
        figure = arcade.Sprite(f"assets/{which}.png")
        figure.set_position(x, y)
        self.figure_list.append(figure)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        aim = x // TILE_SIZE + (2 - y // TILE_SIZE) * 3
        self.grid.do_move(aim)

    def on_draw(self) -> None:
        self.clear()
        self.grid_sprite.draw()
        self.figure_list.draw()
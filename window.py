import arcade
from settings import SIZE, BG_COLOR, TILE_SIZE
from logic import Grid


class Tictactoe(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color(BG_COLOR)
        self.grid_field = None
        self.move = None
        self.grid = None
        self.figure_list = None

    def setup(self) -> None:
        self.grid_field = Grid()
        self.grid = arcade.Sprite("assets/grid.png")
        self.grid.set_position(SIZE / 2, SIZE / 2)
        self.figure_list = arcade.SpriteList()

    def create_figure(self, x: float, y: float, which: str):
        tile_index = self.grid_field.get_tile_index(x, y)
        x, y = self.grid_field.get_tile_center(index)
        figure = arcade.Sprite(f"assets/{which}.png")
        figure.set_position(x, y)
        self.figure_list.append(figure)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        aim = x // TILE_SIZE + (2 - y // TILE_SIZE) * 3
        self.grid_field.do_move(aim)
        self.create_figure(x, y, self.grid_field.move)

    def on_draw(self) -> None:
        self.clear()
        self.grid.draw()
        self.figure_list.draw()

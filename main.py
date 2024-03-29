import arcade

SIZE = 400
TILE_SIZE = SIZE // 3
GRID_COLOR = 138, 138, 138
BG_COLOR = (51, 51, 51)


class Tictactoe(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color(BG_COLOR)
        self.grid_field = None
        self.move = None
        self.grid = None
        self.figure_list = None

    def setup(self) -> None:
        self.grid_field = ["blank"] * 9  # can be "blank", "cross" or "nought"
        self.move = "cross"  # cross moves first
        self.grid = arcade.Sprite("assets/grid.png")
        self.grid.set_position(SIZE / 2, SIZE / 2)
        self.figure_list = arcade.SpriteList()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        aim = x // TILE_SIZE + (2 - y // TILE_SIZE) * 3
        if self.grid_field[aim] != "blank":
            return
        self.grid_field[aim] = self.move
        self.create_figure(aim)
        self.move = "cross" if self.move == "nought" else "nought"

    def on_draw(self) -> None:
        self.clear()
        self.grid.draw()
        self.figure_list.draw()
    
    def create_figure(self, aim) -> None:
        x = int((aim % 3 + 1 / 2) * SIZE / 3)
        y = int((2 - aim // 3 + 1 / 2) * SIZE / 3)
        match self.move:
            case "nought":
                nought = arcade.Sprite("assets/nought.png")
                nought.set_position(x, y)
                self.figure_list.append(nought)
            case "cross":
                cross = arcade.Sprite("assets/cross.png")
                cross.set_position(x, y)
                self.figure_list.append(cross)


def main():
    game = Tictactoe()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()

import arcade

SIZE = 400
TILE_SIZE = SIZE // 3
GRID_COLOR = 138, 138, 138
GRID_LINE_WIDTH = 5
NOUGHT_COLOR = 253, 71, 85
CROSS_COLOR = 1, 208, 251
DELTA = 20


class Tictactoe(arcade.Window):
    def __init__(self):
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color((51, 51, 51))
        self.grid_field = ["blank"] * 9  # can be "blank", "cross" or "nought"
        self.move = "cross"  # cross moves first

    def draw_grid(self):
        arcade.draw_line(SIZE / 3, 0, SIZE / 3, SIZE, GRID_COLOR, GRID_LINE_WIDTH)
        arcade.draw_line(
            SIZE / 3 * 2, 0, SIZE / 3 * 2, SIZE, GRID_COLOR, GRID_LINE_WIDTH
        )
        arcade.draw_line(0, SIZE / 3, SIZE, SIZE / 3, GRID_COLOR, GRID_LINE_WIDTH)
        arcade.draw_line(
            0, SIZE / 3 * 2, SIZE, SIZE / 3 * 2, GRID_COLOR, GRID_LINE_WIDTH
        )

    @staticmethod
    def draw_nought(x, y):
        arcade.draw_circle_outline(x, y, SIZE / 8, NOUGHT_COLOR, 5)

    @staticmethod
    def draw_cross(x, y):
        arcade.draw_line(
            x + SIZE / 6 - DELTA,
            y + SIZE / 6 - DELTA,
            x - SIZE / 6 + DELTA,
            y - SIZE / 6 + DELTA,
            CROSS_COLOR,
            5,
        )
        arcade.draw_line(
            x - SIZE / 6 + DELTA,
            y + SIZE / 6 - DELTA,
            x + SIZE / 6 - DELTA,
            y - SIZE / 6 + DELTA,
            CROSS_COLOR,
            5,
        )

    def draw_noughts_and_crosses(self):
        for i, value in enumerate(self.grid_field):
            x = (i % 3 + 1/2) * SIZE/3
            y = (2 - i // 3 + 1/2) * SIZE/3
            match value:
                case "nought":
                    self.draw_nought(x, y)
                case "cross":
                    self.draw_cross(x, y)
                case _:
                    pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        aim = x // TILE_SIZE + (2-y // TILE_SIZE) * 3
        if self.grid_field[aim] != "blank":
            return
        self.grid_field[aim] = self.move
        self.move = "cross" if self.move == "nought" else "nought"

    def on_draw(self):
        self.clear()
        self.draw_grid()
        self.draw_noughts_and_crosses()


def main():
    game = Tictactoe()
    game.run()


if __name__ == "__main__":
    main()

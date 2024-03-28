import arcade

SIZE = 400
GRID_COLOR = 138, 138, 138
GRID_LINE_WIDTH = 5


class Tictactoe(arcade.Window):
    def __init__(self):
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color((51, 51, 51))
    
    def draw_grid(self):
        arcade.draw_line(SIZE/3, 0, SIZE/3, SIZE, GRID_COLOR, GRID_LINE_WIDTH)
        arcade.draw_line(SIZE/3*2, 0, SIZE/3*2, SIZE, GRID_COLOR, GRID_LINE_WIDTH)
        arcade.draw_line(0, SIZE/3, SIZE, SIZE/3, GRID_COLOR, GRID_LINE_WIDTH)
        arcade.draw_line(0, SIZE/3*2, SIZE, SIZE/3*2, GRID_COLOR, GRID_LINE_WIDTH)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.draw_grid()


def main():
    game = Tictactoe()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()

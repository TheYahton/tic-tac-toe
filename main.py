import arcade

SIZE = 400


class Tictactoe(arcade.Window):
    def __init__(self):
        super().__init__(SIZE, SIZE, "Tic Tac Toe")
        arcade.set_background_color((51, 51, 51))

    def setup(self):
        pass

    def on_draw(self):
        self.clear()


def main():
    game = Tictactoe()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()

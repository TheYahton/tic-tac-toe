from settings import SIZE, TILE_SIZE, WIN_CONDITIONS


class Grid:
    def __init__(self, window) -> None:
        self.field = ["blank"] * 9  # can be "blank", "cross" or "nought"
        self.player = "cross"  # cross moves first
        self.window = window
        self.stop = False

    def do_move(self, index) -> None:
        if self.stop:
            return
        if self.field[index] != "blank":
            return
        self.field[index] = self.player
        self.window.draw_figure(index, self.player)
        self.check_win()
        self.switch_player()

    def switch_player(self) -> None:
        self.player = "cross" if self.player == "nought" else "nought"

    def get_tile_center(self, grid_index: int) -> list:
        x = int((grid_index % 3 + 1 / 2) * SIZE / 3)
        y = int((2 - grid_index // 3 + 1 / 2) * SIZE / 3)
        return x, y

    def get_tile_index(self, x, y) -> int:
        return x // TILE_SIZE + (2 - y // TILE_SIZE) * 3

    def is_win(self) -> list | bool:
        fun = lambda a, b, c: self.field[a] == self.field[b] == self.field[c] != "blank"
        for win in WIN_CONDITIONS:
            if fun(*win):
                return win
        return False

    def is_draw(self) -> bool:
        return "blank" not in self.field

    def check_win(self) -> None:
        if self.is_win() or self.is_draw():
            self.stop = True
            self.window.end(self.is_win(), self.is_draw())

from settings import SIZE, TILE_SIZE, WIN_CONDITIONS


class Grid:
    def __init__(self, window):
        self.field = ["blank"] * 9  # can be "blank", "cross" or "nought"
        self.current_player = "cross"  # cross moves first
        self.window = window
        self.stop = False

    def do_move(self, index):
        if self.stop:
            return
        if self.field[index] != "blank":
            return
        self.field[index] = self.current_player
        self.window.create_figure(index, self.current_player)
        self.check_win()
        self.switch_player()
    
    def switch_player(self):
        self.current_player = "cross" if self.current_player == "nought" else "nought"

    def get_tile_center(self, grid_index: int) -> list:
        x = int((grid_index % 3 + 1 / 2) * SIZE / 3)
        y = int((2 - grid_index // 3 + 1 / 2) * SIZE / 3)
        return x, y

    def get_tile_index(self, x, y):
        return x // TILE_SIZE + (2 - y // TILE_SIZE) * 3

    def is_win(self):
        fun = lambda a, b, c: self.field[a] == self.field[b] == self.field[c] != "blank"
        for win in WIN_CONDITIONS:
            if fun(*win):
                return win

    def is_draw(self):
        if "blank" not in self.field:
            return True

    def check_win(self):
        if self.is_win() or self.is_draw():
            self.stop = True
            self.window.stop(self.current_player, self.is_draw())

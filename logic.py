from settings import SIZE, TILE_SIZE


class Grid:
    def __init__(self, window):
        self.field = ["blank"] * 9  # can be "blank", "cross" or "nought"
        self.move = "cross"  # cross moves first
        self.window = window

    def do_move(self, index):
        if self.field[index] != "blank":
            return
        self.field[index] = self.move
        self.window.create_figure(index, self.move)
        self.move = "cross" if self.move == "nought" else "nought"

    def get_tile_center(self, grid_index: int) -> list:
        x = int((grid_index % 3 + 1 / 2) * SIZE / 3)
        y = int((2 - grid_index // 3 + 1 / 2) * SIZE / 3)
        return x, y

    def get_tile_index(self, x, y):
        return x // TILE_SIZE + (2 - y // TILE_SIZE) * 3

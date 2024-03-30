from settings import SIZE, TILE_SIZE


class Grid:
    def __init__(self, window):
        self.grid_field = ["blank"] * 9  # can be "blank", "cross" or "nought"
        self.move = "cross"  # cross moves first

    def do_move(self, index):
        if self.grid_field[index] != "blank":
            return
        self.grid_field[index] = self.move
        self.move = "cross" if self.move == "nought" else "nought"

    def get_tile_center(self, grid_index: int) -> list:
        x = int((aim % 3 + 1 / 2) * SIZE / 3)
        y = int((2 - aim // 3 + 1 / 2) * SIZE / 3)
        return x, y

    def get_tile_index(self, x, y):
        return x // TILE_SIZE + (2 - y // TILE_SIZE) * 3

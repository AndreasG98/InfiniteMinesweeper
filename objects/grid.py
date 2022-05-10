# from . import Square
from objects.square import Square
from math import floor


class Grid:
    def __init__(self, initial_x, initial_y, px_size):

        # Dimensions in pixels
        self.x_width = initial_x
        self.y_width = initial_y
        self.px_size = px_size

        # Dimensions in squares
        self.x_squares = floor(self.y_width / px_size)
        self.y_squares = floor(self.y_width / px_size)

        self.square_count = self.x_squares * self.y_squares
        self.clicked_squares = 0
        self.mine_count = 0

        self.grid = []

        for i in range(self.x_squares):
            curr_col = []
            for j in range(self.y_squares):
                square_x = i * px_size
                square_y = j * px_size
                new_square = Square(i, j, square_x, square_y)
                curr_col.append(new_square)

                if new_square.type == 'mine':
                    self.mine_count += 1

                # print(new_square.to_string())
            self.grid.append(curr_col)

    def print_grid(self, surface):
        for col in self.grid:
            for square in col:
                if square.status == 'hidden' or square.status == 'number':
                    square.draw(surface)
                elif square.type == 'mine':
                    square.draw(surface)

    def pixel_to_index(self, coordinate):
        return floor(coordinate / self.px_size)

    def click(self, left_mouse, mouse_x, mouse_y):
        square_x = self.pixel_to_index(mouse_x)
        square_y = self.pixel_to_index(mouse_y)

        ret = self.grid[square_x][square_y].click(left_mouse)

        if self.grid[square_x][square_y].type == 'clicked':
            self.clicked_squares += 1

        return ret

    def check_remaining(self):
        return self.square_count - self.mine_count - self.clicked_squares



    def check_coordinate(self, coord_x, coord_y):
        square_x = self.pixel_to_index(coord_x)
        square_y = self.pixel_to_index(coord_y)

        count = 0

        for i in range(square_x - 1, square_x + 2):
            for j in range(square_y - 1, square_y + 2):

                if i == square_x and j == square_y:
                    continue

                if self.x_squares - 1 < i or i < 0:
                    continue
                if self.y_squares - 1 < j or j < 0:
                    continue

                # print("Checking coordinate",square_x, square_y, i, j)

                # if self.x_squares < square_x + i < 0 or self.y_squares < square_y + j < 0:
                #     continue

                # print("Checking mine")

                if self.grid[i][j].type == 'mine':
                    # print("Mine found at", i , j)
                    count += 1

        if not self.grid[square_x][square_y].flag:
            self.grid[square_x][square_y].adjacent_mines = count

            if count != 0:
                self.grid[square_x][square_y].status = 'number'
                self.grid[square_x][square_y].set_image("number_" + str(count))

        # print("Square at", square_x, square_y, "has adjacent", count, self.grid[square_x][square_y].adjacent_mines)

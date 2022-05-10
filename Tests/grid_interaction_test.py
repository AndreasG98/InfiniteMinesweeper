import time

import pygame
from time import sleep

from math import floor

# self.surface.blit(item.image, (item.x, item.y))
# pygame.display.flip()

WINDOW_X = 800
WINDOW_Y = 800
PX_SIZE = 40


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Infinite Minesweeper")
        pygame.mixer.init()

        self.surface = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

        self.grid = Grid(800, 800)

        # self.square = Square(0, 0)

        self.click_time = None
        self.click_x = None
        self.click_x = None

        self.screen_dragging = False
        self.drag_start_x = None
        self.drag_start_y = None

        self.drag_offset_x = 0
        self.drag_offset_y = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_up(event)

            self.draw_frame()
            sleep(0.1)

    def mouse_down(self, event):
        self.click_time = time.time()
        self.click_x, self.click_y = event.pos

    def mouse_up(self, event):
        clicked_time = time.time() - self.click_time
        if clicked_time < 0.2:

            self.single_click()

        self.click_time = None
        self.click_x = None
        self.click_y = None

    def single_click(self):
        print("Single click", self.click_x, self.click_y)
        self.grid.check_click(self.grid, self.click_x, self.click_y)


    def log_key(self):
        print("kyup")

    def draw_frame(self):
        self.render_background("Mosaic_Background")
        self.grid.print_grid(self.surface)
        # self.surface.blit(self.square.image, (self.square.x - self.drag_offset_x, self.square.y - self.drag_offset_y))
        pygame.display.flip()

    def render_background(self, filename):
        bg = pygame.image.load(f"../resources/{filename}.jpg")
        self.surface.blit(bg, (0, 0))


class Square:

    types = ['safe', 'mine', 'flag', 'number_1']

    def __init__(self, grid_x, grid_y, initial_x, initial_y):
        self.image = pygame.image.load("../resources/mine.jpg").convert()

        self.grid_x = grid_x
        self.grid_y = grid_y

        self.x = initial_x
        self.y = initial_y
        self.type = None

        self.clicked = False

    def to_string(self):
        print("Square", self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def click(self, grid, click_x, click_y):
        if self.type == 'safe':
            self.remove(grid)

    def remove(self, grid, click_x, click_y):
        pass




class Grid:
    def __init__(self, initial_x, initial_y):
        # Dimensions in pixels
        self.x_width = initial_x
        self.y_width = initial_y

        self.x_squares = floor(self.y_width / PX_SIZE)
        self.y_squares = floor(self.y_width / PX_SIZE)

        self.grid = []

        print("Total X Squares", self.x_squares)
        for i in range(self.x_squares):
            curr_col = []
            for j in range(self.y_squares):
                square_x = i * PX_SIZE
                square_y = j * PX_SIZE
                new_square = Square(i, j, square_x, square_y)
                curr_col.append(new_square)
                print(new_square.to_string())
            self.grid.append(curr_col)

    def print_grid(self, surface):
        for col in self.grid:
            for square in col:
                if not square.clicked:
                    square.draw(surface)

    def check_click(self, grid, mouse_x, mouse_y):
        square_x = floor(mouse_x / PX_SIZE)
        square_y = floor(mouse_y / PX_SIZE)
        print("Square at", square_x, square_y)
        self.grid[square_x][square_y].clicked = True

    def remove_square(self, x, y):
        pass


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

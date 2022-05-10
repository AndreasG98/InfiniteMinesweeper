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

        self.grid = Grid(0,0)

        self.square = Square(0, 0)

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
                    # Start dragging
                    self.start_drag(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Stop dragging
                    self.end_drag(event)
                elif self.screen_dragging:
                    self.continue_drag(event)

            print("Dragging", self.screen_dragging, self.drag_offset_x, self.drag_offset_y)

            self.draw_frame()
            sleep(0.1)

    def start_drag(self, event):
        self.screen_dragging = True
        self.drag_start_x, self.drag_start_y = event.pos
        # print("Start drag", self.drag_start_x, self.drag_start_y)

    def end_drag(self, event):
        self.screen_dragging = False
        self.drag_start_x = self.drag_start_y = None
        # print("End drag", self.drag_start_x, self.drag_start_y)

    def continue_drag(self, event):
        curr_x, curr_y = pygame.mouse.get_pos()

        rel_x = curr_x - self.drag_start_x
        rel_y = curr_y - self.drag_start_y

        self.drag_offset_x -= rel_x
        self.drag_offset_y -= rel_y
        # print("Continue drag", self.drag_offset_x, self.drag_offset_y)



    def draw_frame(self):
        self.render_background("Mosaic_Background")



        self.surface.blit(self.square.image, (self.square.x - self.drag_offset_x, self.square.y - self.drag_offset_y))
        pygame.display.flip()


    def render_background(self, filename):
        bg = pygame.image.load(f"resources/{filename}.jpg")
        self.surface.blit(bg, (0, 0))

class Square:
    def __init__(self, initial_x, initial_y):
        self.image = pygame.image.load("../resources/mine.jpg").convert()
        self.x = initial_x
        self.y = initial_y

class Grid:
    def __init__(self, initial_x, initial_y):
        # Dimensions in pixels
        self.x_width = initial_x
        self.y_width = initial_y

        self.x_squares = floor(self.y_width / PX_SIZE)
        self.y_squares = floor(self.y_width / PX_SIZE)

        self.grid = [[PX_SIZE] * self.y_squares] * self.x_squares

        for row in self.grid:
            print(row)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

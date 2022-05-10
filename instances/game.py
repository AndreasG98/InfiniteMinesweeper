import pygame
from time import time, sleep
from math import floor

from objects.grid import Grid

import objects
import utils


class Game:

    def __init__(self, window_x, window_y, px_size):
        # PyGame Init
        pygame.init()
        pygame.display.set_caption("Infinite Minesweeper")
        pygame.mixer.init()

        # Save parameters
        self.window_x = window_x
        self.window_y = window_y
        self.px_size = px_size

        # Set up render surface
        self.surface = pygame.display.set_mode((window_x, window_y))

        # Set up objects
        self.grid = Grid(window_x, window_y, px_size)

        # For checking if mouse event is a click or drag
        self.click_time = None
        self.click_x = None
        self.click_y = None
        self.left_click = None

        # self.screen_dragging = False
        # self.drag_start_x = None
        # self.drag_start_y = None

        # self.drag_offset_x = 0
        # self.drag_offset_y = 0

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
        self.left_click = False
        if event.button == 1:
            self.left_click = True
        self.click_time = time()
        self.click_x, self.click_y = event.pos

    def mouse_up(self, event):
        clicked_time = time() - self.click_time
        if clicked_time < 0.2:
            self.single_click()

        self.click_time = None
        self.click_x = None
        self.click_y = None
        self.left_click = None

    def single_click(self):
        ret = self.grid.click(self.left_click, self.click_x, self.click_y)

        if ret:
            self.grid.check_coordinate(self.click_x, self.click_y)
            # print("Success")
        else:
            print("GAME OVER")

        if self.grid.check_remaining() == 0:
            print("Win!")

    def draw_frame(self):
        self.render_background("Mosaic_Background")
        self.grid.print_grid(self.surface)
        # self.surface.blit(self.square.image, (self.square.x - self.drag_offset_x, self.square.y - self.drag_offset_y))
        pygame.display.flip()

    def render_background(self, filename):
        bg = pygame.image.load(f"resources/{filename}.jpg")
        self.surface.blit(bg, (0, 0))

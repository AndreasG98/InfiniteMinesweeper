import pygame
from random import randint

class Square:

    # type = ['safe', 'mine']
    # status = ['hidden', 'clicked']

    def __init__(self, grid_x, grid_y, initial_x, initial_y):
        self.image = None
        self.set_image("hidden")

        self.grid_x = grid_x
        self.grid_y = grid_y

        self.x = initial_x
        self.y = initial_y

        self.type = ''
        self.status = 'hidden'
        self.flag = False
        self.adjacent_mines = None

        self.assign_type()

    def set_image(self, image):
        # print("set image", image)
        self.image = pygame.image.load(f"./resources/{image}.jpg").convert()

    def assign_type(self):
        rand = randint(0, 100)
        if rand < 10:
            self.type = 'mine'
        else:
            self.type = 'safe'

    def toggle_flag(self):
        if self.flag:
            self.flag = False
            self.set_image("hidden")
        else:
            self.flag = True
            self.set_image("flag")

    def click(self, left_mouse=True):

        # print("click. adjacent:", self.adjacent_mines)

        # The square has already been clicked
        if self.status == 'clicked':
            # print("A")
            return True

        # Right click toggles the flag
        if not left_mouse:
            # print("B")
            self.toggle_flag()
            return True

        # Left click clicks a square

        # Set the square to clicked
        self.status = 'clicked'

        # Revealed a safe square
        if self.type == 'safe':
            return True

        # Revealed a mine
        self.set_image("mine")

        return False

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

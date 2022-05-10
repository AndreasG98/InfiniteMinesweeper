import pygame

# self.surface.blit(item.image, (item.x, item.y))
# pygame.display.flip()


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Infinite Minesweeper")
        pygame.mixer.init()

    def run(self):
        pass


class Grid:
    def __init__(self, initial_x, initial_y):
        self.x_width = initial_x
        self.y_width = initial_y


class Mine:
    def __init__(self, surface):
        self.image = pygame.image.load("resources/mine_image.jpg").convert()
        self.parent_screen = surface
        self.x_coordinate = None
        self.y_coordinate = None


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

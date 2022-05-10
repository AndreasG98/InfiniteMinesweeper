from instances.game import Game

WINDOW_X = 800
WINDOW_Y = 800
PX_SIZE = 40


def main():
    game = Game(WINDOW_X, WINDOW_Y, PX_SIZE)
    game.run()


if __name__ == '__main__':
    main()

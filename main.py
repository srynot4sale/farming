import math
import pygame

import system
import mode.play


def main():
    app = system.system()
    app.setup()

    app.switch_mode(mode.play.play())
    app.run()


if __name__ == "__main__":
    main()

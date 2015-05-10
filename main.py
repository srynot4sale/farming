import math
import pygame

import system
import mode.menu
import mode.play


def main():
    app = system.system()
    app.setup()

    #app.switch_mode(mode.play.play())
    app.switch_mode(mode.menu.menu())
    app.run()


if __name__ == "__main__":
    main()

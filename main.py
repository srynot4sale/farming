import math
import pygame

import person

NAME = 'Rylee\'s game'
MAX_X = 1024
MAX_Y = 768

DEBUG = 1

def main():

    screen = pygame.display.set_mode((MAX_X, MAX_Y))
    clock = pygame.time.Clock()
    pygame.display.set_caption(NAME)
    pygame.font.init()

    rect = screen.get_rect()
    p = person.person('sprites/maleprotagonist.png', rect.center)

    font = pygame.font.Font(None, 24)

    try:
        running = True

        while running:
            # USER INPUT
            deltat = clock.tick(30) # 30fps

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                if not hasattr(event, 'key'):
                    continue

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        p.queue(p.move_right)

                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        p.queue(p.move_left)

                    elif event.key in (pygame.K_UP, pygame.K_w):
                        p.queue(p.move_up)

                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        p.queue(p.move_down)

                    elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                        running = False
                        break

            if not running:
                continue

            # RENDERING
            screen.fill((100,100,255))
            p.update(deltat, screen)

            text = font.render("X: %d" % p.x, 1, (100, 100, 100))
            screen.blit(text, (10, 50))

            text = font.render("Y: %d" % p.y, 1, (100, 100, 100))
            screen.blit(text, (10, 70))

            pygame.display.flip()

        pygame.quit()

    except SystemExit:
        pygame.quit()

if __name__ == "__main__":
    main()

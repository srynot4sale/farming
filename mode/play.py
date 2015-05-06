import pygame

import mode
import person


class play(mode.base):

    def setup(self, app):
        rect = app.screen.get_rect()
        self.p = person.person('sprites/maleprotagonist.png', rect.center)

    def events(self, app):
        p = self.p

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.stop()
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
                    app.stop()
                    break

    def render(self, app):
        p = self.p

        app.screen.fill((100,100,255))
        p.update(app.deltat, app.screen)

        text = app.font.render("X: %d" % p.x, 1, (100, 100, 100))
        app.screen.blit(text, (10, 50))

        text = app.font.render("Y: %d" % p.y, 1, (100, 100, 100))
        app.screen.blit(text, (10, 70))

        pygame.display.flip()

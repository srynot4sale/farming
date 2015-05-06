import pygame

import mode
import person


class play(mode.base):
    def setup(self, app):
        self.app = app
        rect = self.app.screen.get_rect()
        self.p = person.person('sprites/maleprotagonist.png', rect.center)

    def event(self, event):
        p = self.p

        if not hasattr(event, 'key'):
            return

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
                self.app.stop()

    def render(self):
        p = self.p
        app = self.app

        app.screen.fill((100,100,255))
        p.update(app.deltat, app.screen)

        text = app.font.render("X: %d" % p.x, 1, (100, 100, 100))
        app.screen.blit(text, (10, 50))

        text = app.font.render("Y: %d" % p.y, 1, (100, 100, 100))
        app.screen.blit(text, (10, 70))

        pygame.display.flip()

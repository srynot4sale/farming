import pygame


NAME = "Rylee's game"

MAX_X = 1024
MAX_Y = 768


class system(object):

    screen = None
    clock = None
    font = None

    # Current game mode
    mode = None

    # Flag telling system whether it is running or not
    __running = True

    def setup(self):

        self.screen = pygame.display.set_mode((MAX_X, MAX_Y))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(NAME)
        pygame.font.init()

        self.font = pygame.font.Font(None, 24)

    def running(self):
        return self.__running

    def stop(self):
        self.__running = False

    def switch_mode(self, mode):
        self.mode = mode
        self.mode.setup(self)

    def run(self):
        try:
            while self.running():
                self.deltat = self.clock.tick(30) # 30fps

                # Look for quit events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        app.stop()
                        break

                    self.mode.event(event)

                if not self.running():
                    continue

                self.mode.render()

        except SystemExit:
            pass
#        except Exception:
 #           print('exception!')
        finally:
            pygame.quit()


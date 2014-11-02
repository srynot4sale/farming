import math
import pygame

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
    c = person('sprites/maleprotagonist.png', rect.center)
    car_group = pygame.sprite.RenderPlain(c)

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
                        c.move_right()

                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        c.move_left()

                    elif event.key in (pygame.K_UP, pygame.K_w):
                        c.move_up()

                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        c.move_down()

                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        break

            if not running:
                continue

            # RENDERING
            screen.fill((100,100,255))
            car_group.update(deltat)
            car_group.draw(screen)

    #        text = font.render("Speed: %d" % c.speed, 1, (100, 100, 100))
    #        screen.blit(text, (10, 10))

    #        text = font.render("Direction: %d" % c.direction, 1, (100, 100, 100))
    #        screen.blit(text, (10, 30))

            text = font.render("X: %d" % c.x, 1, (100, 100, 100))
            screen.blit(text, (10, 50))

            text = font.render("Y: %d" % c.y, 1, (100, 100, 100))
            screen.blit(text, (10, 70))

            pygame.display.flip()

        pygame.quit()

    except SystemExit:
        pygame.quit()


class person(pygame.sprite.Sprite):

    increment = 28
    x = 0
    y = 0

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        size = self.src_image.get_rect().size
        self.src_image = pygame.transform.chop(self.src_image, (0, 0, size[0]-self.increment, size[1]-self.increment))
        self.x = position[0]
        self.y = position[1]

    def move_up(self):
        self.y -= self.increment

    def move_down(self):
        self.y += self.increment

    def move_left(self):
        self.x -= self.increment
    
    def move_right(self):
        self.x += self.increment

    def update(self, deltat):
        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


if __name__ == "__main__":
    main()

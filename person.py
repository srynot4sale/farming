import pygame

DOWN    = 'd'
UP      = 'u'
LEFT    = 'l'
RIGHT   = 'r'

class person(pygame.sprite.Sprite):

    size = 32
    increment = 32
    sprites = {
        DOWN:   (0,32),
        UP:     (0,0),
        LEFT:   (0,64),
        RIGHT:  (0,96)
    }

    src_image = None
    x = 0
    y = 0
    direction = DOWN

    action_queue = []

    renderer = None

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        self.src_image = pygame.image.load(image)

        self.x = position[0]
        self.y = position[1]
        self.direction = DOWN

        self.action_queue = []

        self.renderer = pygame.sprite.RenderPlain(self)

    def queue(self, action):
        self.action_queue.append(action)

    def move_up(self):
        self.y -= self.increment
        self.direction = UP

    def move_down(self):
        self.y += self.increment
        self.direction = DOWN

    def move_left(self):
        self.x -= self.increment
        self.direction = LEFT

    def move_right(self):
        self.x += self.increment
        self.direction = RIGHT

    def update(self, deltat, screen):

        # Do next action in queue
        if len(self.action_queue):
            action = self.action_queue.pop()
            action()

        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.image.blit(self.src_image, (0, 0), (self.sprites[self.direction][0], self.sprites[self.direction][1], self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        screen.blit(self.image, self.rect)

import pygame

class person(pygame.sprite.Sprite):

    src_image = None

    increment = 32
    x = 0
    y = 0

    action_queue = []

    renderer = None

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load(image)
        size = image.get_rect().size
        self.src_image = pygame.transform.chop(image, (0, 0, size[0]-self.increment, size[1]-self.increment))

        self.x = position[0]
        self.y = position[1]
   
        self.action_queue = []

        self.renderer = pygame.sprite.RenderPlain(self)

    def queue(self, action):
        self.action_queue.append(action)

    def move_up(self):
        self.y -= self.increment

    def move_down(self):
        self.y += self.increment

    def move_left(self):
        self.x -= self.increment
    
    def move_right(self):
        self.x += self.increment

    def update(self, deltat, screen):

        # Do next action in queue
        if len(self.action_queue):
            action = self.action_queue.pop()
            action()

        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.renderer.draw(screen)

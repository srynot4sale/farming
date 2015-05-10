import pygame

import mode
import system


class menu(mode.base):

    header = 'Main menu'

    options = [
        ('New game', 240),
        ('Continue', 280),
        ('Settings', 320),
        ('Quit',     360),
    ]

    selection = 0
    image = {}

    def setup(self, app):
        self.app = app
        self.image['firby_purple'] = pygame.image.load('sprites/firby_purple.jpg')
        self.image['cartoon_person'] = pygame.image.load('sprites/cartoon_person.jpg')

    def event(self, event):
        if not hasattr(event, 'key'):
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.selection > 0:
                    self.selection -= 1

            elif event.key == pygame.K_DOWN:
                if self.selection < (len(self.options) - 1):
                    self.selection += 1

            elif event.key == pygame.K_RETURN:
                if self.selection == 3:
                    self.app.stop()

    def update(self):
        pass

    def __get_centered(self, width):
        s_width = self.app.screen.get_width()
        return (s_width / 2) - (width / 2)

    def render(self):
        self.app.screen.fill((81,232,177))

        font = pygame.font.Font(None, 75)
        text = font.render(system.NAME, 1, (100, 100, 100))
        self.app.screen.blit(text, (self.__get_centered(text.get_width()), 50))

        font = pygame.font.Font(None, 45)
        text = font.render(self.header, 1, (100, 100, 100))
        self.app.screen.blit(text, (self.__get_centered(text.get_width()), 120))

        font = pygame.font.Font(None, 36)
        o = 0
        for option in self.options:
            text, location = option

            if self.selection == o:
                text = font.render(text, 1, (0, 0, 0))
            else:
                text = font.render(text, 1, (100, 100, 100))

            self.app.screen.blit(text, (self.__get_centered(text.get_width()), location))
            o += 1

        self.rect = self.image['firby_purple'].get_rect()
        self.rect.center = (200, 200)
        self.app.screen.blit(self.image['firby_purple'], self.rect)

        self.rect = self.image['cartoon_person'].get_rect()
        self.rect.center = (600, 600)
        self.app.screen.blit(self.image['cartoon_person'], self.rect)

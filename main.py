import pygame

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Sokoban:

    def load_images(self):
        for name in ['floor', 'wall', 'target', 'box', 'robo', 'ready', 'target_robo']:
            self.images.append(pygame.image.load(name + 'png'))

    def new_game(self):
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def loop(self):
        self.running = True
        while self.running:
            self.check_events()
            self.draw_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

                if event.key == K_LEFT:
                    self.move(-1, 0)
                if event.key == K_RIGHT:
                    self.move(1, 0)
                if event.key == K_UP:
                    self.move(0, -1)
                if event.key == K_DOWN:
                    self.move(0, 1)

    def move(self, move_x: int, move_y: int):
        robo_x, robo_y = self.find_robo()
        robo_x += move_x
        robo_y += move_y

        if self.map[robo_y][robo_x] == 1:
            return

        if self.map[robo_y][robo_x] in [3, 5]:
            box_x = robo_x + move_x
            box_y = robo_y + move_y

            if self.map[box_y][box_x] in [1, 3, 5]:
                return

            self.map[robo_y][robo_x] -= 3
            self.map[box_y][box_x] += 3

        self.map[robo_y - move_y][robo_x - move_x] -= 4
        self.map[robo_y][robo_x] += 4

    def draw_screen(self):
        self.screen.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                frame = self.map[y][x]
                self.screen.blit(self.images[frame], (x * self.scale, y * self.scale))

        pygame.display.flip()

    def find_robo(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return x, y

    def __init__(self):
        pygame.init()

        self.images = []
        self.map = []
        self.running = False

        self.load_images()
        self.new_game()

        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()

        screen_width = self.scale * self.height
        screen_height = self.scale * self.width

        self.screen = pygame.display.set_mode((screen_width, screen_height))

        pygame.display.set_caption(')-( SOKOBAN )-(')

        self.loop()


if __name__ == '__main__':
    Sokoban()

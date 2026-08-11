import pygame
from constants import *
from logger import log_state
from player import Player

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    #use groupings for easier management of updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for event in pygame.event.get():
            pass

        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

import pygame
from constants import *

def main():
    initRestuls = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags = pygame.SCALED)
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill("black")
        pygame.display.flip()


        dt = clock.tick(60)/1000


    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


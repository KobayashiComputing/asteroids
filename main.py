import pygame
from constants import *
from player import *

def main():
    initRestuls = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags = pygame.SCALED)
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill("black")
        player1.draw(screen)
        player1.update(dt)
        pygame.display.flip()


        dt = clock.tick(60)/1000


    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


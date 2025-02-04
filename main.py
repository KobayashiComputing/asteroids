import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    initRestuls = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    asteroidfield1 = AsteroidField()
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags = pygame.SCALED)
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill("black")
        # player1.update(dt)
        updatable.update(dt)
        # now check for collisions
        for a in asteroids:
            if a.collision(player1):
                print("Game over")
                exit()
        
        # player1.draw(screen)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


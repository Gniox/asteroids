import pygame
import sys

from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        for asteroid in asteroids:
            if(asteroid.hasCollided(player)):
                print("Game over!")
                sys.exit(1)
        for shot in shots:
            for asteroid in asteroids:
                if shot.hasCollided(asteroid):
                    print(len(shots))
                    print("hit an asteroid!")
                    asteroid.split()
                    shot.kill()


        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)
             
        pygame.display.flip()

        time_elapsed = clock.tick(60)

        dt = time_elapsed / 1000

if __name__ == "__main__":
    main()

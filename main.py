import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    projectiles = AsteroidField()
    Shot.containers = (updateable, drawable)

    
    print("Starting asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        for item in updateable:
            item.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                sys.exit("Game Over!")

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
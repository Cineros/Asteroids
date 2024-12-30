import pygame
from constants import *
def main():
    pygame.init()
    game_clock = pygame.time.Clock
    dt = 0
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60)/1000
    

if __name__ == "__main__":
    main()
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        log_state()

        # if user closes the window, kill the process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # black background fill
        screen.fill((0, 0, 0))

        # update all updatable objects
        updatable.update(dt)

        # loop through drawable objects and draw them individually
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
    
        delta = clock.tick(60)
        dt = delta / 1000
        

if __name__ == "__main__":
    main()

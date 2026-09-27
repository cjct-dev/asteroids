import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import sys



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x, y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(x, y)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        #print(dt)



if __name__ == "__main__":
    clock = pygame.time.Clock()
    dt = 0.0
    main()

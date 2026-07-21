@ -0,0 +1,8 @@
import pygame

class Bullet:
    def __init__(self, screen, position):
        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000

        pygame.draw.circle(screen)
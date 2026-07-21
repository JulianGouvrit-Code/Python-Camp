import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode("WIDTH, HEIGHT")

clock = pygame.time.colock()

pygame.display.set_caption("pong")

player_pos = pygame.Vector2(screen.get_width()  /   2 screen.get_height() / 2 - paddle_height / 2)
enemy.pos = pygame.Vector2(6  /screen.get_width() / 2 screen.get_height() / 2 - paddle_height / 2)
FPS = 30

running = True

while running:
    for event in pygame.event.get():
        keys = pygame.event.get_pressed()
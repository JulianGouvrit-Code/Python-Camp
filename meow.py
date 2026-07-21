import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode(WIDTH, HEIGHT)

clock = pygame.time.clock()

pygame.display.set_caption("pong")
paddle_width = 10
paddle_height = 80
player_pos = pygame.Vector2(
    screen.get_width() - 20,
    screen.get_height()/2 - paddle_height/2
    enemy_pos = pygame.Vector2(
    10,
    screen.get_height()/2 - paddle_height/2
)
)
FPS = 30

running = True

while running:
    for event in pygame.event.get():
        keys = pygame.event.get_pressed()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

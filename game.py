import pygame
import random
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("collector")

score = 0

player = pygame.image.load("images/tripleT.png")
player = pygame.transform.scale(player, (50, 50))

pygame.mixer.init()
collect_sound = pygame.mixer.Sound("tripletT.mp3")

collectable = pygame.image.load("images/wood bat.png")
collectable = pygame.transform.scale(collectable, (30, 30))

enemy =     pygame.image.load("images/67.png")
enemy = pygame.transform.scale(enemy, (50, 50))

enemy_position_x = 500 - 50
enemy_position_y = 500 - 50

collectable_x = random.randrange(0, 500 - 50)
collectable_y = random.randrange(0, 500 - 50)

player_move_x = 1
player_move_y = 0
player_position_x = 0
player_position_y = 0

pygame.font.init()
font = pygame.font.Font("font.ttf")

clock = pygame.time.Clock()
running = True
while running:

    pygame.display.flip()


    window.fill((5, 0, 0))
    window.blit(enemy, (enemy_position_x, enemy_position_y))
    window.blit(player, (player_position_x, player_position_y))
    window.blit(collectable, (collectable_x, collectable_y))

    if enemy_position_x > player_position_x:
        enemy_position_x -= 1

    if enemy_position_x < player_position_x:
        enemy_position_x += 1

    if enemy_position_y > player_position_y:
        enemy_position_y -= 1

    if enemy_position_y < player_position_y:
        enemy_position_y += 1

    draw_score = font.render(str(score), True, (255, 255, 255))
    window.blit(draw_score, (0, 0))

    player_hitbox = player.get_rect()
    player_hitbox.x = player_position_x
    player_hitbox.y = player_position_y
    collectable_hitbox = collectable.get_rect()
    collectable_hitbox.x = collectable_x
    collectable_hitbox.y = collectable_y
    if player_hitbox.colliderect(collectable_hitbox):
        collectable_x = random.randrange(0, 500 - 50)
        collectable_y = random.randrange(0, 500 - 50)

        score += 1

        collect_sound.play()

    enemy_hitbox = enemy.get_rect()
    enemy_hitbox.x = enemy_position_x
    enemy_hitbox.y = enemy_position_y
    if enemy_hitbox.colliderect(player_hitbox):
        running = False
    

    player_position_x += player_move_x
    player_position_y += player_move_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_move_x = 0
        player_move_y = -1.9
    if keys[pygame.K_s]:
        player_move_x = 0
        player_move_y = 1.9
    if keys[pygame.K_a]:
        player_move_x = -1.9
        player_move_y = 0
    if keys[pygame.K_d]:
        player_move_x = 1.9
        player_move_y = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    clock.tick(60)
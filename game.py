import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя игра")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

def reset_game():
    global x, y, enemy_x, enemy_y, enemy_speed_x, enemy_speed_y, game_over, score, start_time
    x = 400
    y = 300
    enemy_x = random.randint(50, 750)
    enemy_y = random.randint(50, 550)
    enemy_speed_x = 0.3
    enemy_speed_y = 0.3
    game_over = False
    score = 0
    start_time = time.time()

x = 400
y = 300
speed = 0.5
enemy_x = random.randint(50, 750)
enemy_y = random.randint(50, 550)
enemy_speed_x = 0.3
enemy_speed_y = 0.3
game_over = False
score = 0
start_time = time.time()

font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 36)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()
    
    if not game_over:
        score = int(time.time() - start_time)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        
        if x < 0:
            x = 0
        if x > 750:
            x = 750
        if y < 0:
            y = 0
        if y > 550:
            y = 550
        
        enemy_x += enemy_speed_x
        enemy_y += enemy_speed_y
        
        if enemy_x <= 0:
            enemy_x = 0
            enemy_speed_x = -enemy_speed_x
        if enemy_x >= 750:
            enemy_x = 750
            enemy_speed_x = -enemy_speed_x
        if enemy_y <= 0:
            enemy_y = 0
            enemy_speed_y = -enemy_speed_y
        if enemy_y >= 550:
            enemy_y = 550
            enemy_speed_y = -enemy_speed_y
        
        player_rect = pygame.Rect(x, y, 50, 50)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
        
        if player_rect.colliderect(enemy_rect):
            game_over = True
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 50, 50))
    
    score_text = small_font.render(f"Очки: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        text = font.render("ТЫ ПРОИГРАЛ!", True, BLACK)
        screen.blit(text, (200, 220))
        
        score_text = small_font.render(f"Твой счёт: {score}", True, BLACK)
        screen.blit(score_text, (300, 290))
        
        restart_text = small_font.render("Нажми R, чтобы начать заново", True, BLACK)
        screen.blit(restart_text, (220, 340))
    
    pygame.display.flip()

pygame.quit()
import pygame
import sys
import random

# 초기화
pygame.init()

# 한글 폰트 설정
try:
    font = pygame.font.Font('malgun.ttf', 48)  # 맑은 고딕
except:
    font = pygame.font.SysFont('arial', 48)    # 폰트가 없을 경우 기본 폰트

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),    # 빨강
    (255, 128, 0),  # 주황
    (255, 255, 0),  # 노랑
    (0, 255, 0),    # 초록
    (0, 128, 255),  # 하늘
    (0, 0, 255),    # 파랑
    (255, 0, 255)   # 분홍
]
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 패들
PADDLE_WIDTH = 300
PADDLE_HEIGHT = 15
paddle = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_SPEED = 8

# 공
BALL_SIZE = 10
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_dx = 7
ball_dy = -7

# 블럭
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 30
BLOCK_ROWS = 5
BLOCK_COLS = 8
blocks = []
block_colors = []

# 아이템
items = []
ITEM_SIZE = 15
ITEM_SPEED = 3
has_gun = False

# 총알
bullets = []
BULLET_SIZE = 5
BULLET_SPEED = 10

# 블럭 초기화
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(
            col * (BLOCK_WIDTH + 2) + 50,
            row * (BLOCK_HEIGHT + 2) + 50,
            BLOCK_WIDTH,
            BLOCK_HEIGHT
        )
        blocks.append(block)
        block_colors.append(random.choice(COLORS))

class Item:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ITEM_SIZE, ITEM_SIZE)
        self.speed = ITEM_SPEED

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)

def draw_game():
    screen.fill(BLACK)
    
    # 블럭 그리기
    for block, color in zip(blocks, block_colors):
        pygame.draw.rect(screen, color, block)
    
    # 아이템 그리기
    for item in items:
        pygame.draw.rect(screen, YELLOW, item.rect)
    
    # 총알 그리기
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet.rect)
    
    # 패들 그리기
    pygame.draw.rect(screen, GREEN, paddle)
    
    # 공 그리기
    pygame.draw.circle(screen, RED, ball.center, BALL_SIZE//2)
    
    # 게임 상태 메시지
    if game_over:
        text = font.render('게임 오버!', True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
    if game_won:
        text = font.render('승리!', True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
    
    # 아이템 상태 표시
    if has_gun:
        text = font.render('총알 발사 가능!', True, YELLOW)
        screen.blit(text, (10, 10))
    
    pygame.display.flip()

# 게임 상태
game_over = False
game_won = False
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and has_gun:
                # 스페이스바로 총알 발사
                bullets.append(Bullet(paddle.centerx, paddle.top))
            
    if not game_over and not game_won:
        # 키보드 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += PADDLE_SPEED
            
        # 공 이동
        ball.x += ball_dx
        ball.y += ball_dy
        
        # 벽 충돌 처리
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_dx = -ball_dx
        if ball.top <= 0:
            ball_dy = -ball_dy
            
        # 패들 충돌 처리
        if ball.colliderect(paddle):
            ball_dy = -ball_dy
            
        # 아이템 이동 및 충돌 처리
        for item in items[:]:
            item.rect.y += item.speed
            if item.rect.colliderect(paddle):
                has_gun = True
                items.remove(item)
            elif item.rect.top >= HEIGHT:
                items.remove(item)
                
        # 총알 이동 및 충돌 처리
        for bullet in bullets[:]:
            bullet.rect.y -= BULLET_SPEED
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
            else:
                for i, block in enumerate(blocks[:]):
                    if bullet.rect.colliderect(block):
                        blocks.remove(block)
                        block_colors.pop(i)
                        if random.random() < 0.3:  # 30% 확률로 아이템 생성
                            items.append(Item(block.centerx, block.centery))
                        bullets.remove(bullet)
                        break
            
        # 블럭 충돌 처리
        for i, block in enumerate(blocks[:]):
            if ball.colliderect(block):
                blocks.remove(block)
                block_colors.pop(i)
                ball_dy = -ball_dy
                if random.random() < 0.3:  # 30% 확률로 아이템 생성
                    items.append(Item(block.centerx, block.centery))
                break
                
        # 게임 오버 체크
        if ball.bottom >= HEIGHT:
            game_over = True
            
        # 승리 체크
        if len(blocks) == 0:
            game_won = True
    
    # 화면 갱신
    draw_game()
    clock.tick(60)

pygame.quit()
sys.exit()

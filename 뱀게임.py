import pygame
import random
import sys

# 초기화
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 게임 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
SNAKE_SPEED = 8  # 속도를 15에서 8로 줄임
FOOD_COUNT = 3   # 동시에 표시될 사과의 개수

# 화면 설정
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('뱀 게임')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        
    def get_head_position(self):
        return self.positions[0]
    
    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + (x*BLOCK_SIZE), cur[1] + (y*BLOCK_SIZE))
        
        # 벽 충돌 검사 추가
        if (new[0] < 0 or new[0] >= WINDOW_WIDTH or 
            new[1] < 0 or new[1] >= WINDOW_HEIGHT):
            return False
        
        if new in self.positions[3:]:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return True
    
    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, 
                           (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
        
    def randomize_position(self):
        self.position = (random.randint(0, (WINDOW_WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE,
                        random.randint(0, (WINDOW_HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE)
    
    def render(self, surface):
        pygame.draw.rect(surface, self.color,
                        (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# 방향 정의
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    snake = Snake()
    # 여러 개의 음식 생성
    foods = [Food() for _ in range(FOOD_COUNT)]
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        # 뱀 이동
        if not snake.update():
            break

        # 음식 먹기 체크
        for food in foods:
            if snake.get_head_position() == food.position:
                snake.length += 1
                score += 1
                food.randomize_position()

        # 화면 그리기
        screen.fill(BLACK)
        snake.render(screen)
        for food in foods:
            food.render(screen)
        
        # 점수 표시
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

    # 게임 오버 화면
    font = pygame.font.Font(None, 72)
    game_over = font.render('Game Over!', True, WHITE)
    screen.blit(game_over, (WINDOW_WIDTH//2 - 140, WINDOW_HEIGHT//2 - 30))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
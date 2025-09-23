import pygame
import random

# 게임 설정
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, BLUE, ORANGE, GREEN, RED]

class Tetromino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation % len(self.shape)]

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.board = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.gameover = False
        self.score = 0
        self.new_tetromino()

    def new_tetromino(self):
        idx = random.randint(0, len(SHAPES) - 1)
        shape = SHAPES[idx]
        color = SHAPE_COLORS[idx]
        self.tetromino = Tetromino(COLUMNS // 2 - len(shape[0]) // 2, 0, shape, color)

    def valid(self, shape, offset_x, offset_y):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    nx = x + offset_x
                    ny = y + offset_y
                    if nx < 0 or nx >= COLUMNS or ny < 0 or ny >= ROWS:
                        return False
                    if self.board[ny][nx] != BLACK:
                        return False
        return True

    def freeze(self):
        for y, row in enumerate(self.tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.tetromino.y + y][self.tetromino.x + x] = self.tetromino.color
        self.clear_lines()
        self.new_tetromino()
        if not self.valid(self.tetromino.shape, self.tetromino.x, self.tetromino.y):
            self.gameover = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == BLACK for cell in row)]
        lines_cleared = ROWS - len(new_board)
        for _ in range(lines_cleared):
            new_board.insert(0, [BLACK for _ in range(COLUMNS)])
        self.board = new_board
        self.score += lines_cleared

    def move(self, dx, dy):
        if self.valid(self.tetromino.shape, self.tetromino.x + dx, self.tetromino.y + dy):
            self.tetromino.x += dx
            self.tetromino.y += dy
            return True
        return False

    def rotate(self):
        shape = [list(row) for row in zip(*self.tetromino.shape[::-1])]
        if self.valid(shape, self.tetromino.x, self.tetromino.y):
            self.tetromino.shape = shape

    def drop(self):
        while self.move(0, 1):
            pass
        self.freeze()

def draw_board(screen, game):
    for y in range(ROWS):
        for x in range(COLUMNS):
            color = game.board[y][x]
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    # 현재 테트로미노
    for y, row in enumerate(game.tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                px = (game.tetromino.x + x) * BLOCK_SIZE
                py = (game.tetromino.y + y) * BLOCK_SIZE
                pygame.draw.rect(screen, game.tetromino.color, (px, py, BLOCK_SIZE, BLOCK_SIZE), 0)
                pygame.draw.rect(screen, WHITE, (px, py, BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    game = Tetris()
    fall_time = 0
    fall_speed = 0.5

    running = True
    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime() / 1000
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()
                elif event.key == pygame.K_SPACE:
                    game.drop()

        if fall_time > fall_speed:
            if not game.move(0, 1):
                game.freeze()
            fall_time = 0

        draw_board(screen, game)
        pygame.display.flip()

        if game.gameover:
            print('Game Over! Score:', game.score)
            pygame.time.wait(2000)
            running = False

    pygame.quit()

if __name__ == '__main__':
    main()


import pygame
from pygame.color import THECOLORS
import sys


def print_x(coord: tuple):
    pygame.draw.line(screen, (0, 0, 0), (coord[0] + 30, coord[1] + 30), (coord[0] + 70, coord[1] + 70))
    pygame.draw.line(screen, (0, 0, 0), (coord[0] + 30, coord[1] + 70), (coord[0] + 70, coord[1] + 30))


def print_o(coord: tuple):
    pygame.draw.circle(screen, (0, 0, 0), (coord[0] + 50, coord[1] + 50), 20, width=1)


def is_winner(player):
    if player == board[0] == board[1] == board[2] or \
       player == board[3] == board[4] == board[5] or \
       player == board[6] == board[7] == board[8] or \
       player == board[0] == board[3] == board[6] or \
       player == board[1] == board[4] == board[7] or \
       player == board[2] == board[5] == board[8] or \
       player == board[0] == board[4] == board[8] or \
       player == board[2] == board[4] == board[6]:
        return True
    else:
        return False


def winner(player=None):
    if player:
        if player == 1:
            win = 'X'
        else:
            win = 'O'
        text = f1.render(f'Победитель: {win}', True, (180, 0, 0))
        screen.blit(text, (100, 50))
    else:
        text = f1.render('Победила ничья', True, (180, 0, 0))
        screen.blit(text, (90, 50))


pygame.init()

clock = pygame.time.Clock()
FPS = 30
screen = pygame.display.set_mode((400, 450))
screen.fill(THECOLORS['white'])
pygame.display.set_caption('Крестики - Нолики')
f1 = pygame.font.Font(None, 36)

rectangle = pygame.Rect(50, 100, 300, 300)
pygame.draw.rect(screen, (180, 180, 180), rectangle, width=0)
pygame.draw.line(screen, (0, 0, 0), (150, 100), (150, 400))
pygame.draw.line(screen, (0, 0, 0), (250, 100), (250, 400))
pygame.draw.line(screen, (0, 0, 0), (50, 200), (350, 200))
pygame.draw.line(screen, (0, 0, 0), (50, 300), (350, 300))

cells = (
    ((50, 150), (100, 200)),
    ((150, 250), (100, 200)),
    ((250, 350), (100, 200)),
    ((50, 150), (200, 300)),
    ((150, 250), (200, 300)),
    ((250, 350), (200, 300)),
    ((50, 150), (300, 400)),
    ((150, 250), (300, 400)),
    ((250, 350), (300, 400)),
)

board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]

count = 0

flag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not flag:
            pos = event.pos
            for i, cell in enumerate(cells):
                if cell[0][0] <= pos[0] <= cell[0][1] and cell[1][0] <= pos[1] <= cell[1][1] and board[i] == 0:
                    if count % 2 == 0:
                        board[i] = (count % 2) + 1
                        print_x((cell[0][0], cell[1][0]))
                    else:
                        board[i] = (count % 2) + 1
                        print_o((cell[0][0], cell[1][0]))
                    if is_winner((count % 2) + 1):
                        winner((count % 2) + 1)
                        flag = True
                    elif 0 not in board:
                        winner()
                    count += 1
                    break
    pygame.display.flip()
    clock.tick(FPS)

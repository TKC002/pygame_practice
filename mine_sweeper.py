from lib.shape.shape import *
from lib.shape.define import *
import pygame
import time
import random
# Square for minesweeper
colors = [None, CYAN, GREEN, RED, NAVY, BROWN, (102,205,170), RED, RED]
# [hight, width, bomb_num, square_size]
setting = {
    "easy": [9, 9, 10, 50],
    "normal": [16, 16, 40, 20],
    "hard": [16, 30, 99, 20],
    # "super": [50, 50, 500, 15],
    # "alien": [100, 100, 2000, 10]
}
class Square:
    def __init__(self, size, coordinate, has_bomb):
        # coordinate : upper left coordinate
        # self.n : number of neighbour square that has bomb
        self.has_bomb = has_bomb
        vertices = [
            coordinate,
            [coordinate[0]+size, coordinate[1]],
            [coordinate[0]+size, coordinate[1]+size],
            [coordinate[0], coordinate[1]+size],
        ]
        self.square = Polygon(BLUE, vertices, BLACK)
        self.opened = False
        self.size = size
        self.n = 0
        self.flag = False
    
    def open(self):
        self.opened = True
        self.square.color=WHITE

    def draw(self, screen):
        if self.opened:
            self.square.draw(screen, draw_edge=True)
            if self.has_bomb:
                pygame.draw.circle(screen, RED, self.square.cog.elems, self.size*0.4)
            elif self.n == 0:
                self.square.draw(screen, draw_edge=True)
            else:
                font = pygame.font.Font(None, self.size)
                text_surface = font.render(str(self.n), True, colors[self.n])
                text_rect = text_surface.get_rect(center=self.square.cog.elems)
                screen.blit(text_surface, text_rect)
        else:
            self.square.draw(screen, draw_edge=True)
            if self.flag:
                pygame.draw.circle(screen, YELLOW, self.square.cog.elems, self.size*0.4)
class Counter:
    def __init__(self, screen_width, screen_height):
        self.height = 100
        vertices = [(0,screen_height), 
                    (screen_width, screen_height),
                    (screen_width, screen_height+self.height),
                    (0, screen_height+self.height)]
        self.rect = Polygon(GREY, vertices, None)
    
    def draw(self, screen):
        self.rect.draw(screen)



d = input(f'input difficulty{list(setting.keys())}, or custom > ')
if d=='custom':
    sh = int(input('input height > '))
    sw = int(input('input width > '))
    bomb_num = int(input('input number of bomb > '))
    square_size = 20
else:
    print(setting[d])
    sh = setting[d][0]
    sw = setting[d][1]
    bomb_num = setting[d][2]
    square_size = setting[d][3]
screen_height = square_size*sh
screen_width = square_size*sw

opened_num = [0]

def chain_open(squares, i, j):
    if squares[i][j].n != 0:
        squares[i][j].open()
        # print('i,j = ', i,j)
        opened_num[0] +=1
        # print(opened_num[0])
    else:
        squares[i][j].open()
        opened_num[0] +=1
        i_min = max(0, i-1)
        i_max = min(sh, i+2)
        j_min = max(0, j-1)
        j_max = min(sw, j+2)
        for k in range(i_min, i_max):
            for l in range(j_min, j_max):
                if squares[k][l].opened == False:
                    chain_open(squares, k, l)

pygame.init()
counter = Counter(screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height+counter.height))
squares = [[0 for j in range(sw)] for i in range(sh)]
for i in range(sh):
    for j in range(sw):
        squares[i][j] = Square(square_size, [square_size*j, square_size*i], False)

def place_bomb(i,j):
    indices = list(range(sw*sh))
    i_min = max(-1, i-2)
    i_max = min(sh-1, i+1)
    j_min = max(-1, j-2)
    j_max = min(sw-1, j+1)
    for k in range(i_max, i_min, -1):
        for l in range(j_max, j_min, -1):
            ind = k*sw+l
            indices.pop(ind)
    # print(indices)
    has_bombs = random.sample(indices, bomb_num)
    bomb_list = []

    for has_bomb in has_bombs:
        i = has_bomb//sw
        j = has_bomb%sw
        squares[i][j].has_bomb = True
        bomb_list.append([i,j])
    # set square.n
    for b in bomb_list:
        i_min = max(0, b[0]-1)
        i_max = min(sh, b[0]+2)
        j_min = max(0, b[1]-1)
        j_max = min(sw, b[1]+2)
        for i in range(i_min, i_max):
            for j in range(j_min, j_max):
                squares[i][j].n += 1
    return bomb_list

def draw():
    for i in range(sh):
        for j in range(sw):
            squares[i][j].draw(screen)
    counter.draw(screen)

running = True
clicked = False
bomb_remain = bomb_num

draw()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            j = mouse_x // square_size
            i = mouse_y // square_size
            if mouse_x <= screen_height and mouse_y <= screen_width:
                if not clicked: # 最初のクリック
                    bomb_list = place_bomb(i,j)
                    clicked = True
                if event.button == 1:  # 左クリック
                    if squares[i][j].flag==False and squares[i][j].opened==False:
                        if squares[i][j].has_bomb:
                            for b in bomb_list:
                                squares[b[0]][b[1]].open()
                            print('You Lose!')
                        else:
                            # squares[i][j].open()
                            chain_open(squares, i, j)
                            # print(opened_num[0])
                            if opened_num[0] == sh*sw-bomb_num:
                                print('You Win!')
                if event.button == 3:  # 右クリック
                    if squares[i][j].flag:
                        squares[i][j].flag = False
                        bomb_remain+=1
                    else:
                        squares[i][j].flag = True
                        bomb_remain-=1
                    print(bomb_remain)
                screen.fill((0, 0, 0))
                draw()
            pygame.display.flip()

        
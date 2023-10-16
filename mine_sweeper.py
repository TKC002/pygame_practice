from lib.shape.shape import *
from lib.shape.define import *
import pygame
import time
import random
# Square for minesweeper
colors = [None, CYAN, GREEN, RED, NAVY, BROWN, (102,205,170), RED, RED]
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

screen_width = 500
screen_height = 500
square_size = 20
sw = screen_width//square_size
sh = screen_height//square_size
bomb_num = 50

def chain_open(squares, i, j):
    if squares[i][j].n != 0:
        squares[i][j].open()
    else:
        squares[i][j].open()
        i_min = max(0, i-1)
        i_max = min(sh, i+2)
        j_min = max(0, j-1)
        j_max = min(sw, j+2)
        for k in range(i_min, i_max):
            for l in range(j_min, j_max):
                if squares[k][l].opened == False:
                    chain_open(squares, k, l)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

has_bombs = random.sample(range(sw*sh), bomb_num)
squares = [[0 for j in range(sw)] for i in range(sh)]
bomb_list = []

for i in range(sh):
    for j in range(sw):
        squares[i][j] = Square(square_size, [square_size*j, square_size*i], False)

for has_bomb in has_bombs:
    i = has_bomb//sh
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                mouse_x, mouse_y = event.pos
                j = mouse_x // square_size
                i = mouse_y // square_size
                if squares[i][j].has_bomb:
                    for b in bomb_list:
                        squares[b[0]][b[1]].open()
                else:
                    # squares[i][j].open()
                    chain_open(squares, i, j)
    screen.fill((0, 0, 0))
    for i in range(sh):
        for j in range(sw):
            squares[i][j].draw(screen)
    pygame.display.flip()

        
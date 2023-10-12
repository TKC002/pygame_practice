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
        self.open = False
        self.n = 0
    
    def open(self):
        self.square.color=WHITE

    def draw(self, screen):
        if self.open:
            self.square.draw(screen, draw_edge=True)
        else:
            self.square.draw(screen, draw_edge=True)

screen_width = 500
screen_height = 500
square_size = 20
sw = screen_width//square_size
sh = screen_height//square_size
bomb_num = 20

screen = pygame.display.set_mode((screen_width, screen_height))

has_bombs = random.sample(range(sw*sh), bomb_num)
squares = [[0 for j in range(sw)] for i in range(sh)]

for i in range(sh):
    for j in range(sw):
        squares[i][j] = Square(square_size, [square_size*i, square_size*j], False)

for has_bomb in has_bombs:
    i = has_bomb//sh
    j = has_bomb%sw
    squares[i][j].has_bomb = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in range(sh):
        for j in range(sw):
            squares[i][j].draw(screen)
    pygame.display.flip()

        
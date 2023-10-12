from lib.shape.shape import *
from lib.shape.define import *
import pygame
import time

WIDTH, HEIGHT = 300,600


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

vertices=[
    (0,0),
    (0,100),
    (100,100),
    (100,0)
]

p = Polygon(color=YELLOW, edge_color=BLUE, vertices=vertices)
c = Circle(color=YELLOW, edge_color=BLUE, center=[200,200], radius=50)

print(p.area())
print(p.contain([50, 50]))
print(p.contain([150, 50]))
print(p.contain([0,50]))
print(p.edges[0].contain([0,0]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    p.draw(screen, draw_edge=True)
    c.draw(screen, draw_edge=True)
    pygame.display.flip()
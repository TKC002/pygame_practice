from lib.shape.polygon import *
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

p = Polygon(screen=screen, color=YELLOW, vertices=vertices)

seg1 = Segment(screen, WHITE, [[0,100],[100,100]])
seg2 = Segment(screen, GREEN, [[150,50],[150,65535]])

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

    p.draw()
    seg1.draw()
    seg2.draw()
    pygame.display.flip()
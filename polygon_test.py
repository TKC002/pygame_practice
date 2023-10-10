from lib.shape.polygon import *
from lib.shape.define import *
import pygame
import time

pygame.init()
WIDTH, HEIGHT = 300,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")



vertices=[
    (0,0),
    (0,100),
    (100,100),
    (100,0)
]

p = Polygon(screen=screen, color=YELLOW, vertices=vertices)

print(p.area())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    p.draw()
    pygame.display.flip()
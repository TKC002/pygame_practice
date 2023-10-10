from .shape import Shape
import pygame

class Polygon(Shape):
    def __init__(self, screen, color, vertices):
        # vertices: list of array-like
        # vertice: (x,y)
        self.screen = screen
        self.color = color
        self.vertices = [list(vertice) for vertice in vertices]
        self.n = len(vertices)
    
    def area(self):
        tmp = 0
        for i in range(self.n):
            current = self.vertices[i]
            next = self.vertices[(i+1)%self.n]
            tmp += (current[0]-next[0])*(current[1]+next[1])
        tmp = abs(tmp)
        res = tmp / 2

        return res
    
    def draw(self):
        pygame.draw.polygon(surface=self.screen, color=self.color, points=self.vertices)
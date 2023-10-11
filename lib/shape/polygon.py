from .shape import Shape
from .segment import Segment
from ..util.util import *
import pygame

class Polygon(Shape):
    def __init__(self, screen, color, vertices):
        # vertices: list of array-like
        # vertice: (x,y)
        self.screen = screen
        self.color = color
        self.vertices = [list(vertice) for vertice in vertices]
        self.n = len(vertices)
        self.edges=[]

        for i in range(self.n):
            current = self.vertices[i]
            next = self.vertices[(i+1)%self.n]
            edge = Segment(self.screen, self.color, [current, next])
            self.edges.append(edge)
    
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
    
    def contain(self, point):
        seg = Segment(None, None, [point, (point[0],65535)])
        cross_num=0
        for i in range(self.n):
            if self.edges[i].contain(point):
                return True
            if self.edges[i].cross(seg):
                print(i)
                cross_num+=1
        if cross_num%2==1:
            return True
        else:
            return False

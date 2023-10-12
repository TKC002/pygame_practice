from abc import ABC, abstractmethod
from ..util.util import *
import pygame
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def contain(self, point):
        pass

    # @abstractmethod
    # def pararell_move(self, direction):
    #     pass

class Vector:
    def __init__(self, elems):
        if isinstance(elems, Vector):
            self.elems = elems.elems
        else:
            self.elems = elems
        self.dim = len(elems)
        tmp = 0
        for e in self.elems:
            tmp += e**2
        res = math.sqrt(tmp)
        self.length = res
    
    def __add__(self, other):
        elems = [e0+e1 for e0,e1 in zip(self.elems, other.elems)]
        return Vector(elems)
    
    def __sub__(self, other):
        elems = [e0-e1 for e0,e1 in zip(self.elems, other.elems)]
        return Vector(elems)

    def __len__(self):
        return self.dim
    
    def __getitem__(self, position):
        return self.elems[position]

    def inner_product(self, other):
        if self.dim != other.dim:
            print('vector1 and vector2 must be same length.')
            return False
        res = 0
        for e1, e2 in zip(self.elems, other.elems):
            res += e1*e2
        return res

class Segment(Shape):
    def __init__(self, color, vertice0, vertice1):
        # vertices : list of list
        self.color = color
        # A
        self.s = Vector(vertice0)
        # B
        self.e = Vector(vertice1)
        self.vec = self.e-self.s
        self.length = self.vec.length
    
    def area(self):
        return 0
    
    def draw(self, screen):
        pygame.draw.line(surface=screen, color=self.color, start_pos=self.s.elems, end_pos=self.e.elems)

    def cross(self, seg):
        # determin whether two segments cross
        tc0 = (self.e[0]-self.s[0])*(seg.s[1]-self.s[1])-(seg.s[0]-self.s[0])*(self.e[1]-self.s[1])
        tc1 = (self.e[0]-self.s[0])*(seg.e[1]-self.s[1])-(seg.e[0]-self.s[0])*(self.e[1]-self.s[1])
        tc2 = (seg.e[0]-seg.s[0])*(self.s[1]-seg.s[1])-(self.s[0]-seg.s[0])*(seg.e[1]-seg.s[1])
        tc3 = (seg.e[0]-seg.s[0])*(self.e[1]-seg.s[1])-(self.e[0]-seg.s[0])*(seg.e[1]-seg.s[1])

        if tc0*tc1 <= 0 and tc2*tc3<=0:
            return True
        else:
            return False

    def contain(self, point):
        if not isinstance(point, Vector):
            point = Vector(point)
        point_vec = point-self.s

        if self.vec.inner_product(point_vec) == self.length*point_vec.length:
            if self.length >= point_vec.length:
                return True
        return False
    
    def pararell_move(self, direction):
        self.s = self.s + direction
        self.e = self.e+direction

class Polygon(Shape):
    def __init__(self, color, vertices, edge_color=None):
        # vertices: list of list
        # vertice: (x,y)
        self.color = color
        if edge_color is None:
            self.edge_color = color
        else:
            self.edge_color = edge_color
        self.vertices = [Vector(vertice) for vertice in vertices]
        self.n = len(vertices)
        self.edges=[]

        for i in range(self.n):
            current = vertices[i]
            next = vertices[(i+1)%self.n]
            edge = Segment(self.edge_color, current, next)
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
    
    def draw(self, screen, draw_edge=False):
        vertices = [vec.elems for vec in self.vertices]
        pygame.draw.polygon(surface=screen, color=self.color, points=vertices)
        if draw_edge:
            for edge in self.edges:
                edge.draw(screen)
    
    def contain(self, point):
        seg = Segment(None, point, (point[0],65535))
        cross_num=0
        for i in range(self.n):
            if self.edges[i].contain(point):
                return True
            if self.edges[i].cross(seg):
                cross_num+=1
        if cross_num%2==1:
            return True
        else:
            return False

class Circle(Shape):
    def __init__(self, color, center, radius, edge_color=None):
        self.color = color
        self.center = center
        self.radius = radius
        if edge_color is None:
            self.edge_color = color
        else:
            self.edge_color = edge_color
    
    def area(self):
        return self.radius**2*math.pi
    
    def contain(self, point):
        length = math.sqrt((point[0]-self.center[0])**2+(point[1]-self.center[1])**2)
        if length <= self.radius:
            return True
        else:
            return False
    
    def draw(self, screen, draw_edge=False):
        pygame.draw.circle(screen, self.color, self.center, self.radius)
        if draw_edge:
            pygame.draw.circle(screen, self.edge_color, self.center, self.radius+1, width=1)


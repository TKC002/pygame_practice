from .shape import Shape
from ..util.util import *
import pygame
import math

class Segment(Shape):
    def __init__(self, screen, color, vertices):
        self.screen = screen
        self.color = color
        self.s = vertices[0] # A
        self.e = vertices[1] # B

        self.length = math.sqrt((self.e[0]-self.s[0])**2+(self.e[1]-self.s[1])**2)
    
    def area(self):
        return 0
    
    def draw(self):
        pygame.draw.line(surface=self.screen, color=self.color, start_pos=self.s, end_pos=self.e)

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
        vec = [self.e[0]-self.s[0], self.e[1]-self.s[1]] # B-A
        point_vec = [point[0]-self.s[0], point[1]-self.s[1]] # P-A

        point_vec_length = math.sqrt(point_vec[0]**2+point_vec[1]**2)

        if inner_product(vec, point_vec) == self.length*point_vec_length:
            if self.length >= point_vec_length:
                return True
        return False





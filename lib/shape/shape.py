from abc import ABC, abstractmethod

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
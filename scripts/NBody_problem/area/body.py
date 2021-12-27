from _typeshed import Self
import NBody_problem.utils.settings as settings

class Body:
    def __init__(self, fileName):
        self.mass = 0.0
        self.position = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0
    
    def compute(self, body) :
        self.position += self.velocity + self.acceleration * 0.5
        self.velocity += self.acceleration
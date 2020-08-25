from .dot import Dot
from .vector import Vector

class Board:
    def __init__( self, dimensions: Vector ):
        self.dimensions = dimensions
        self.dots = []
        for y in range(self.dimensions.y):
            self.dots.append( [Dot( Vector(x, y) ) for x in range(self.dimensions.x)] )
    
    def __repr__( self ):
        return str(self.dots)
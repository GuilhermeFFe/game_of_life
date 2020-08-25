from enum import Enum
from .vector import Vector

class Dot:
    class State(Enum):
        ALIVE = 0
        DEAD = 1
        
    def __init__( self, pos: Vector ):
        self.state = self.State.DEAD
        self.pos = pos
    
    def __repr__( self ):
        return f'Dot=({self.state}, {self.pos})'

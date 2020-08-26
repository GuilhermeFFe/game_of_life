from enum import Enum
from .vector import Vector

import pygame

import random #TODO: remove!

class Dot:
    class State(Enum):
        ALIVE = 255
        DEAD = 0
        
    def __init__( self, pos: Vector ):
        self.state = random.choice( [self.State.ALIVE, self.State.DEAD] )
        self.pos = pos
    
    def draw(self, canvas, resolution: int) -> None:
        colorint = self.state.value
        color = tuple(colorint for _ in range(3))

        truepos = self.pos*resolution

        rect = pygame.Rect(truepos.x+1, truepos.y+1, resolution-2, resolution-2)
        pygame.draw.rect(canvas, color, rect)
    
    def __repr__( self ) -> str:
        return f'Dot=({self.state}, {self.pos})'

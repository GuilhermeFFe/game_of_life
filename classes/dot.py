from enum import Enum
from .vector import Vector

import pygame

class Dot:
    class State(Enum):
        ALIVE = 0
        DEAD = 255
        
    def __init__( self, pos: Vector ):
        self.state = self.State.DEAD
        self.next_state = None
        self.pos = pos
    
    def draw(self, canvas, resolution: int) -> None:
        colorint = self.state.value
        color = tuple(colorint for _ in range(3))

        truepos = self.pos*resolution

        rect = pygame.Rect(truepos.x+1, truepos.y+1, resolution-2, resolution-2)
        pygame.draw.rect(canvas, color, rect)
    
    def kill(self) -> None:
        self.next_state = self.State.DEAD
    
    def revive(self) -> None:
        self.next_state = self.State.ALIVE
    
    def update(self) -> None:
        if self.next_state:
            self.state = self.next_state;
            self.next_state = None
    
    def change(self) -> None:
        self.state = self.State.ALIVE if self.state == self.State.DEAD else self.State.DEAD
    
    def is_alive(self):
        return self.state == self.State.ALIVE
    
    def __repr__( self ) -> str:
        return f'Dot=({self.state}, {self.pos})'

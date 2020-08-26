from .dot import Dot
from .vector import Vector

class Board:
    def __init__(self, dimensions: Vector):
        self.dimensions = dimensions
        self.dots = []
        self.running = False
        for y in range(self.dimensions.y):
            self.dots.append( [Dot( Vector(x, y) ) for x in range(self.dimensions.x)] )
    
    def __repr__(self) -> str:
        return str(self.dots)
    
    def __getitem__(self, which: tuple) -> Dot:
        x, y = which
        return self.dots[(y+self.dimensions.y)%self.dimensions.y][(x+self.dimensions.x)%self.dimensions.x]

    def update(self) -> bool:
        if not self.running:
            return True

        for row in self.dots:
            for dot in row:
                neighbors = self.check_neighbors(dot)
                if dot.is_alive():
                    if neighbors < 2:
                        dot.kill()
                    elif neighbors > 3:
                        dot.kill()
                else:
                    if neighbors == 3:
                        dot.revive()
        
        for row in self.dots:
            for dot in row:
                dot.update()

        return True
    
    def force_update(self) -> bool:
        ret = None
        if self.running:
            ret = self.update()
        else:
            self.running = True
            ret = self.update()
            self.running = False
        return ret
    
    def killall(self) -> None:
        for row in self.dots:
            for dot in row:
                dot.kill()
                dot.update()
    
    def update_dot(self, pos: tuple) -> None:
        if not self.running:
            self[pos].change()
    
    def draw(self, canvas, resolution: int) -> None:
        for row in self.dots:
            for dot in row:
                dot.draw(canvas, resolution)
    
    def change(self) -> None:
        self.running = not self.running
    
    def check_neighbors(self, dot: Dot) -> int:
        ammount = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                ammount += 1 if self[ dot.pos.x+x, dot.pos.y+y ].is_alive() else 0
        ammount -= 1 if dot.is_alive() else 0
        return ammount
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def as_tuple(self) -> tuple:
        return self.x, self.y
    
    def __repr__(self) -> str:
        return f'Position=({self.x}, {self.y})'
    
    def __truediv__(self, num: int):
        return Vector(int(self.x/num), int(self.y/num))
    
    def __mul__(self, num: int):
        return Vector(int(self.x*num), int(self.y*num))
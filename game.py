from classes import Board
from classes import Vector

import pygame
from pygame.locals import *
from time import sleep

class Game:
    def __init__( self ):
        self.framerate = 60
        self.running = True
        self.resolution = 10
        self.screenSize = Vector( 600, 400 )
        self.canvas = None

        self.boardSize = self.screenSize/self.resolution
    
    def gameLoop(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            if not self.tick():
                self.running = False
                
            self.render()
            pygame.display.update()
            sleep(1 / self.framerate)
    
    def on_event(self, event) -> None:
        if event.type == QUIT:
            self.running = False
    
    def tick(self) -> bool:
        return self.board.update()
    
    def render(self) -> None:
        self.canvas.fill((0, 0, 0))
        self.board.draw(self.canvas, self.resolution)

    def run(self) -> None:
        pygame.init()
        self.canvas = pygame.display.set_mode(self.screenSize.as_tuple( ))
        pygame.display.set_caption('Conway Game of Life')

        self.board = Board(self.boardSize)
        self.gameLoop()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
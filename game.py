from classes import Board
from classes import Vector

import pygame
from pygame.locals import *
from math import floor

class Game:
    def __init__( self ):
        self.tickrate = 60
        self.ticks_per_update = 1
        self.ticks_passed = 0
        self.running = True
        self.resolution = 10
        self.screenSize = Vector( 800, 600 )
        self.canvas = None

        self.boardSize = self.screenSize/self.resolution
    
    def gameLoop(self):
        while self.running:
            self.ticks_passed += 1
            for event in pygame.event.get():
                self.on_event(event)

            if self.ticks_passed >= self.ticks_per_update:
                self.ticks_passed = 0
                if not self.tick():
                    self.running = False

            self.render()
            pygame.display.update()
            self.clock.tick(self.tickrate)
    
    def on_event(self, event) -> None:
        if event.type == QUIT:
            self.running = False
        if event.type == KEYDOWN:
            self.on_key(event.key)
        if event.type == MOUSEBUTTONDOWN:
            self.on_mouse(event.pos)
    
    def on_key(self, key) -> None:
        if key == K_SPACE:
            self.board.change()
        if key == K_ESCAPE:
            self.running = False
        if key == K_t:
            self.board.force_update()
        if key == K_c:
            self.board.killall()
    
    def on_mouse(self, pos: tuple) -> None:
        x, y = pos
        x = floor(x/self.resolution)
        y = floor(y/self.resolution)
        self.board.update_dot((x, y))

    def tick(self) -> bool:
        return self.board.update()
    
    def render(self) -> None:
        self.canvas.fill((255, 255, 255))
        self.board.draw(self.canvas, self.resolution)

    def run(self) -> None:
        pygame.init()
        self.canvas = pygame.display.set_mode(self.screenSize.as_tuple( ))
        pygame.display.set_caption('Conway Game of Life')

        self.clock = pygame.time.Clock()

        self.board = Board(self.boardSize)
        self.gameLoop()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
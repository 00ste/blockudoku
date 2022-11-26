import pygame
from grid import grid

class game_view:
    def __init__(self) -> None:
        self.grid = grid((675, 675), (20, 20))
    
    def run(self, display: pygame.Surface):
        self.grid.values[0][4] = True
        self.grid.values[2][2] = True
        self.grid.values[2][3] = True
        self.grid.values[1][7] = True
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit(0)

            display.fill('#dddddd')
            self.grid.render(display)
            pygame.display.update()
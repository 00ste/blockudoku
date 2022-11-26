import pygame

class grid:
    def __init__(self, dimensions, position) -> None:
        self.values = []
        for i in range(9):
            self.values.append([])
            for j in range(9):
                self.values[i].append(False)
        print(f'grid is: {self.values}')
        self.dimensions = dimensions
        self.position = position

    def render(self, display: pygame.Surface):
        surf = pygame.Surface(self.dimensions)
        for x_index, col in enumerate(self.values):
            for y_index, item in enumerate(col):
                color = '#ffffff'
                if item:
                    color = '#0362fc'
                print(f'cell {x_index}, {y_index} is {item}, color is {color}')
                pygame.draw.rect(surf, color, pygame.Rect((75*x_index, 75*y_index), self.dimensions))
                #pygame.draw.rect(surf, '#000000', pygame.Rect((75*x_index, 75*y_index), self.dimensions), 2)
        display.blit(surf, self.position)
                    
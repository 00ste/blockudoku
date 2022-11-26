import pygame
from game_view import game_view

dimensions = (800, 800)

pygame.init()
display = pygame.display.set_mode(dimensions)

output = game_view().run(display)
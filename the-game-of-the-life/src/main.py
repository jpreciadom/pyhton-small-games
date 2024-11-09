import pygame
from game_objects import Cell
from gui import Window

window = Window()

while window.is_running:
  window.draw_scene()

pygame.quit()

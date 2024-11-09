import pygame
from game_objects import Cell

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

cell = Cell(True)
print(cell)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.fill("purple")

  pygame.display.flip()

  clock.tick(60)

pygame.quit()

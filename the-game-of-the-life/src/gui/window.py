import pygame
from game_objects import GameBoard

class Window:
  screen: pygame.Surface
  clock: pygame.time.Clock
  is_running: bool
  dimensions: tuple[int, int]

  # Game board
  game_board: GameBoard

  def __init__(self):
    pygame.init()
    self.dimensions = (480, 480)
    self.screen = pygame.display.set_mode(self.dimensions)
    self.clock = pygame.time.Clock()
    self.is_running = True

    self.game_board = GameBoard()

  def draw_scene(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.is_running = False
    
    self.screen.fill((0, 0, 0, 0))
    
    pygame.draw.rect(
      self.screen,
      (255, 255, 255, 0),
      rect=(39, 39, 402, 402),
    )

    # TODO: Here we iterate over the cells to draw them in the board.
    # Use this iteration to calculate the next cell state.
    # TODO: Organize this code
    for cell in self.game_board.grid:
      color = (255, 255, 255, 0) if cell.is_alive else (0, 0, 0, 0)
      pygame.draw.rect(
        self.screen,
        color,
        (
          cell.position[0] * 4 + 40,
          cell.position[1] * 4 + 40,
          4,
          4,
        ),
      )

    pygame.display.flip()
    print("Hello world")
    self.clock.tick(2)

  def halt(self):
    pygame.quit()

import numpy as np
import random
from .types import Dimensions
from .cell import Cell

class GameBoard:
  dimensions: Dimensions
  grid: np.ndarray

  def __init__(self):
    self.dimensions = (100, 100)
    self.grid = np.zeros(self.dimensions[0] * self.dimensions[1], Cell)
    # TODO: Here we create the cell randomly (by now). Load the cell
    # neighbors in this section.
    for x in range(0, self.dimensions[0]):
      for y in range(0, self.dimensions[1]):
        status = random.randint(0, 99)
        self.grid[(y * self.dimensions[0] + x)] = Cell(status >= 87, (x, y))


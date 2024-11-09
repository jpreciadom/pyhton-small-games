from enum import Enum
import numpy as np
from .types import Dimensions

class Cell:
  is_alive: bool
  neighbors: np.array
  position: Dimensions

  def __init__(self, is_alive: bool, position: Dimensions):
    self.is_alive = is_alive
    self.position = position
    self.neighbors = np.zeros(8, Cell)

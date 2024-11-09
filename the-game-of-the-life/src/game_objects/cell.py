from enum import Enum
import numpy as np

class Cell:
  is_alive: bool
  neighbors: np.array

  def __init__(self, is_alive: bool):
    self.is_alive = is_alive
    self.neighbors = np.zeros(8)

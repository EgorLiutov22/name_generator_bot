#imports
import random

class BasicGenerator:
    def __init__(self, seed) -> None:
        self._seed = seed

    @property
    def seed(self):
      return self._seed

    @seed.setter
    def seed(self, new_seed):
      self.seed = new_seed

    @seed.deleter
    def seed(self):
      del self.seed
      
    def generate_name(self):
      return "EgorLiutov" + random.randint(0, 100)

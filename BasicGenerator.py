# imports
import random
from TileManager import TileManager
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from db.types import Names, Decorators


# Класс для генерации имён
class BasicGenerator:
    def __init__(self, weirdness: int, name: str) -> None:
        """BasicGenerator — это класс для генерации случайного ника, основываясь на данных значениях.

      Args:
          weirdness (int): уровень странности ника. Целое число от одного до десяти
          name (str): Имя на основе которого будет ник
      """
        self._weirdness = weirdness
        self._name = name
        self._engine = create_engine("sqlite://", echo=True)
        self._session = Session(self._engine)

    def generate_nick(self) -> str:
        """Непосредственно генерация ника.

      Returns:
          str: Сгенерированный ник.
      """
        tiles = TileManager().loadAllTiles()
        weirdness_range = set(range(self.weirdness - 1, self.weirdness + 2))
        # nick = random.choice(tiles["decorators"][random.choice(list(set(tiles["decorators"].keys()).intersection(weirdness_range)))])
        # name = tiles["names"][self.name][random.choice(list(set(tiles["names"][self.name].keys()).intersection(weirdness_range)))]
        name_query = select(Names).where(Names.name == self._name)
        name = self._session.execute(name_query)
        decorator_query = select(Decorators)
        nick_list = self._session.execute(decorator_query)
        nick_list = [r for r, in nick_list]
        nick = random.choice(nick_list)
        nick = nick.format(name)
        return nick

    @property
    def weirdness(self) -> int:
        return self._weirdness

    @weirdness.setter
    def weirdness(self, new_weirdness) -> None:
        self._weirdness = new_weirdness

    @weirdness.deleter
    def weirdness(self) -> None:
        del self._weirdness

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name


b = BasicGenerator(5, 'Максим')
print(b.generate_nick())

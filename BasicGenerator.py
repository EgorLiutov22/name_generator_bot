# imports
from TileManager import TileManager


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

    def generate_nick(self) -> str:
        """Непосредственно генерация ника.

        Returns:
            str: Сгенерированный ник.
        """
        
        name = TileManager.load_name_tyle(self.name, self.weirdness - 1, self.weirdness + 1)
        decorator = TileManager.load_decorator_tyle(self.weirdness - 1, self.weirdness + 1)
        
        return decorator.format(name)
        

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


b = BasicGenerator(5, "Максим")
print(b.generate_nick())

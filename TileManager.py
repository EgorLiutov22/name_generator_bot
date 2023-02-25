import json
import random

class TileManager:
    """Класс для хранения частей ника (тайлов) (имён, декораторов и т.д.)"""
    
    @staticmethod
    def load_name_tyle(current_name: str, least_weird: int, most_weird: int) -> str:
        """Функция, в которой храниться словарь всех тайлов.

        Returns:
            dict[dict]: словарь тайлов, значения:
                - "names" — имена, на которых может основываться ник,
                    внутри словари с ключами по уровню странности, каждому ключу соответствует список имён;
                - "decorators" — декораторы вокруг ника,
                    внутри ключи по уровню странности, каждому ключу соответствует список декораторов;
        """
        name_tiles = TileManager.load_all_tyles()["names"][TileManager.to_number_format(current_name)]
        least_to_most = set(range(least_weird, most_weird + 1))
        available_keys = set(list(map(int, name_tiles.keys())))
        weirdness_range = least_to_most.intersection(available_keys)
        return random.choice([name_tiles[str(i)][random.randint(0, len(name_tiles[str(i)]) - 1)] for i in weirdness_range])
    
    @staticmethod
    def load_decorator_tyle(least_weird: int, most_weird: int) -> str:
        """Функция, в которой храниться словарь всех тайлов.

        Returns:
            dict[dict]: словарь тайлов, значения:
                - "names" — имена, на которых может основываться ник,
                    внутри словари с ключами по уровню странности, каждому ключу соответствует список имён;
                - "decorators" — декораторы вокруг ника,
                    внутри ключи по уровню странности, каждому ключу соответствует список декораторов;
        """
        name_tiles = TileManager.load_all_tyles()["decorators"]
        least_to_most = set(range(least_weird, most_weird + 1))
        available_keys = set(list(map(int, name_tiles.keys())))
        weirdness_range = least_to_most.intersection(available_keys)
        return random.choice([name_tiles[str(i)][random.randint(0, len(name_tiles[str(i)]) - 1)] for i in weirdness_range])
    
    @staticmethod
    def load_all_tyles() -> any:
        return json.load(open("tiles.json"))
    
    @staticmethod
    def to_number_format(word: str) -> str:
        alpabet = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я".split(" ")
        return '.'.join(list(map(str, [alpabet.index(i) for i in word.lower()])))
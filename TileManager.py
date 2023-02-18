from typing import Dict, List


class TileManager:
    """Класс для хранения частей ника (тайлов) (имён, декораторов и т.д.)"""
    def loadAllTiles(self) -> dict[
        str, dict[int, list[str]] | dict[str, dict[int, list[str]] | dict[int, list[str] | str]]]:
        """Функция, в которой храниться словарь всех тайлов.

        Returns:
            dict[dict]: словарь тайлов, значения:
                - "names" — имена, на которых может основываться ник,
                    внутри словари с ключами по уровню странности, каждому ключу соответствует список имён;
                - "decorators" — декораторы вокруг ника,
                    внутри ключи по уровню странности, каждому ключу соответствует список декораторов;
        """
        return {
            "names": {
                "Егор": {
                    1: ["Egor"], 
                    3: ["Egorka"], 
                    5: ["Egorchik"], 
                    7: ["Egorushka", "Jora"], 
                    9: ["Jorus"],
                    10: ["Jorazillus"]
                },
                "Пётр": {
                    1: ["Petya"],
                    2: ["Pyotr", "Peter", "Pierre"],
                    5: ["Petrusha", "Petrovich"],
                    6: ["Petrushka"], 
                    7: ["Petyajka"], 
                    8: ["Petrusya"], 
                    10: ["Pyotroshitel"]
                    },
                "Максим": {
                    1: ["Maxim", "Max"], 
                    3: "Masik", 
                    5: "Maxyushka",
                    7: "Maximus",
                    10: "Maxomolka"}
            },
            "decorators": {
                1: ["_{}_"], 
                3: ["xX_{}_Xx", "xX-{}-Xx", "Xx_{}_xX"], 
                4: ["-:[{}]:-"],
                8: ["-~~~xXX[{}]XXx~~~-"],
                10: ["_.-=^\"`{}`\"^=-._", "__________{}__________", "[                                      {}                                      ]"]
            },
            
        }
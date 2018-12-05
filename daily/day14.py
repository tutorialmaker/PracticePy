"""

    SpeciesBookはモンスターの記録管理をする.
    SpeciesBookの処理をヘルパークラスを用いて簡略化せよ.
    なお一例として, ヘルパークラスを用いた場合,
    99行目以降の処理は以下のように簡略化することができる.


    if __name__ == "__main__":
        book = SpeciesBook()

        mouse = book.species("Mouse")
        duck = book.species("Duck")

        mic = mouse.monster("Mic")
        min = mouse.monster("Min")
        don = duck.monster("Doc")

        mic.set(HP=300, ATK=200, DEF=100)
        min.set(HP=200, ATK=300, DEF=100)
        don.set(HP=100, ATK=100, DEF=50)
        
        book.show()

"""


class SpeciesBook:
    """モンスターを記録管理する

    Attributes
    ----------

    _status : Dict
        モンスターの種族, 名称, ステータス(体力, 攻撃力, 守備力)を記録管理する.

    """
    def __init__(self):
        self._status = {}

    def set_species(self, species):
        """新しい種族を追加する

        Parameters
        ----------

        species : str
            新しく追加する種族の名称.

        """
        self._status[species] = {}

    def set_monster(self, species, name, *, HP, ATK, DEF):
        """新しいモンスターを追加する

        Parameters
        ----------

        species : str
            既に追加した種族の名称.

        name : str
            新しく追加するモンスターの名称.

        HP : int
            体力.

        ATK : int
            攻撃力.

        DEF : int
            守備力.

        """
        if species not in self._status:
            raise Exception(f"Dont have {species} yet!")

        self._status[species][name] = {
            "HP" : HP,
            "ATK" : ATK,
            "DEF" : DEF,
        }

    def show(self):
        print("*@"*8, "STATUS", "*@"*8)
        for species in self._status:
            print("_"*40)
            print(f"PECIES : {species}")
            print("_"*40)
            for name in self._status[species]:
                status = self._status[species][name]
                print(f"    NAME : {name}")
                print(f"        HP  : {status['HP']}")
                print(f"        ATK : {status['ATK']}")
                print(f"        DEF : {status['DEF']}")
        print("*@"*20)


if __name__ == "__main__":
    book = SpeciesBook()

    book.set_species("Mouse")
    book.set_monster("Mouse", "Mic", HP=300, ATK=200, DEF=100)
    book.set_monster("Mouse", "Min", HP=200, ATK=300, DEF=100)
    book.set_species("Duck")
    book.set_monster("Duck", "Don", HP=100, ATK=100, DEF=50)

    book.show()

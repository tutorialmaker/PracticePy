"""

    SpeciesBookはモンスターの記録管理をする.
    SpeciesBookの処理をヘルパークラスを用いて簡略化せよ.
    ただし, クラスおよびメソッドに対してアノテーションを必ず付与すること.
    なお一例として, ヘルパークラスを用いた場合,
    139行目以降の処理は以下のように簡略化することができる.


    if __name__ == "__main__":
        book = SpeciesBook()

        mouse = book.species("Mouse")
        duck = book.species("Duck")

        mic = mouse.monster("Mic")
        min = mouse.monster("Min")
        don = duck.monster("Doc")

        mic.get_monster(HP=300, ATK=200, DEF=100)
        min.get_monster(HP=200, ATK=300, DEF=100)
        don.get_monster(HP=100, ATK=100, DEF=50)

        print("\n///Before Buttle.///\n")
        book.show()

        mic.update(dH=10, dA=5, dD=10)
        min.update(dH=5, dA=10, dD=10)
        don.update(dH=50, dA=5, dD=5)

        print("\n///After Buttle.///\n")
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

    def get_new_species(self, species):
        """新しい種族を追加する

        Parameters
        ----------

        species : str
            新しく追加する種族の名称.

        """
        self._status[species] = {}

    def get_monster(self, species, name, *, HP, ATK, DEF):
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

    def update(self, species, name, *, dH, dA, dD):
        """追加済みのモンスターのステータスを更新する

        Parameters
        ----------

        species : str
            既に追加した種族の名称.

        name : str
            既に追加したモンスターの名称.

        dH : int
            体力の差分.

        dA : int
            攻撃力の差分.

        dD : int
            守備力の差分.

        """
        if species not in self._status:
            raise Exception(f"Dont have {species} yet!")
        if name not in self._status[species]:
            raise Exception(f"Dont have {name} yet!")

        self._status[species][name]["HP"] += dH
        self._status[species][name]["ATK"] += dA
        self._status[species][name]["DEF"] += dD

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

    book.get_new_species("Mouse")
    book.get_monster("Mouse", "Mic", HP=300, ATK=200, DEF=100)
    book.get_monster("Mouse", "Min", HP=200, ATK=300, DEF=100)
    book.get_new_species("Duck")
    book.get_monster("Duck", "Don", HP=100, ATK=100, DEF=50)

    print("\n///Before Buttle.///\n")
    book.show()

    book.update("Mouse", "Mic", dH=10, dA=5, dD=10)
    book.update("Mouse", "Min", dH=5, dA=10, dD=10)
    book.update("Duck", "Don", dH=50, dA=5, dD=5)

    print("\n///After Buttle.///\n")
    book.show()

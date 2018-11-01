"""

    以下のPersonは個人情報を取り扱うクラスである.
    実装するべき機能をTODOに示した. アノテーションの内容を満たすようにTODOの内容を実装せよ.

"""


class Person:
    """個人情報

    Attributes
    ----------

    data : List
        個人情報のリスト

    """
    def __init__(self):
        self.data = list()

    def add(self, name, **options):
        """名前を個人情報のリストに追加する

        Parameters
        ----------

        name : str
            登録する人物の名前.
            姓と名は半角スペース' 'で区切られている必要がある.

        **options :
            titleは登録する人物の肩書きで,
            titleが与えられていない場合, titleは'Esq'を与える.
            genderが与えられてtitleが与えられていない場合,
            genderが'Man'であるならば'Mr', 'Woman'であるならば'Ms',
            それ以外ならば'Esq'を与える.
            genderは登録する人物の性別を与える.

        """
        # TODO: genderに関する機能を追加する.

        title = options.pop("title", None)
        if title is not None:
            title = title.capitalize()

        name = [n.capitalize() for n in name.split(" ")]
        if len(name) == 1:
            raise Exception("The first and last names should be separated by spaces.")
        elif len(name) > 2:
            raise Exception("Only the first and last names are accepted.")

        self.data.append({"name" : {"first" : name[0], "last": name[1]},
                        "title" : title})


if __name__ == "__main__":
    help(Person)

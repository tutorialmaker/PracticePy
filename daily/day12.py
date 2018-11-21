class Sample:
    pass


if __name__ == "__main__":

    # 以下に定義する変数brank1からbrank5に, 文脈上適切な関数を用いてオブジェクトを与えよ.

    # Pythonではすべてのクラスは, objectの直接的あるいは間接的なサブクラスである.

    brank1 = None
    brank2 = None
    print(f"{int.__name__}は{object.__name__}のサブクラスか？ -> {brank1}")
    print(f"{Sample.__name__}は{object.__name__}のサブクラスか？ -> {brank2}")

    print("_"*40)

    # Pythonではすべてのクラスはオブジェクトである.
    # クラスがオブジェクトであるならば, 型が存在する.

    brank3 = None
    print(f"{object.__name__}の型は何か？ -> {brank3}")

    print("_"*40)

    # また, brank4はobjectの型であるが, objectのサブクラスでもある.
    # ただし当然ながら, objectはbrank4のサブクラスではない.

    brank4 = None
    print(f"{brank3}は{object.__name__}のサブクラスか？ -> {brank4}")
    brank5 = None
    print(f"{object.__name__}は{brank3}のサブクラスか？ -> {brank5}")

    print("_"*40)

    # ところで, 組み込み関数intを用いることで, intのオブジェクトを動的に生成できる.

    print(f"{int.__name__}のオブジェクトを動的に生成する.")
    one = int("1")

    print("_"*40)

    # 同様に, brank4を用いることで, クラスを動的に生成できるはずである.
    # 以下に定義する関数mewを属性に持つクラスCatを動的に生成せよ.

    def mew(times=1):
        return "MEW! " * times

    # print(Cat.mew(3))

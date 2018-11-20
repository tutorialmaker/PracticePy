class Sample:
    pass


if __name__ == "__main__":

    # 以下に定義する変数brank1からbrank6に, 文脈上適切な関数を用いてオブジェクトを与えよ.

    # Pythonではすべてのクラスは, objectの直接的あるいは間接的なサブクラスである.

    brank1 = None
    brank2 = None
    brank3 = None
    print(f"intはobjectのサブクラスか？ -> {brank1}")
    print(f"Sampleはobjectのサブクラスか？ -> {brank2}")

    print("_"*40)

    # Pythonではすべてのクラスはオブジェクトである.
    # クラスがオブジェクトであるならば, 型が存在する.

    brank4 = None
    print(f"objectの型は何か？ -> {brank4}")

    print("_"*40)

    # また, brank4はobjectの型であるが, objectのサブクラスでもある.
    # ただし当然ながら, objectはbrank4のサブクラスではない.

    brank5 = None
    print(f"{brank4}はobjectのサブクラスか？ -> {brank5}")
    brank6 = None
    print(f"objectは{brank4}のサブクラスか？ -> {brank6}")

    print("_"*40)

    # ところで, 組み込み関数intを用いることで, intのオブジェクトを動的に生成できる.

    print("intのオブジェクトを動的に生成する.")
    one = int("1")

    print("_"*40)

    # 同様に, brank4を用いることで, クラスを動的に生成できるはずである.
    # 以下に定義する関数mewを属性に持つクラスCatを動的に生成せよ.

    def mew(times=1):
        return "MEW! " * times

    # print(Cat.mew(3))

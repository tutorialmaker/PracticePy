class Sample:
    pass


if __name__ == "__main__":

    # 以下に定義する変数brank1からbrank7に, 文脈上適切な関数を用いてオブジェクトを与えよ.
    # ただし, 必要に応じてモジュールをインポートしてよい.

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

    # ところで, int, floatそしてcomplexはいずれも数の型であり,
    # 四則演算など多くの共通のインターフェースを持つが,
    # (object以外の)共通の基底クラスを継承している訳ではない.
    # その代わり, 数の抽象基底クラスが定義されている.
    # ゆえにオブジェクトが数であるかどうかは,
    # この抽象基底クラスを用いて判定することができる.

    brank6 = None
    print(f"{int.__name__}, {float.__name__}そして{complex.__name__}は"\
            f"({object.__name__}以外の)共通の基底クラスを継承しているか? -> {brank6}")
    brank7 = None
    print(f"{1+3j}は数か? -> {brank7}")

    print("_"*40)

    # ところで, 組み込み関数intを用いることで, intのオブジェクトを動的に生成できる.

    print(f"{int.__name__}のオブジェクトを動的に生成する.")
    
    one = int("1")
    
    print(one)

    print("_"*40)

    # 同様に, brank4を用いることで, クラスを動的に生成できるはずである.
    # 以下に定義する関数mewを属性に持つクラスCatを動的に生成せよ.

    def mew(times=1):
        return "MEW! " * times

    # print(Cat.mew(3))

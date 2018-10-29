def empty():
    pass


if __name__ == "__main__":
    """

    (1)から(5)の出力結果はすべてTrueである.

    以下に示すクラス

    bool
    float
    int
    str

    または関数(引数は各自で設定する)

    type()

    を, objectの代わりにtype_1からtype_5に一回づつ代入し,
    (1)から(5)の出力結果をすべてTrueにせよ.

    """
    type_1 = int
    print(isinstance(0, type_1)) # (1)

    type_2 = float
    print(isinstance(0., type_2)) # (2)

    type_3 = str
    print(isinstance("0", type_3)) # (3)

    type_4 = bool
    print(isinstance(False, type_4)) # (4)

    type_5 = type(None)
    print(isinstance(empty(), type_5)) # (5)

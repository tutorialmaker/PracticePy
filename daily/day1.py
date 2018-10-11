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
    type

    を, objectの代わりにtype_1からtype_5に一回づつ代入し,
    (1)から(5)の出力結果をすべてTrueにせよ.

    """
    type_1 = object
    print(isinstance(0, type_1)) # (1)

    type_2 = object
    print(isinstance(0., type_2)) # (2)

    type_3 = object
    print(isinstance("0", type_3)) # (3)

    type_4 = object
    print(isinstance(False, type_4)) # (4)

    type_5 = object
    print(isinstance(empty(), type_5)) # (5)

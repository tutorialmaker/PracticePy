def make_dict(keys, values):
    """

    関数make_dictはkeys, valuesより辞書を作成し辞書を返す.

    引数
    keys : イテラブルオブジェクト
    values : イテラブルオブジェクト

    返り値
    d : 辞書

    """

    d = dict(zip(keys, values))

    return d


def break_dict(d):
    """

    dのキーをkeys, バリューをvaluesというリストで返す関数break_dictを作成せよ.

    引数
    d : 辞書

    返り値
    keys : リスト
    values : リスト

    """
    
    pass

    return keys, values


if __name__ == "__main__":
    keys0 = (
        "key0",
        "key1",
        "key2",
        "key3",
    )

    values0 = (
        "value0",
        "value1",
        "value2",
        "value3",
    )

    print("keys0\n", keys0)
    print("values0\n", values0)

    print("Run the make_dict.")
    d = make_dict(keys0, values0)
    print(d)

    print("Run the break_dict.")
    keys1, values1 = break_dict(d)
    print("keys1\n", keys1)
    print("values1\n", values1)

def make_dict(keys, values):
    """

    関数make_dictはkeys, valuesより辞書(ハッシュと呼ぶこともある)を作成し辞書を返す.

    引数
    keys: Iterable[Any]
    values: Iterable[Any]

    返り値
    dict: Dict[Any, Any]

    """

    dict = dict(zip(keys, values))

    return dict


def break_dict(d):
    """

    dのキーをkeys, バリューをvaluesというリストで返す関数break_dictを作成せよ.

    引数
    d: Dict[Any, Any]

    返り値
    keys: List[Any]
    values: List[Any]

    """

    pass

    # return keys, values


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

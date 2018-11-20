def invert_num(num: int) -> int:
    return num * -1


if __name__ == '__main__':
    nums = range(0, 10)
    print(list(nums))

    # 1, mapは第一引数に関数自体(計算する前の関数)を引数にとり、第二引数の配列を一つづつ代入し新しい配列を作成します
    inverted_map_1 = map(invert_num, nums)

    # 2, lambda式というものを使うと、その場で関数を名前を付けず生成することができます
    inverted_map_2 = map(lambda num: num * -1, nums)

    # 3, mapを使わなくてもpythonにはリスト内包というものがあります
    inverted_map_3 = [num * -1 for num in nums]

    # 4, ジェネレータ内包表記もあります
    inverted_map_4 = (num * -1 for num in nums)

    # python3ではmap objectは遅延評価
    print(list(inverted_map_1))
    print(list(inverted_map_2))

    # inveted_map_3はリストなので遅延評価ではない
    print(inverted_map_3)

    # inverted_map_4はイテレータなので遅延評価
    print(list(inverted_map_4))

    # mapは元の配列に変化は起こしません
    print(list(nums))

    # TODO: 30~100までの数字の配列(nums_2)を作り
    # 上記1, 2, 3, 4の方法にならい、それぞれ100を引いてみてください
    # また3と4の方法について, それぞれのオブジェクトのサイズを示してください
    # ただしnums_2の中身は変更しないようにしてください

    # nums_2 =
    # print(list(nums))

    # hundredfold_map_1 =
    # hundredfold_map_2 =
    # hundredfold_map_3 =
    # sizeof3 =
    # hundredfold_map_4 =
    # sizeof4 =

    # print(list(hundredfold_map_1))
    # print(list(hundredfold_map_2))
    # print(hundredfold_map_3)
    # print(f"hundredfold_map_3 : {sizeof3} bytes")
    # print(list(hundredfold_map_4))
    # print(f"hundredfold_map_4 : {sizeof4} bytes")
    # print(nums_2)

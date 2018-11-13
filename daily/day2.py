def coord(x, y):
    """

    関数coordはx, yをリストとして返す.

    引数
    x : 数値
    y : 数値

    返り値
    c : リスト

    """

    c = [x, y]

    return c


def manhattan_dist(coord1, coord2):
    """

    coord1とcoord2はどちらも長さ2のリストが与えられるとする.
    ふたつのリストを座標とみなし、L1距離を返す関数manhattan_distを作成せよ.

    引数
    coord1 : リスト
    coord2 : リスト

    返り値
    l1 : 数値

    """
    pass

    # return l1

    x = abs(coord1[0]-coord2[0])
    y = abs(coord1[1]-coord2[1])
    return x+y


if __name__ == "__main__":
    x = float(input("Input a x = "))
    y = float(input("Input a y = "))

    print("Run the coord.")
    A = coord(x, y)
    print(A)

    x = float(input("Input a x = "))
    y = float(input("Input a y = "))
    print("Run the coord.")
    B = coord(x, y)
    print(B)

    print("Run the manhattan_dist.")
    print(manhattan_dist(A, B))

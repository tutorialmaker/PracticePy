def coord(x, y):
    """

    関数coordはx, yをリストとして返す.

    引数
    x: Union[int, float]
    y: Union[int, float]

    返り値
    result: List[Union[int, float]]

    """

    result = [x, y]

    return result


def manhattan_dist(coord1, coord2):
    """

    coord1とcoord2はどちらも長さ2のリストが与えられるとする.
    ふたつのリストを座標とみなし、距離(distance)を返す関数manhattan_distを作成せよ.

    引数
    coord1: List[Union[int, float]]
    coord2: List[Union[int, float]]

    返り値
    distance: Union[int, float]

    """
    pass

    # return distance


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

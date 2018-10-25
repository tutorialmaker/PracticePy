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
    l1 = abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
    return l1


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

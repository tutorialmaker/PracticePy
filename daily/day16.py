"""

    TODOを実装せよ.

"""
from numbers import Number
from reprlib import recursive_repr


class Matrix(list):
    """
    行列

    Parameters
    ----------
    M : Iterable

    """
    def __init__(self, M):
        super().__init__(M)

        row_length_list = []
        for i, row in enumerate(self):
            if not hasattr(row, "__iter__"):
                raise TypeError(f"{type(row)} object is not iterable")
            elif not isinstance(row, list):
                self[i] = row = list(row)

            row_length_list.append(len(row))
            for e in row:
                if not isinstance(e, Number):
                    raise TypeError(
                        f"Matrix element must be a Number, not {type(e)}")

        row_length = max(row_length_list)
        if row_length != min(row_length_list):
            raise ValueError(f"unexpected Matrix shape")
        column_length = len(row_length_list)
        self.__shape = (column_length, row_length)

    def __mul__(self, other):
        # TODO: 行列積の計算を実装
        return NotImplemented

    @property
    def shape(self):
        # TODO: ドキュメンテーションを追記
        return self.__shape

    def getT(self):
        """
        転置した行列を返す.

        Parameters
        ----------
        None

        Returns
        -------
        ret : Matrix
            自身の転置行列.

        """
        # TODO: 転置を返すメソッドを実装
        pass

    @recursive_repr()
    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"

    # TODO: 転置について読み取り専用のアクセサを実装


if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7],
         [8],
         [9]]

    try:
        import numpy as np
        """

            NumPyを用いてAとBの内積を求めよ.

        """

    except ImportError:
        """

            定義したMatrixを用いてAとBの内積を求めよ.

        """

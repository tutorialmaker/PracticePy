"""

    TODOを実装せよ.

"""
from numbers import Number
from reprlib import recursive_repr


class Matrix(list):
    """行列

    Parameters
    ----------
    M : Iterable

    """
    __slots__ = ["_shape", ]

    def __init__(self, M):
        super().__init__(M)

        rlens = []
        for row in self:
            if not hasattr(row, "__iter__"):
                raise TypeError(f"{type(row)} object is not iterable")
            elif not isinstance(row, list):
                row = list(row)

            rlens.append(len(row))
            for v in row:
                if not isinstance(v, Number):
                    raise TypeError(
                        f"Matrix element must be a Number, not {type(v)}")

        rlen = max(rlens)
        if rlen != min(rlens):
            raise ValueError(f"unexpected Matrix shape")
        clen = len(rlens)
        self._shape = (clen, rlen)

    def __mul__(self, other):
        # TODO: 行列積の計算を実装
        return NotImplemented

    def getshape(self):
        return self._shape

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

    shape = property(getshape, None)
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

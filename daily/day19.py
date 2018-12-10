"""
    (α)
    以下のドキュメンテーションに示すような関数checkを実装せよ.

    リーチおよびビンゴの有無を調べる.

    Parameters
    ----------
    card : BingoCard
        BingoCardのインスタンス

    Returns
    -------
    result : None or str
        cardにリーチが含まれるならば'reach',
        リーチの有無に関わらずビンゴが含まれるならば'bingo',
        リーチもビンゴも含まれないならばNone.

    (β)
    以下のドキュメンテーションに示すようなジェネレータsimulateを実装せよ.

    ビンゴゲームをシミュレーションする.
    最大でカードに含まれうる数字の数だけ反復可能である.

    Parameters
    ----------
    players : int
        ビンゴゲームの参加人数
    size : int, default 5
        カードの列および行数
    high : int, default 75
        カードが含む数字の最大値
    low : int, default 1
        カードが含む数字の最小値

    Yield
    -----
    report : List
        各参加者のカードにビンゴおよびリーチが含まれるかどうか示す.
        カードにリーチが含まれるならば'reach',
        リーチの有無に関わらずビンゴが含まれるならば'bingo',
        リーチもビンゴも含まれないならばNoneで表す.

    (γ)
    NumPyを用いてBingoCardと同様の機能を持つBingoCard2を新たに定義せよ.

    (δ)
    timeitを用いてBingoCardとBingoCard2でビンゴゲームをシミュレーションした場合の
    処理時間を測定し, 測定結果をコメントアウトに記載せよ.
    ただし参加者数は10人, カードの列および行数は99マスとし,
    シミュレーション10回分の処理時間を求めよ.

    (ε)
    Matplotlibを用いてビンゴゲームのシミュレーション結果をグラフに出力せよ.
    ただし参加者数は1000人, カードの列および行数は5マス,
    カードが含む数字の最大値は75, 最小値は1とし, リーチのカードを持つ参加者数と
    ビンゴとなったカードを持つ参加者数の推移を折れ線グラフで出力せよ.

"""
import random


class _Count:
    """
    各行, 列および対角上でスタンプされた番号の総数を記録する.
    """
    __slots__ = 'size', 'row', 'col', 'diag'

    def __init__(self, size):
        self.size = size
        self.row = dict(zip(range(size), [0]*size))
        self.col = dict(zip(range(size), [0]*size))
        self.diag = {0: 0, 1: 0}

    def filled(self, i, j):
        """i行j列の番号がスタンプされたことを記録する."""
        self.row[i] += 1
        self.col[j] += 1
        if i == j:
            self.diag[0] += 1
        if i + j == self.size - 1:
            self.diag[1] += 1


class BingoCard:
    """
    ビンゴカード

    Parameters
    ----------
    size : int, default 5
        カードの列および行数
    high : int, default 75
        カードが含む数字の最大値
    low : int, default 1
        カードが含む数字の最小値

    """
    __slots__ = '_filled', '_count', '_squares'

    def __init__(self, size=5, high=75, low=1):
        if size % 2 == 0:
            raise ValueError(f'size must be odd, got {size}')
        elif high - low < size ** 2 - 1:
            low, high = 1, size ** 2

        self._filled = 'X' * len(str(high))
        values = list(range(low, high))
        random.shuffle(values)
        center = int(size/2)
        around = int(size**2/2)
        values = values[:around] + [self._filled] + values[around:]
        self._squares = [values[size*p:size*(p+1)] for p in range(size)]
        self._count = _Count(size)
        self._count.filled(center, center)

    def stamped(self, num):
        """引数の番号がカードにあるならば, 番号をスタンプする."""
        squares = self._squares
        size = len(squares)
        for i in range(size):
            for j in range(size):
                if squares[i][j] == num:
                    squares[i][j] = self._filled
                    self._count.filled(i, j)

    @property
    def count(self):
        """各行, 列および対角上でスタンプされた番号の総数を返す."""
        count = self._count
        report = {'row': count.row,
                  'col': count.col,
                  'diag': count.diag}
        return report

    def __repr__(self):
        if not self:
            return f'{self.__class__.__name__}'

        squares = self._squares
        size = len(squares)
        digit = len(self._filled)
        header = footer = '+' + '-' * (size * digit + size - 1) + '+'
        card = header
        for row in squares:
            card += '\n' + '|'
            for e in row:
                card += str(e).zfill(digit) + '|'
        card += '\n' + footer
        return f'{card}'


if __name__ == "__main__":
    """

    実行するコードを実装する.

    """

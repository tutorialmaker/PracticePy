import random


class _Count:
    __slots__ = 'size', 'row', 'col', 'diag'

    def __init__(self, size):
        self.size = size
        self.row = dict(zip(range(size), [0]*size))
        self.col = dict(zip(range(size), [0]*size))
        self.diag = {0: 0, 1: 0}

    def filled(self, i, j):
        self.row[i] += 1
        self.col[j] += 1
        if i == j:
            self.diag[0] += 1
        if i + j == self.size - 1:
            self.diag[1] += 1


class BingoCard:
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

    def get(self, num):
        squares = self._squares
        size = len(squares)
        for i in range(size):
            for j in range(size):
                if squares[i][j] == num:
                    squares[i][j] = self._filled
                    self._count.filled(i, j)

    @property
    def count(self):
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

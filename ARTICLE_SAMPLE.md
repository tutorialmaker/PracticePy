## 問題

[day1](https://github.com/tutorialmaker/PracticePy/blob/master/daily/day1.py)

## 解説(Python 3.6.5)

### [isinstance](https://docs.python.jp/3/library/functions.html#isinstance)

組み込み関数isinstanceは第一引数が第二引数のインスタンスの場合に```True```を返す。
例えば```0```はintのインスタンスなので

```python
isinstance(0, int)
```

は```True```を返す。

### [type](https://docs.python.jp/3/library/functions.html#type)

組み込み関数typeは引数が一つだけの場合、引数のオブジェクトの型オブジェクトを返す。例えばヌルオブジェクト```None```を引数にとる場合

```python
type(None)
```

上記の返り値は型オブジェクト```<class 'NoneType'>```である。

故にオブジェクト(仮に```obj```とする)がヌルオブジェクトである場合、

```python
isinstance(obj, type(None))
```

は```True```を返す。

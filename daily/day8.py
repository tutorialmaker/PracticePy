import random

def to_str(string):
    return string.decode()

def o_or_x(fitzpatrick_scale):
    l = [0x1F645, 0x1F646]
    color = [0, 0x1f3fb, 0x1f3fc, 0x1f3fd, 0x1f3fe, 0x1f3ff]
    utf = chr(random.choice(l)).encode() + chr(color[fitzpatrick_scale%6]).encode()
    print(to_str(utf))

if __name__ == "__main__":
    """
    バイト列を引数に取り, Unicode文字に復号化してその結果を返す関数to_strを定義せよ.
    関数to_strを用いて以下のバイト列
    \xf0\x9f\x91\x8d
    を復号せよ.
    またUnicodeコードポイントで1F645または1F646の文字をランダムに返す関数o_or_xを定義し実行せよ.
    ただし引数fitzpatrick_scaleを定義し, これに与える整数の値により返す文字の色調を変更できるようにせよ.
    """
    print(to_str(b'\xf0\x9f\x91\x8d'))
    for i in range(100):
        o_or_x(i)

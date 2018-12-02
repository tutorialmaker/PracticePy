import random

def to_str(string):
    return string.decode()

def o_or_x(fitzpatrick_scale):
    l = [0x1F645, 0x1F646]
    color = [0x1f3fb, 0x1f3fc, 0x1f3fd, 0x1f3fe, 0x1f3ff]
    try:
        if fitzpatrick_scale == 0:
            utf = chr(random.choice(l)).encode()
        else:
            utf = chr(random.choice(l)).encode() + chr(color[fitzpatrick_scale-1]).encode()
        return to_str(utf)
    except IndexError as e:
        return e

if __name__ == "__main__":
    """
    バイト列を引数に取り, Unicode文字に復号化してその結果を返す関数to_strを定義せよ.
    関数to_strを用いて以下のバイト列
    \xf0\x9f\x91\x8d
    を復号せよ.
    またUnicodeコードポイントで1F645または1F646の文字をランダムに返す関数o_or_xを定義し実行せよ.
    また引数fitzpatrick_scaleを定義し, これに与える1から5の整数の値により返す文字の色調を変更できるようにせよ.
    ただしfitzpatrick_scaleに0から5以外の値が与えられた場合, エラーを出力せよ.
    """
    print(to_str(b'\xf0\x9f\x91\x8d'))
    for i in range(7):
        print(o_or_x(i))

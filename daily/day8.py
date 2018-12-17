import random


def to_str(byte):
    return byte.decode()


def o_or_x(fitzpatrick_scale):
    uni = [0x1F645, 0x1F646]
    color = [0x1F3FB, 0x1F3FC, 0x1F3FD, 0x1F3FE, 0x1F3FF]
    str_pic = chr(random.choice(uni))
    if fitzpatrick_scale == 0:
        return str_pic
    elif fitzpatrick_scale in range(1, 6):
        str_pic_color = str_pic + chr(color[fitzpatrick_scale-1])
        return str_pic_color
    else:
        raise ValueError("The value input is invalid .")


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
    print(to_str(b"\xf0\x9f\x91\x8d"))
    i = int(input("0~5の値を入力してください"))
    print(o_or_x(i))

import random


def to_str(bytes):
    str = bytes.decode('utf-8')
    return str


def o_or_x(fitzpatrick_scale):
    fitzpatrick_scale = num_checker(fitzpatrick_scale)
    color = change_color(fitzpatrick_scale)
    num = random.randrange(2)
    if num == 1:
        codepoint = '\U0001F645'
    else:
        codepoint = '\U0001F646'
    if color is None:
        codepoint = codepoint
    else:
        codepoint = codepoint + color
    codepoint = codepoint.encode()
    return codepoint


def change_color(num):
    list = [None, '\U0001F3FB', '\U0001F3FC',
            '\U0001F3FD', '\U0001F3FE', '\U0001F3FF']
    color = list[num]
    return color


def num_checker(num):
    if num < 0 or num > 5:
        raise ValueError('入力された値は,指定された範囲を超えています.')
    return num


def main():
    str = to_str(b'\xf0\x9f\x91\x8d')
    print(str)
    print('0~5の範囲の整数を入力してください.')
    fitzpatrick_scale = int(input())

    codepoint = o_or_x(fitzpatrick_scale)
    print(to_str(codepoint))


if __name__ == "__main__":
    """

    バイト列を引数に取り, Unicode文字に復号化してその結果を返す関数to_strを定義せよ.
    関数to_strを用いて以下のバイト列

    \xf0\x9f\x91\x8d

    を復号せよ.
    またUnicodeコードポイントで1F645または1F646の文字をランダムに返す関数o_or_xを定義し実行せよ.
    また引数fitzpatrick_scaleを定義し, これに与える1から5のintにより返す文字の色調を変更できるようにせよ.
    ただし0が与えられた場合, 色調はデフォルトを適用し,
    fitzpatrick_scaleに0から5以外のintが与えられた場合, 適切なエラーを出力せよ.


    """
    main()

import random

def to_str(bytes):
    str = bytes.decode('utf-8')
    return str

def o_or_x():
    num = random.randrange(1)
    if num == 1:
        return '\U0001F645'
    else:
        return '\U0001F646'

def change_color(num):
    if num == 0:
        color = None
    elif num == 1:
        color = '\U0001F3FB'
    elif num == 2:
        color = '\U0001F3FC'
    elif num == 3:
        color = '\U0001F3FD'
    elif num == 4:
        color = '\U0001F3FE'
    elif num == 5:
        color = '\U0001F3FF'
    return color

def num_checker(num):
    flag = 0
    while flag == 0:
        if num < 0 or num > 5:
            print('入力された値は%dです.指定された範囲を超えています.' % num)
            print('0~5の範囲の整数を入力してください.')
            num = int(input())
        else:
            flag = 1
    return num

def main():
    str = to_str(b'\xf0\x9f\x91\x8d')
    print(str)
    print('0~5の範囲の整数を入力してください.')
    fitzpatrick_scale = int(input())

    fitzpatrick_scale = num_checker(fitzpatrick_scale)
    fitzpatrick_scale = change_color(fitzpatrick_scale)

    codepoint = o_or_x()
    codepoint = codepoint + fitzpatrick_scale
    codepoint = codepoint.encode()
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

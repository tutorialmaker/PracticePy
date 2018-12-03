from collections import OrderedDict
from day5 import get_pokemon_data

if __name__ == "__main__":
    """
    day5で作成した順序付き辞書に対して,
    存在しないキー(例えば"MissingNo.")をキーとしてバリューの取得を試みた場合,
    KeyErrorが発生する.
    day5で定義した関数get_pokemon_dataをインポートし,
    day5で作成した順序付き辞書を再び作成, これを用いて存在しないキーを指定した場合,
    KeyErrorを発生させずにデフォルトとしてNoneを返すようなバリューの取得方法について
    以下の二つの方法で示せ.

    (α)
    バリューを取得した場合, 辞書から取得したバリューのキーを削除する.

    (β)
    バリューを取得した場合でも, 辞書から取得したバリューのキーを削除しない.
    """
    bmi_dict = OrderedDict()
    for i in range(1, 152):
        get_pokemon = get_pokemon_data(i)
        name = get_pokemon["name"]
        weight = get_pokemon["weight"]/10
        height = get_pokemon["height"]/10
        bmi = weight / (height**2)
        bmi_dict[name] = bmi

    sorted_dict = OrderedDict(sorted(bmi_dict.items(), key=lambda x: x[1], reverse=True))

    # (α)
    value = sorted_dict.pop("MissingNo.", None)
    print(value)

    # (β)
    value = sorted_dict.get("MissingNo.")
    print(value)

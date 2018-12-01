from collections import OrderedDict
from day5 import get_pokemon_data, calc_bmi

NUMBER = 20

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
    バリューを取得した場合, 辞書から取得したキーを削除する.

    (β)
    バリューを取得した場合でも, 辞書から取得したキーを削除しない.
    """

    bmi_dict = OrderedDict()
    for i in range(1,NUMBER+1):
        # print(str(i) + "/" + str(MAX_NUMBER))
        poke_data = get_pokemon_data(i)
        bmi_dict[poke_data['name']] = calc_bmi(poke_data['weight'], poke_data['height'])
    ordered_bmi_dict = OrderedDict(sorted(bmi_dict.items(), key=lambda x: x[1], reverse=True))

    value = ordered_bmi_dict.get('metapod')
    print(value)
    value = ordered_bmi_dict.get('metapod')
    print(value)
    value = ordered_bmi_dict.pop('pidgey', None)
    print(value)
    value = ordered_bmi_dict.pop('pidgey', None)
    print(value)

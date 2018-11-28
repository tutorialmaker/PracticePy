import urllib.request
import json
import collections
from collections import OrderedDict

def get_pokemon_data(n):
    """
    関数get_pokemon_dataはAPI(https://pokeapi.co/api/v2/)を利用することにより,
    ずかん番号に対応するポケモンの情報を返す.
    引数
    n : 整数
    返り値
    data : 辞書
    """
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(n)
    req = urllib.request.Request(url, headers={"User-Agent": "dummy"})
    with urllib.request.urlopen(req) as f:
        data = json.loads(f.read().decode("utf-8"))

    return data


if __name__ == "__main__":
    """
     関数get_pokemon_dataを用いて,
    キーにポケモンの名称、バリューにそのポケモンのBMIを持つ辞書を作成せよ.
    キーにポケモンの名称, バリューにそのポケモンのBMIを持つ辞書を作成せよ.
    またBMIが高い順に並んだ順序付き辞書を作成せよ.
     また, 引数をしきい値として,
    しきい値を下回るBMIのポケモンのみによる順序付き辞書を返す関数を定義して実行せよ.
     ただしポケモンの名称および重量および高さは, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"および"height"に対応しており,
    "weight"および"height"の値の単位はそれぞれ0.1メートルおよび0.1キログラムである.
    """
    bmi_dict = OrderedDict()
    for i in range(1, 5):
        get_pokemon = get_pokemon_data(i)
        name = get_pokemon["name"]
        weight = get_pokemon["weight"]
        height = get_pokemon["height"]
        bmi = weight / (height**2)
        bmi_dict[name] = bmi
    print(bmi_dict)

    sorted_dict = OrderedDict(sorted(bmi_dict.items(), key=lambda x: x[1], reverse=True))
    print(sorted_dict)

    n = int(input())

    def threshold(n):
        threshold_dict = sorted_dict
        for name in list(sorted_dict):
            if threshold_dict[name] < n:
                pass
            else:
                threshold_dict.pop(name)
        return OrderedDict(sorted(threshold_dict.items(), key=lambda x: x[1], reverse=True))
    print(threshold(n))

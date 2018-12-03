import urllib.request
import urllib.error
import json
from collections import OrderedDict

def get_pokemon_data(n):
    """
    関数get_pokemon_dataはAPI(https://pokeapi.co/api/v2/)を利用することにより,
    ずかん番号に対応するポケモンの情報を返す.
    引数
    n : int
    返り値
    data : Dict[Any, Any]
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{n}/'
    req = urllib.request.Request(url, headers={"User-Agent": "dummy"})
    try:
        with urllib.request.urlopen(req) as f:
            data = json.loads(f.read().decode("utf-8"))
        return data
    except urllib.error.URLError:
        print("\nError: The requested URL could not be retrived. \
                        Are you connected to the Internet?\n")


if __name__ == "__main__":
    """
    関数get_pokemon_dataを用いて,
    キーにポケモンの名称, バリューにそのポケモンのBMIを持つ辞書を作成せよ.
    またBMIが高い順に並んだ順序付き辞書を作成せよ.
    また, 引数にしきい値とBMIが高い順に並んだ順序付き辞書をとり,
    しきい値を下回るBMIのポケモンのみによる順序付き辞書を返す関数を定義して実行せよ.
    ただしポケモンの名称および重量および高さは, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"および"height"に対応しており,
    "weight"および"height"の値の単位はそれぞれ0.1メートルおよび0.1キログラムである.
    """

    bmi_dict = OrderedDict()
    for i in range(1, 152):
        get_pokemon = get_pokemon_data(i)
        name = get_pokemon["name"]
        weight = get_pokemon["weight"]/10
        height = get_pokemon["height"]/10
        bmi = weight / (height**2)
        bmi_dict[name] = bmi
    print(bmi_dict)

    sorted_dict = OrderedDict(sorted(bmi_dict.items(), key=lambda x: x[1], reverse=True))
    print(sorted_dict)

    n = int(input())

    def threshold(n, threshold_dict):
        final_dict = OrderedDict()
        for name in threshold_dict.keys():
            if threshold_dict[name] < n:
                final_dict[name] = threshold_dict[name]
        return final_dict
    print(threshold(n, sorted_dict))

import urllib.request
import json
import collections


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
    またBMIが高い順に並んだ順序付き辞書を作成せよ.

    また, 引数にしきい値とBMIが高い順に並んだ順序付き辞書をとり,
    しきい値を下回るBMIのポケモンのみによる順序付き辞書を返す関数を定義して実行せよ.

    ただしポケモンの名称および重量および高さは, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"および"height"に対応しており,
    "weight"および"height"の値の単位はそれぞれ0.1メートルおよび0.1キログラムである.

    """
#keyにポケモンの名前valueにBMIをもつ辞書の作成
pokemon_dict = {}
for i in range(3):
    pokemon = get_pokemon_data(i+1)
    pokemon_name = pokemon["name"]
    pokemon_bmi = (pokemon["weight"]/(pokemon["height"])**2)*10
    pokemon_dict[pokemon_name] = pokemon_bmi
print(pokemon_dict)

#BMIの高い順に並び替え
dict_sorted = {}
dict_sorted = OrderedDict()
for k, v in sorted(pokemon_dict.items(), key=lambda x: x[1], reverse=True):
    dict_sorted[k] = v
print(dict_sorted)

#引数にしきい値とBMIが高い順に並んだ順序付き辞書をとって閾値以下のBMIのポケモンのみの辞書を返す
def threshold(x,dict_sorted):
    under_threshold = {}
    for k, v in dict_sorted.items():
        if v < x:
            under_threshold[k] = v
    under_threshold = dict(sorted(under_threshold.items(), key=lambda x:x[1], reverse=True))
    return under_threshold
print(threshold(15,dict_sorted))

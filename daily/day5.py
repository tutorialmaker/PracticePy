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

    ただしポケモンの名称および重量および高さは, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"および"height"に対応しており,
    "weight"および"height"の値の単位はそれぞれ0.1メートルおよび0.1キログラムである.

    """

pokemon_dict = {}
for i in range(3):
    pokemon = get_pokemon_data(i+1)
    pokemon_name = pokemon["name"]
    pokemon_bmi = (pokemon["weight"]/(pokemon["height"])**2)*10
    pokemon_dict[pokemon_name] = pokemon_bmi
print(pokemon_dict)

dict_sorted = {}
for k, v in sorted(pokemon_dict.items(), key=lambda x: x[1], reverse=True):
    dict_sorted[k] = v
print(dict_sorted)

def under_threshold(x):
    dict_under_threshold = {}
    for i in range(1,5):
        data = get_pokemon_data(i)
        name = data["name"]
        weight = data["weight"]
        height = data["height"]
        BMI = weight/height**2
        bmi = BMI*10
        if bmi < x:
            dict_under_threshold[name] = bmi
            dict_sort = {}
            for k, v in sorted(dict_under_threshold.items(), key=lambda x: x[1], reverse=True):
                dict_sort[k] = v
    return dict_sort

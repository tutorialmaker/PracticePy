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

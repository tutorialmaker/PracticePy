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
    以下に示すような, キーにポケモンの名称、バリューにそのポケモンの重量を持つ辞書を作成せよ.

    {
        'bulbasaur': 69, 'ivysaur': 130, 'venusaur': 1000,
        'charmander': 85, 'charmeleon': 190, 'charizard': 905,
        'squirtle': 90, 'wartortle': 225, 'blastoise': 855
    }

    さらに以下に示すような, 重量が重い順に並んだ順序付き辞書を作成せよ.

    OrderedDict([
        ('venusaur', 1000), ('charizard', 905), ('blastoise', 855),
        ('wartortle', 225), ('charmeleon', 190), ('ivysaur', 130),
        ('squirtle', 90), ('charmander', 85), ('bulbasaur', 69)
        ])

    ただしポケモンの名称および重量は, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"に対応している.

    """

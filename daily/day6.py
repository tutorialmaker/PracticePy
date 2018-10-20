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

    {
    'bulbasaur': 7, 'ivysaur': 10, 'venusaur': 20,
    'charmander': 6, 'charmeleon': 11, 'charizard': 17,
    'squirtle': 5, 'wartortle': 10, 'blastoise': 16
    }

    といったキャラクターの名前、高さの辞書を作成してください。

    さらに、_辞書内包表記_を用いて以下のような_高さが1.0m以下_の
    ポケモンの名前、高さの辞書を1~30番までのポケモンで作成してください。

    {
    'bulbasaur': 7, 'ivysaur': 10, 'charmander': 6,
    'squirtle': 5, 'wartortle': 10, 'caterpie': 3,
    ...
    'sandshrew': 6, 'sandslash': 10, 'nidoran-f': 4
    }
    
    0.1m = 1であることに注意してください。
    """

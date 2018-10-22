import urllib.request
import json
import collections

def get_pokemon_data_sp(n):
    """

    関数get_pokemon_data_spはAPI(https://pokeapi.co/api/v2/)を利用することにより,
    ずかん番号に対応するポケモンの図鑑情報を返す.

    引数
    n : 整数

    返り値
    data : 辞書

    """
    url = 'https://pokeapi.co/api/v2/pokemon-species/{}/'.format(n)
    req = urllib.request.Request(url, headers={"User-Agent": "dummy"})
    with urllib.request.urlopen(req) as f:
        data = json.loads(f.read().decode("utf-8"))

    return data


if __name__ == "__main__":
    """

    関数get_pokemon_data_spをコンストラクタに用い、
    ポケモンの分類(genera)、名前(names)に関するクラスPokemonI18nを作成してください。
    このクラスでは引数に言語コードをとり、その言語コードにおけるポケモンの分類、名前を返すメソッドを定義してください。
    メソッド名は分類->group、名前->nameとしてください。
    ただし、引数の言語コードは、APIから取得できる言語しか与えられないことを想定して構いません。

    また、図鑑番号1~15の範囲で、図鑑番号に対応した情報を返す辞書pokemon_infoを作成してください。

    この課題ではAPIから取得されるデータのキーに関する情報は最低限しか与えられません。
    まずはhttps://pokeapi.co/api/v2/pokemon-species/1
    のデータを取得して、どのようなデータがあるのかを確かめてください。

    """

    # print(pokemon_info[1].name('en')) # Bulbasaur
    # print(pokemon_info[1].group('de')) # Samen
    # print(pokemon_info[2].name('roomaji')) # Fushigisou
    # print(pokemon_info[2].group('fr')) # Pokémon Graine

import urllib.request
import urllib.error
import json


def kanto_pokedex():
    """

    関数kanto_pokedexはAPI(https://pokeapi.co/api/v2/)を利用することにより,
    ずかん番号1から151に対応するポケモンの情報を返す.

    返り値
    pokemons : List[Any]

    """

    url = "https://pokeapi.co/api/v2/pokedex/2"
    req = urllib.request.Request(url, headers={"User-Agent": "dummy"})
    try:
        with urllib.request.urlopen(req) as f:
            pokemons = json.loads(f.read().decode("utf-8"))["pokemon_entries"]
        return pokemons
    except urllib.error.URLError:
        print("\nError: The requested URL could not be retrived. Are you connected to the Internet?\n")


if __name__ == "__main__":
    """

    関数kanto_pokedexを用いて,
    ずかん番号1から151に対応するポケモンの名称をリストpokemon_nameに格納せよ.

    """

    # print(pokemon_name)

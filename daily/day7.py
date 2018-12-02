from day5 import get_pokemon_data

class Pokedex:
    def __init__(self):
        self._pokemons = {}

    @property
    def pokemons(self):
        return self._pokemons

    @pokemons.getter
    def pokemons(self):
        return self._pokemons

    @pokemons.setter
    def pokemons(self, data):
        self._pokemons.update({data['id']: data})

    @pokemons.deleter
    def pokemons(self):
        del self._pokemons


if __name__ == "__main__":
    """
    day5で定義した関数get_pokemon_dataをインポートし,
    バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトの辞書を
    プロパティとするクラスPokedexを, 以下に示すコードを適切に実行できるよう修正せよ.
    # Pokedexのインスタンスを生成する.
    mypkd = Pokedex()
    # n10およびn20はポケモンずかんにおけるポケモンの番号を表す.
    n10, n20 = 10, 20
    # mypkdのセッターを用いて, mypkdのインスタンス変数_pokemonsに,
    # バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトを設定する.
    mypkd.pokemons = get_pokemon_data(n10)
    mypkd.pokemons = get_pokemon_data(n20)
    # mypkdのゲッターを用いて, _pokemonsを取得する.
    pokemons = mypkd.pokemons
    # 取得した辞書からずかん番号10のポケモンの名称を出力する.
    print(pokemons[n10]["name"])
    # キーがn10のオブジェクトを削除する.
    del mypkd.pokemons[n10]
    # 取得した辞書からずかん番号20のポケモンの名称を出力する.
    print(pokemons[n20]["name"])
    """

    # Pokedexのインスタンスを生成する.
    mypkd = Pokedex()
    # n10およびn20はポケモンずかんにおけるポケモンの番号を表す.
    n10, n20 = 10, 20
    # mypkdのセッターを用いて, mypkdのインスタンス変数_pokemonsに,
    # バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトを設定する.
    mypkd.pokemons = get_pokemon_data(n10)
    mypkd.pokemons = get_pokemon_data(n20)
    # mypkdのゲッターを用いて, _pokemonsを取得する.
    pokemons = mypkd.pokemons
    # 取得した辞書からずかん番号10のポケモンの名称を出力する.
    print(pokemons[n10]["name"])
    # キーがn10のオブジェクトを削除する.
    del mypkd.pokemons[n10]
    # 取得した辞書からずかん番号20のポケモンの名称を出力する.
    print(pokemons[n20]["name"])

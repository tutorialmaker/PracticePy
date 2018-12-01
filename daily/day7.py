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
        self._pokemons = {data['id']: data}

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
    # numberはポケモンずかんにおけるポケモンの番号を表す.
    number = 10
    # mypkdのセッターを用いて, mypkdのインスタンス変数_pokemonsに,
    # バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトを設定する.
    mypkd.pokemons = get_pokemon_data(number)
    # mypkdのゲッターを用いて, _pokemonsを取得する.
    pokemons = mypkd.pokemons
    # 取得した辞書からずかん番号numberのポケモンの名称を出力する.
    print(pokemons[number]["name"])
    # キーがnumberのオブジェクトを削除する.
    del mypkd.pokemons[number]
    """

    # Pokedexのインスタンスを生成する.
    mypkd = Pokedex()
    # numberはポケモンずかんにおけるポケモンの番号を表す.
    number = 10
    # mypkdのセッターを用いて, mypkdのインスタンス変数_pokemonsに,
    # バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトを設定する.
    mypkd.pokemons = get_pokemon_data(number)
    # mypkdのゲッターを用いて, _pokemonsを取得する.
    pokemons = mypkd.pokemons
    # 取得した辞書からずかん番号numberのポケモンの名称を出力する.
    print(pokemons[number]["name"])
    # キーがnumberのオブジェクトを削除する.
    del mypkd.pokemons[number]

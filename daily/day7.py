class Pokedex:
    """ポケモンの情報を格納する."""
    def __init__(self):
        self._pokemons = {}

    @property
    def pokemons(self):
        pass

    @pokemons.getter
    def pokemons(self):
        pass

    @pokemons.setter
    def pokemons(self):
        pass

    @pokemons.deleter
    def pokemons(self):
        pass


if __name__ == "__main__":
    """

    day5で定義した関数get_pokemon_dataをインポートし,
    以下に示すコードが適切に実行されるようPokedexを修正せよ.

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

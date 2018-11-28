class Pokedex:
    def __init__(self):
        self._pokemon = {}


if __name__ == "__main__":
    """

    day5で定義した関数get_pokemon_dataをインポートし,
    バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトの辞書を
    プロパティとするクラスPokedexを, 以下に示すコードを適切に実行できるよう完成せよ.

    # Pokedexのインスタンスを生成する.
    mypkd = Pokedex()

    # numberはポケモンずかんにおけるポケモンの番号を表す.
    number = 10

    # mypkdのセッターを用いて, mypkdのインスタンス変数_pokemonsに,
    # バリューにget_pokemon_dataの返り値を持ち, キーをずかん番号とするオブジェクトを設定する.
    mypkd.pokemons = get_pokemon_data(number)

    # mypkdのゲッターを用いて, _pokemonsを取得する.
    pokemons = mypkd.pokemons

    # 取得したポケモンの名称を出力する.
    print(pokemons[number]["name"])

    # キーがnumberのオブジェクトを削除する.
    del mypkd.pokemons[number]

    """

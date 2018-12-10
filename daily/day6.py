from day5 import get_pokemon_data
from collections import OrderedDict

def main():
    pokemons = OrderedDict()
    for i in range(1, 10):
        pokemon = get_pokemon_data(i)
        name = pokemon['name']
        bmi = 0.1*pokemon['weight']/((0.1*pokemon['height'])**2)
        pokemons[name] = bmi
    print('ivysaur' in pokemons)
    # (β)
    print(pokemons.get('ivysaur', None))

    # (α)
    print(pokemons.pop('ivysaur', None))
    print('ivysaur' in pokemons)

if __name__ == "__main__":
    """

    day5で作成した順序付き辞書に対して,
    存在しないキー(例えば"MissingNo.")をキーとしてバリューの取得を試みた場合,
    KeyErrorが発生する.
    day5で定義した関数get_pokemon_dataをインポートし,
    day5で作成した順序付き辞書を再び作成, これを用いて存在しないキーを指定した場合,
    KeyErrorを発生させずにデフォルトとしてNoneを返すようなバリューの取得方法について
    以下の二つの方法で示せ.

    (α)
    バリューを取得した場合, 辞書から取得したバリューのキーを削除する.

    (β)
    バリューを取得した場合でも, 辞書から取得したバリューのキーを削除しない.

    """
    main()

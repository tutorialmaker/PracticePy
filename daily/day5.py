import urllib.request
import urllib.error
import json

def get_pokemon_data(n):
    """
    関数get_pokemon_dataはAPI(https://pokeapi.co/api/v2/)を利用することにより,
    ずかん番号に対応するポケモンの情報を返す.

    引数
    n : int

    返り値
    data : Dict[Any, Any]

    """
    url = f'https://pokeapi.co/api/v2/pokemon/{n}/'
    req = urllib.request.Request(url, headers={"User-Agent": "dummy"})
    try:
        with urllib.request.urlopen(req) as f:
            data = json.loads(f.read().decode("utf-8"))
        return data
    except urllib.error.URLError:
        print("\nError: The requested URL could not be retrived. \
                        Are you connected to the Internet?\n")
def threash(th, dic):
    threashed = {}
    for k, v in dic.items():
        if v < th:
            threashed[k] = v
    threashed = dict(sorted(threashed.items(), key=lambda x:x[1], reverse=True))
    return threashed

def main():
    pokemons = {}
    print('しきい値を入力してください.')
    th = float(input())
    for i in range(1, 10):
        pokemon = get_pokemon_data(i)
        name = pokemon['forms'][0]
        name = name['name']
        bmi = 10*pokemon['weight']/((pokemon['height']*10)**2)
        pokemons[name] = bmi
    print(sorted(pokemons.items(), key=lambda x:x[1], reverse=True))
    pokemons = dict(sorted(pokemons.items(), key=lambda x:x[1], reverse=True))
    result = threash(th, pokemons)
    print(result)
if __name__ == "__main__":
    """
    関数get_pokemon_dataを用いて,
    キーにポケモンの名称, バリューにそのポケモンのBMIを持つ辞書を作成せよ.
    またBMIが高い順に並んだ順序付き辞書を作成せよ.
    また, 引数にしきい値とBMIが高い順に並んだ順序付き辞書をとり,
    しきい値を下回るBMIのポケモンのみによる順序付き辞書を返す関数を定義して実行せよ.
    ただしポケモンの名称および重量および高さは, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"および"height"に対応しており,
    "weight"および"height"の値の単位はそれぞれ0.1メートルおよび0.1キログラムである.

    """
    main()

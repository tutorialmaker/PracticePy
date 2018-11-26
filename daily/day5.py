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
    キーにポケモンの名称、バリューにそのポケモンのBMIを持つ辞書を作成せよ.
    キーにポケモンの名称, バリューにそのポケモンのBMIを持つ辞書を作成せよ.
    またBMIが高い順に並んだ順序付き辞書を作成せよ.
     また, 引数をしきい値として,
    しきい値を下回るBMIのポケモンのみによる順序付き辞書を返す関数を定義して実行せよ.
     ただしポケモンの名称および重量および高さは, 関数get_pokemon_dataの返り値において,
    バリューとしてキー"name"および"weight"および"height"に対応しており,
    "weight"および"height"の値の単位はそれぞれ0.1メートルおよび0.1キログラムである.
    """
    d = {}
    for i in range(1, 152):
        get = get_pokemon_data(i)
        name = get["name"]
        weight = get["weight"]
        height = get["height"]
        bmi = weight / (height**2)
        d[name] = bmi
    print(d)
    d_sorted = {}
    for k, v in sorted(d.items(), key=lambda x: -x[1]):
        d_sorted[k] = v
    print(d_sorted)
    def dict_sorted(n):
        dic = {}
        for t in range(1, 152):
            get = get_pokemon_data(t)
            name = get["name"]
            weight = get["weight"]
            height = get["height"]
            bmi = weight / (height**2)
            if bmi < n:
                dic[name] = bmi
                s = sorted(dic.items(), key=lambda x:-x[1])
        return dict(s)
    print(dict_sorted(3))

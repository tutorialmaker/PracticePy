"""

    (α)
    プログラムは本来正常に処理されるべきリクエストに対してもエラーを生じる.
    エラーの詳細を出力する機能を実装せよ.

    (β)
    (α)のエラーが生じないようにプログラムを修正せよ.

    (γ)
    "hippocampus"の代わりに"ヽ(*ﾟдﾟ)ノ"を返送し, これをクライアント側で適切に表示せよ.

"""

# day10ではインターネット層とトランスポート層のプロトコルについて紹介した.
# day15ではアプリケーション層のプロトコルを紹介する.
import http.server
import socketserver


# -*-*-*-*-*- インターネット層 -*-*-*-*-*-
# プロトコルはIPv4(Internet Protocol version 4)を用いる.
HOST = "127.0.0.1"
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# -*-*-*-*-*- トランスポート層 -*-*-*-*-*-
# プロトコルはTCP(Transmission Control Protocol)を用いる.
Server = socketserver.TCPServer
PORT = 8888
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# -*-*-*-*-*- アプリケーション層 -*-*-*-*-*-
# プロトコルはHTTP(Hypertext Transfer Protocol)を用いる.
Handler = http.server.BaseHTTPRequestHandler
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


class MyHandler(Handler):
    # リクエストメソッドがGETである場合, do_GETメソッドが呼び出される.
    def do_GET(self):
        try:
            # リクエストが正常に処理された場合,
            # HTTPステータスコードは200を返送すると定められている.
            self.send_response(200)
            # 返送するデータがHTML(HyperText Markup Language)ならば,
            # "Content-type"は"text/html"を指定する.
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # クライアントにデータを返送する.
            self.wfile.write("hippocampus")
        except:
            # サーバで正常に処理が行われなかった場合,
            # HTTPステータスコードは500を返送すると定められている.
            self.send_response(500)


if __name__ == "__main__":
    with Server((HOST, PORT), MyHandler) as httpd:
        httpd.serve_forever()

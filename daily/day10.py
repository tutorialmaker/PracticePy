"""

    (α)
    サーバのIPアドレスを127.0.0.1から::1に変更し,
    変更後も変更前と同様にプログラムが動作するようプログラムを修正せよ.
    ただしプログラムの修正に伴い, コメントアウトの内容も適切に変更すること.

    (β)
    サーバが, クライアントからの接続を受け付けたときに生成する
    ソケットに割り当てられたポート番号を出力するコードを実装せよ.

    (γ)
    クライアントのエフェメラルポートのポート番号を出力するよう
    クライアントにコードを実装せよ.

    (δ)
    サーバは接続を受け付けたクライアントのアドレスを取得することが可能か.
    可能ならば, クライアントのIPアドレスとポート番号を出力するコードを実装せよ.
    (出力が(γ)の結果と同じものになることが確認されればOK)
    不可能ならば, なぜ不可能であるか理由をコメントアウトで簡潔に示せ.

"""

import argparse
# プロセス間通信の通信のインターフェースとしては,
# バークレーソケット(Berkeley sockets)が普及している.
import socket


# -*-*-*-*-*- トランスポート層 -*-*-*-*-*-
# プロトコルはTCP(Transmission Control Protocol)を用いる.
PROTO = socket.IPPROTO_TCP
# TCPはストリーム型通信であるから, ストリーム型ソケットを用いる.
TYPE = socket.SOCK_STREAM

# アプリケーションごとに識別子(ポート番号)を割り当てることで,
# 複数のアプリケーションが同時に通信を行える.
# 例えばSSHというプロトコルのポート番号は22,
# HTTPというプロトコルのポート番号は80と定められている.
# 今回はアプリケーションのポート番号に12345を割り当てる.
PORT = 12345
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# -*-*-*-*-*- インターネット層 -*-*-*-*-*-
# プロトコルはIPv4(Internet Protocol version 4)を用いる.
FAMILY = socket.AF_INET
# サーバのIPアドレスは127.0.0.1とする.
HOST = "127.0.0.1"
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    # socket関数はソケットを生成する.
    with socket.socket(FAMILY, TYPE, PROTO) as s:
        # -*-*-*- サーバのソケットとして実行 -*-*-*-
        if args.mode == "server":
            # bindメソッドを実行してソケットにアドレスを割り当てる.
            s.bind((HOST, PORT))
            print(f"サーバのIPアドレス : {HOST}")
            print(f"待ち受け用のソケットに割り当てられたポート番号 : {PORT}")
            # listenメソッドを実行してソケットが接続に待機する.
            s.listen()
            while True:
                # acceptメソッドを実行して接続済みのソケットを生成する.
                conn, addr = s.accept()
                print("\n-*-*-*- 接続済みのソケットを生成 -*-*-*-")
                # TODO: 接続済みのソケットに割り当てられたポート番号を出力するコードを実装
                # TODO: クライアントのIPアドレスが入手できるか調査し, 可能ならば実装
                # TODO: クライアントのポート番号が入手できるか調査し, 可能ならば実装
                with conn:
                    # recvメソッドを実行して接続先のソケットからデータを受信する.
                    data = conn.recv(2**3)
                    if not data: break
                    print(f"受信した符号 : {data}")

                    # sendメソッドを実行して接続先のソケットにデータを送信する.
                    conn.send(data)
                    print(f"受信した符号 : {data}")
                    print(f"-*-*-*- 接続済みのソケットを破棄 -*-*-*-\n")
        # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

        # -*-*- クライアントのソケットとして実行 -*-*-
        elif args.mode == "client":
            print(f"クライアントのIPアドレス : {HOST}")
            # connectメソッドを実行して指定したアドレスが割り当てられたソケットに接続する.
            s.connect((HOST, PORT))
            string = input("送信する文字列 > ")
            # 送信するために文字列をUTF-8でエンコードする.
            code = string.encode()
            # sendメソッドを実行して接続先のソケットにデータを送信する.
            s.send(code)
            print(f"送信した符号 : {code}")
            # recvメソッドを実行してソケットからデータを受信する.
            code = s.recv(2**3)
            # 受信したデータをデコードする.
            string = code.decode(errors="replace")
            print(f"受信した符号 : {code}")
            print(f"受信した文字列 : {string}")
        # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

import itertools
from flask import (
    flash, redirect, render_template, request, url_for
)
from day18 import app
from day18.compute import (
    det, inv, rank
)


@app.route("/", methods=('GET', 'POST'))
def index():
    """POSTされた行列の行列式, 逆行列, ランクを計算して表示"""
    if request.method == 'POST':
        # TODO: HTTPメソッドがPOSTであるときの処理を実装
        # POSTされた行列の値に問題がある場合, 以下の簡易メッセージを表示し, リダイレクトする.
        #
        # flash('please enter the correct value', 'error')
        # return redirect(url_for('index'))

        return render_template('result.html')
    return render_template('input.html')

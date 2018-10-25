# PracticePy

Harder, Better, Faster, Stronger

## Rules

1. 解答者は出題者に問題を解くこと、githubのアカウント名を<A href="mailto:info@tkm.blue">info@tkm.blue</a>に送信し、出題者はその解答者用PullRequestの送信先となるブランチを切る。
  - ブランチ名は"解答者のユーザ名/answer"とする。
  - このとき、**username/answer**からブランチを切る。

2. 解答者はtutorialmakerのリポジトリをフォークして、解答用ブランチを切る。
  - 解答用ブランチ名は"解答者のユーザ名/ongoing"とする。
  - このとき、**username/ongoing**からブランチを切る。

3. 解答者は解答用ブランチで解答して、レビュー済みブランチにプルリクエストを送る。プルリクエストのタイトルは解答した問題のタイトルとする。また、プルリクエストの内容に自分の解答の方針を書く。出題者はプルリクエストのコードにレビューをする。出題者から"Approve"が出た際、解答者は[ARTICLE_SAMPLE.md](https://github.com/tutorialmaker/PracticePy/blob/master/ARTICLE_SAMPLE.md)のように、[問題のURL](https://github.com/tutorialmaker/PracticePy/blob/master/daily/)と解説を掲載した記事を[PlayGround](https://playground-i.com/articles/new/)に投稿する(解答したコード自体は書かない)。"Request Changes"が出た際、解答者はプルリクエストを修正する。

4. 解答者は書いた記事のURLを、出題者にプルリクエストのコメント等で報告する。出題者は記事の投稿を確認したのち、解答者用ブランチをレビュー済みブランチにマージする。

![diagram](https://github.com/tutorialmaker/PracticePy/blob/master/diagram.jpg)

## daily

Pythonの基本的知識、技術を身につけます。Day1から取り組むようにしてください。

## weekly

Pythonを用いた実践的なことを行います。dailyよりも難易度が比較的高くなっています。

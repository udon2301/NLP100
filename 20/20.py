# Wikipediaの記事を以下のフォーマットで書き出したファイル
# jawiki-country.json.gzがある．

# 1行に1記事の情報がJSON形式で格納される
# 各行には記事名が”title”キーに，記事本文が”text”キーの
# 辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
# ファイル全体はgzipで圧縮される

# 以下の処理を行うプログラムを作成せよ．

# Wikipedia記事のJSONファイルを読み込み，
# 「イギリス」に関する記事本文を表示せよ．問題21-29では，
# ここで抽出した記事本文に対して実行せよ．

import json
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
# print(df.info())
# print(df.head())
print(df.query('title == "イギリス"'))

# ANSWER
#     title                                               text
# 235  イギリス  {{redirect|UK}}\n{{redirect|英国|春秋時代の諸侯国|英 (春秋)...


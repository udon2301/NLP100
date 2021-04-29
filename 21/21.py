# 解説参照済み
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
import json
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
# print(type(uk))

# ''' = 正規表現中で改行を使用できる（みやすく！）
# r = raw文字列。python標準のエスケープシーケンスを文字列とみなす
# ^ = 行頭
# $ = 行末
# () = 複数の文字をグループ化
# . = 改行コード以外の任意の1文字とマッチ
# * = 直前の１文字の０回以上の繰り返しを表現
#   ex).* = 任意の一文字の0回以上の繰り返し＝ 全ての文字（列）
# re.MULTILINE = 複数行検索
# re.VERBOSE　= 正規表現中で空白やコメントを使用できる

pattern = r'''
            ^
            (
            .*
            \[
            \[
            Category:
            .*
            \]
            \]
            .*
            )
            $
            '''
answer = re.findall(pattern, str(uk), re.MULTILINE+re.VERBOSE)
print(answer)
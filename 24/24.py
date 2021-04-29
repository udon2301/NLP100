# 記事から参照されているメディアファイルをすべて抜き出せ．

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

# [[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
# .+ = 直前の一文字（任意）の一回以上の繰り返し。つまりスペース以外の全ての文字列
# .* = 直前の一文字（任意）の0回以上の繰り返し。つまりスペース以外の全ての文字列＋文字がない場合も可

# 貪欲マッチ = 検索文字列に最長になる
# 非貪欲マッチ = 検索文字列に最短になる
# <a href="http://foobarexample.com"></a><a href="http://barquuxexample.com"></a>
# Find What:<a href=".*?</a>
# Result :<a href="http://foobarexample.com"></a>
# Find What:<a href=".*</a>
# Result :<a href="http://foobarexample.com"></a><a href="http://barquuxexample.com"></a>

pattern = r'''
            # ^                 行頭一致させる必要なし
            # .*                欲しいのは[[]]の部分なのでその前の改行文字等はそもそも考慮しなくて良い
            \[\[
            (?:File|ファイル)?
            :
            # (.*?)             任意の文字の0回以上の一致＝文字列がない場合でもキャプチャされるのでNG
            (.+?)
            \|
            # (?:.*?)?          ｜以降はキャプチャしないのでいらない
            # \]\]
            # .*
            # $
            '''

answer = re.findall(pattern, uk, re.MULTILINE+re.VERBOSE)
print(answer)
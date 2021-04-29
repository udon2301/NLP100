# 解説参照済み

# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
# 貪欲マッチ・非貪欲マッチとは？？
# 参考：http://tkymtk.hatenablog.com/entry/dot-star-question-mark-2014-1

#?:...でキャプチャ対象外に指定
#()の中がキャプチャされる

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

pattern = r'''
            ^
            \[\[Category:
            (
            .*?
            )
            (?:
            \|
            .*
            )?
            \]\]
            $
            '''

answer = re.findall(pattern, str(uk), re.MULTILINE+re.VERBOSE)
print(answer)
# 未解答

# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

import re
from collections import OrderedDict
from pprint import pprint
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]


# {{基礎情報 国\n
# |略名 = イギリス\n
# |日本語国名 = グレートブリテン及び北アイルランド連合王国\n

# 中略

# |国際電話番号 = 44\n
# |注記 = <references />\n
# }}\n

# re.group()の引数は、マッチしたオブジェクトの順番
# 参考：https://note.nkmk.me/python-re-match-object-span-group/

b_pattern = r'''
                ^
                \{\{
                基礎情報.*?\n
                    (.*?)
                \}\} 
                $
                '''
basic = re.search(b_pattern, uk, re.VERBOSE+re.MULTILINE+re.DOTALL)
# print(basic.group())

pattern = r'''
            \|
                (.+?)
            \s*=\s*
                (.+?)
            (?:
            (?=\n\|)|(?=\n$)
            )
            '''
answer = OrderedDict(re.findall(pattern, basic.group(), re.VERBOSE+re.MULTILINE+re.DOTALL))
pprint(answer)
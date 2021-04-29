# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
# （参考: マークアップ早見表）．

#packagesにマークアップを削除するメソッド追加

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import clean_markup

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

b_pattern = r'''
                ^
                \{\{
                基礎情報.*?\n
                    (.*?)
                \}\} 
                $
                '''
basic = re.search(b_pattern, uk, re.VERBOSE+re.MULTILINE+re.DOTALL)

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

for key, val in answer.items():
    cval = clean_markup(val)
    answer[key] = cval

    if val != cval:
        print('changed : '+str(key)+' / '+str(answer[key]))

# pprint(answer)
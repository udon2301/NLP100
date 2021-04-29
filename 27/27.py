#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．

#packagesに内部リンクマークアップを削除するメソッド追加
# 参考見てもわかんない：https://qiita.com/FukuharaYohei/items/8c2cf248cf02127957c5

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import clean_markup,clean_ILmarkup

import re
import pandas as pd
from pprint import pprint
from collections import OrderedDict

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

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
    ccval = clean_ILmarkup(cval)
    answer[key] = ccval

    if val != cval:
        if cval != ccval:
            print('changed(mrkup&IL) : '+str(key)+' / '+str(answer[key]))
        else:
            print('changed(mrkup) : '+str(key)+' / '+str(answer[key]))
    elif val != ccval:
        print('changed(IL) : '+str(key)+' / '+str(answer[key]))
    else:
        print('nochanges : '+str(key)+' / '+str(answer[key]))
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import clean_markup,clean_ILmarkup

import re
import json
import pandas as pd
from urllib import request, parse
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

# リクエスト生成
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + parse.quote(answer['国旗画像']) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

# MediaWikiのサービスへリクエスト送信
connection = request.urlopen(request.Request(url))

# jsonとして受信
response = json.loads(connection.read().decode())

print(response['query']['pages']['-1']['imageinfo'][0]['url'])
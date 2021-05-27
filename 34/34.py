#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

import MeCab
import pandas as pd
from pprint import pprint

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import read_text

df = read_text()
print(df.info())

extracted = pd.DataFrame(columns = ['lastindex','words'])

# i = 0
# m = []

# for index, row in df.iterrows():
#     if row['pos'] ==  '名詞':
#         m += str(row['surface'])
#         i = index
#     else:
#         if m != []:
#             new = pd.DataFrame([[i,m]])
#             pd.concat([extracted, new])
#             m = []
#         else:
#             continue

# print(extracted.head(5))

#めちゃめちゃ実行に時間かかる

df = df[df['pos'] == '名詞']
nouns = []
for index in df['surface'].index:
    print(index)
    nouns.append(df['surface'][index])

    # ひとつ先のインデックスがない場合は名詞連接の終端
    if (index + 1) not in df.index:

        # 複数(連接)の場合
        if len(nouns) > 1:
            # print(len(nouns), '\t', index, '\t', ''.join(nouns))
            continue
        nouns = []
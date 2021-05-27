#2つの名詞が「の」で連結されている名詞句を抽出せよ

import MeCab
import pandas as pd
from pprint import pprint

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import read_text

df = read_text()
print(df.info())
# print(df[10-1]['pos'])

extracted = []

# i=0
# pdのスライスは一行以上！

for index, row in df.iterrows():
    if row['surface'] == 'の' \
    and df.at[index-1,'pos'] == '名詞' \
    and df.at[index+1,'pos'] == '名詞':
        # if i < 150:
        #     print(index)
        #     print(df.loc[index-1])
        #     print(df.loc[index])
        #     print(df.loc[index+1])
        extracted.append(df.loc[index-1:index+1,:])
    # i += 1

print(extracted[:3])
print(type(extracted[0]))
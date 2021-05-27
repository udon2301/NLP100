# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import MeCab
import pandas as pd
from pprint import pprint

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import read_text

df = read_text()
df = df[(df['pos1'] != '空白') & (df['surface'] != 'EOS') & (df['pos'] != '記号') & (df['surface'] != '記号')]
print(df.info())

vc = df[~df['pos'].str.startswith('助')]['surface'].value_counts(ascending = False)[:50]
print(vc)


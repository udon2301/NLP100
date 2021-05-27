# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import MeCab
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import read_text

df = read_text()
df = df[(df['pos1'] != '空白') & (df['surface'] != 'EOS') & (df['pos'] != '記号') & (df['surface'] != '記号')]
print(df.info())
print(df.head())

vc = df[~df['pos'].str.startswith('助')]['surface'].value_counts(ascending = False)[:10]
print(type(vc))
print(vc.head())
vc.plot.bar()
plt.show()
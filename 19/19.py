# 各行の1列目の文字列の出現頻度を求め，
# その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

import pandas as pd

df = pd.read_table('./popular-names.txt', header=None)
df.columns = ['name', 'sex', 'nop', 'year']

print(df['name'].value_counts())

# ANSWER
# James      118
# William    111
# John       108
# Robert     108
# Mary        92
#           ... 
# Lori         1
# Tracy        1
# Crystal      1
# Carolyn      1
# Laura        1
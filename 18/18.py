# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ
# （この問題はコマンドで実行した時の結果と合わなくてもよい）

import pandas as pd

df = pd.read_table('./popular-names.txt', header=None)
df.columns = ['name', 'sex', 'nop', 'year']
df_s = df.sort_values('nop')

print(df_s[0:5])

# ANSWER
#       name sex   nop  year
# 9    Sarah   F  1288  1880
# 29   Alice   F  1308  1881
# 8   Bertha   F  1320  1880
# 28  Bertha   F  1324  1881
# 27   Annie   F  1326  1881
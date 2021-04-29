# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

import pandas as pd

df_1 = pd.read_table('./13/col1.txt', header=None)
df_2 = pd.read_table('./13/col2.txt', header=None)

df_merged = pd.concat([df_1,df_2],axis=1)

print(df_merged.shape)
print(df_merged[0:5])

# ANSWER
# (2780, 2)
#            0  0
# 0       Mary  F
# 1       Anna  F
# 2       Emma  F
# 3  Elizabeth  F
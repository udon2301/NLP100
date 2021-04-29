# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

import pandas as pd

df = pd.read_table('./popular-names.txt', header=None)
df.columns = ['name', 'sex', 'nop', 'year']

df.to_csv('./12/col1.txt', sep='\t', header=False, index=False, columns = ['name'], mode='w')
df.to_csv('./12/col2.txt', sep='\t', header=False, index=False, columns = ['sex'], mode='w')
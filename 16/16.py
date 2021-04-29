# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='分割数を指定', default = 2)
args = parser.parse_args()

df = pd.read_table('./popular-names.txt', header=None)
stp = len(df) // int(args.n)
dfs = [df.loc[i:i+stp-1, :] for i in range(0, len(df), stp)]

print(dfs[0][0:5])
print(dfs[0].shape)

# ANSWER
# (project_nippo) udn-no-macbook-pro:NLP100 ishiiasuka$ python ./16/16.py -n 10
#         name sex   nop  year
# 0       Mary   F  7065  1880
# 1       Anna   F  2604  1880
# 2       Emma   F  2003  1880
# 3  Elizabeth   F  1939  1880
# 4     Minnie   F  1746  1880
# (278, 4)
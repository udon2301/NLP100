# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='取り出す末行数を指定', default = 1)
args = parser.parse_args()

df = pd.read_table('./popular-names.txt', header=None)
print(df[len(df) - int(args.n):len(df)])

# ANSWER
# (project_nippo) udn-no-macbook-pro:NLP100 ishiiasuka$ python ./15/15.py -n 3
#           0  1      2     3
# 2777  Lucas  M  12585  2018
# 2778  Mason  M  12435  2018
# 2779  Logan  M  12352  2018
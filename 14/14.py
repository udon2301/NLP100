# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='取り出す行数を指定', default = 1)
args = parser.parse_args()

df = pd.read_table('./popular-names.txt', header=None)
print(df[0:int(args.n)])


# ANSWER
# (project_nippo) udn-no-macbook-pro:NLP100 ishiiasuka$ python ./14/14.py -n 3
#       0  1     2     3
# 0  Mary  F  7065  1880
# 1  Anna  F  2604  1880
# 2  Emma  F  2003  1880
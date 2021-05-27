#動詞の表層形をすべて抽出せよ．

import MeCab
import pandas as pd
from pprint import pprint

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import read_text

df = read_text()
print(df.info())
# print(df.head())

extracted = df[df['pos'] == '動詞']['surface']

print(extracted.head())
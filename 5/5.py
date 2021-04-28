# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
# 参考：https://mojitoba.com/2019/09/23/what-is-ngram/

#../package.pyに関数を作成する

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import word_ngram, chr_ngram

seq = 'I am an NLPer.'
print(word_ngram(2,seq))
print(chr_ngram(2,seq))

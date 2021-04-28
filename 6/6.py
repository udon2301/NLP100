# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
# 参考：https://qiita.com/Tocyuki/items/0bc783daab382ef7a0ec

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import chr_ngram

str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(chr_ngram(2, str1))
Y = set(chr_ngram(2, str2))

union = X | Y
intersection = X & Y
sym_dif = X ^ Y

print('union'+str(union))
print('intersection'+str(intersection))
print('symmetric difference'+str(sym_dif))

# ANSWER
# union{'di', 'ap', 'ra', 'gr', 'ph', 'ad', 'ag', 'ar', 'pa', 'is', 'se'}
# intersection{'ra', 'pa', 'ar', 'ap'}
# symmetric difference{'di', 'gr', 'ph', 'ad', 'ag', 'is', 'se'}
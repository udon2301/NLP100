# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that 
# I could actually understand what I was reading : 
# the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
# test

import random

seq = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
splited = seq.split(' ')

shuffled = []

for raw in splited:
    print(str(len(raw))+':'+str(raw))

    if len(raw) >= 5:
        shf = ''.join(random.sample(raw[1:len(raw)-1],len(raw)-2))
        new = str(raw[0]) + str(shf) + str(raw[len(raw)-1])
        shuffled += [new]
    else:
        shuffled += [raw]

print(' '.join(shuffled))

# ANSWER
# I cunld’ot bleieve that I culod acautlly uesnnatdrd what I was rneadig : the pneeahmnol poewr of the hamun mind .
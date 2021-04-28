#“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
#という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
#それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')

from package import alpha_word
answer = dict()

string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
numst = [1, 5, 6, 7, 8, 9, 15, 16, 19]

string = alpha_word(string)

for i, word in enumerate(string):
    if i+1 in numst:
        k = str(word[0])
    else:
        k = str(word[0]+word[1])
    answer[k] = i+1

print(answer)
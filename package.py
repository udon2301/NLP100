# 返り値：アルファベットのみの単語リスト
def alpha_word(string):
    alphabet = []
    splited = string.split(' ')

    for raw in splited:
        word = ''
        for chr in raw:
            if chr.isalpha():
                word += chr
        alphabet.append(word)
    
    return alphabet

#返り値：アルファベットのみで空白を削除した1文
def alpha_seq(string):
    # string = string.replace(' ','')
    seq = ''.join([chr for chr in string if chr.isalpha()])

    return seq
    
#返り値：単語n-gram
def word_ngram(num, seq):
    wn_gram = []

    string = alpha_word(seq)
    for i in range(len(string)-num+1):
        # print(str(i)+' : to append : '+str(string[i:i+num]))
        wn_gram += [string[i:i+num]]
    
    return wn_gram

#返り値：文字n-gram
def chr_ngram(num, seq):
    cn_gram = []

    string = alpha_seq(seq)
    for i in range(len(string)-num+1):
        cn_gram += [string[i:i+num]]

    return cn_gram


def cipher(seq):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in seq])

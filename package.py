import re

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

#返り値：暗号（9）
def cipher(seq):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in seq])

# 協調マークアップの削除
def clean_markup(seq):
    pattern = r'''
                (\'{2,5})
                    (.*?)
                (\1)
                '''
    cleaned = re.sub(pattern, r'\2', seq, flags = re.MULTILINE+re.VERBOSE)
    
    return cleaned

# 内部リンクマークアップの削除 #27
# ここが理解できない！！
def clean_ILmarkup(seq):
    pattern = r'''
                \[\[             # '[['(マークアップ開始)
                (?:              # キャプチャ対象外のグループ開始
                    [^|]*?       # '|'以外の文字0文字以上、非貪欲(ここがわからん！！！)
                    \|           # '|'
                )??              # グループ終了、このグループが0か1出現、非貪欲
                (                # グループ開始、キャプチャ対象
                    (?!Category:)  # 否定の先読(含んだ場合は対象外としている)
                    ([^|]*?)    # '|'以外が0文字以上、非貪欲(表示対象の文字列)
                )
                \]\]        # ']]'（マークアップ終了）
                '''
    cleaned = re.sub(pattern, r'\1', seq, flags = re.MULTILINE+re.VERBOSE)
    
    return cleaned
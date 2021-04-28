#“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
splited = string.split(' ')
alphabet = []

for raw in splited:
    word = ''
    for chr in raw:
        if chr.isalpha():
            word += chr
    alphabet.append(word)

py = [len(w) for w in alphabet]

print(py)
#文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

string = 'stressed'
reversedstring = []

for i in range(len(string)):
    reversedstring.append(string[len(string)-i-1])
reversedstring =''.join(reversedstring)
print(reversedstring)
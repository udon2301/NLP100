#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

pato = 'パトカー'
taxi = 'タクシー'
newstring = ''

for i in range(len(pato)):
    newstring += pato[i] + taxi[i]
print(newstring)
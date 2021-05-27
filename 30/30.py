'''
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

import re
import MeCab
import pandas as pd
from pprint import pprint

# answer = list()

# with open('/Users/ishiiasuka/Documents/GitHub/NLP100/neko.txt.mecab', 'r') as raw:
#     raw = raw.read()
#     print(type(raw))

# df = pd.read_table('/Users/ishiiasuka/Documents/GitHub/NLP100/neko.txt.mecab', 
#                     names = ('表層形','読み','発音','原型','品詞','NaN1','NaN2','NaN3'))
# print(df.head())

'''
一	イチ	イチ	一	名詞-数詞			2
　			　	空白			
吾輩	ワガハイ	ワガハイ	我が輩	代名詞			0
は	ワ	ハ	は	助詞-係助詞			
猫	ネコ	ネコ	猫	名詞-普通名詞-一般			1
で	デ	ダ	だ	助動詞	助動詞-ダ	連用形-一般	
ある	アル	アル	有る	動詞-非自立可能	五段-ラ行	終止形-一般	1
。			。	補助記号-句点			
名前	ナマエ	ナマエ	名前	名詞-普通名詞-一般			0
は	ワ	ハ	は	助詞-係助詞			
まだ	マダ	マダ	未だ	副詞			1
無い	ナイ   	ナイ	無い	形容詞-非自立可能	形容詞	終止形-一般	1
。			。	補助記号-句点
'''

pattern = r'''
            ^
                (.+?)
            \-
                (.+?)
            \-
            .*
            $
            '''

# string = dict()
# new_word = dict()

# for index, row in df.iterrows():

#     if row['原型'] == '空白':
#         #dict(S)を閉じる
#         answer += string
#         string = dict()

#     #品詞を'-'をキーに分割してpos,pos1に分割
#     p = re.search(pattern, str(row['品詞']), re.VERBOSE+re.MULTILINE)
#     print(p)

#     w = {'surface' : str(row['表層形']),
#             'base' : str(row['原型']),
#             'pos'  : str(p[0]),
#             'pos1' : str(p[1]),
#             'id'   : index}
    
#     new_word = dict(w = str(row['表層形']))
#     string = {**string, **new_word}




#neko.txtを形態素解析して、結果を保存する
def moranalysis(path_to_txt, out_file_name):
    f = open(path_to_txt, 'r')
    data = f.read()

    print(type(data))

    m = MeCab.Tagger('')
    text = m.parse(data)

    with open('/Users/ishiiasuka/Documents/GitHub/NLP100/' + out_file_name, 'w') as p:
        p.write(text)
# moranalysis('/Users/ishiiasuka/Documents/GitHub/NLP100/neko.txt','neko.txt.mecab')


def read_text():
    # 0:表層形(surface)
    # 1:品詞(pos)
    # 2:品詞細分類1(pos1)
    # 7:基本形(base)
    df = pd.read_table('/Users/ishiiasuka/Documents/GitHub/NLP100/neko2.txt.mecab', sep='\t|,', header=None, 
                       usecols=[0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], 
                       skiprows=4, skipfooter=1 ,engine='python')
    # 本当は空白はpos1だが、ずれてしまっている
    return df[df['pos'] != '空白']

df2 = read_text()
print(df2.info())

target = []
morphemes = []

for i, row in df2.iterrows():
    if row['surface'] == 'EOS' \
     and len(target) != 0:
        morphemes.append(df2.loc[target].to_dict(orient='records'))
        target = []
    else:
        target.append(i)

print(len(morphemes))
pprint(morphemes[:5])
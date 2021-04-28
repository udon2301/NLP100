# 解答参照済み

# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

import sys
sys.path.append('/Users/ishiiasuka/Documents/GitHub/NLP100')
from package import cipher

seq = 'Surf on Entropy'

encrypted = cipher(seq)
decrypted = cipher(encrypted)

print('暗号 : ' + encrypted)
print('復号 : ' + decrypted)
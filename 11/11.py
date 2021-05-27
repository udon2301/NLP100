# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open('./popular-names.txt') as d:
    data =d.read().replace('\t', ' ')
# popular-names.txtは，アメリカで生まれた赤ちゃんの
# 「名前」「性別」「人数」「年」をタブ区切り形式で格納したファイルである．
# 以下の処理を行うプログラムを作成し，popular-names.txtを入力ファイルとして
# 実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，
# プログラムの実行結果を確認せよ

# 行数をカウントせよ．確認にはwcコマンドを用いよ．

with open('./popular-names.txt') as df:
    l = df.readlines()

print(len(l))

# ANSWER
# 2780
# (base) udn-no-macbook-pro:NLP100 ishiiasuka$ wc popular-names.txt
#     2780   11120   55026 popular-names.txt

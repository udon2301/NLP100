# 解説参照済み

# 記事中に含まれるセクション名とそのレベル
# （例えば”== セクション名 ==”なら1）を表示せよ

# 参考：https://www.javadrive.jp/python/string/index24.html


import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', compression='infer', lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]


pattern = r'''
            ^
            (={2,})
            \s*
            (.+?)
            \s*
            \1
            $
            '''

sections = re.findall(pattern, uk, re.MULTILINE+re.VERBOSE)

for sec in sections:
    level = len(sec[0]) - 1
    print('{indent}{sect}({level})'.format(indent='\t'*(level-1), sect=sec[1], level=level))
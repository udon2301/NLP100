import json 

filename = 'jawiki-country.json'
with open(filename, mode='r') as f:
  for line in f:
    line = json.loads(line)
    if line['title'] == 'イギリス':
      text_uk = line['text']
      break

# 確認
print(text_uk)

import re

pattern = r'^(.*\[\[Category:.*\]\].*)$'
result = '\n'.join(re.findall(pattern, text_uk, re.MULTILINE))
print(result)
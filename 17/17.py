# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはcut, sort, uniqコマンドを用いよ．

import pandas as pd

df = pd.read_table('./popular-names.txt', header=None)
df.columns = ['name', 'sex', 'nop', 'year']
u = df['name'].unique()
print(u)

# ANSWER
# ['Mary' 'Anna' 'Emma' 'Elizabeth' 'Minnie' 'Margaret' 'Ida' 'Alice'
#  'Bertha' 'Sarah' 'John' 'William' 'James' 'Charles' 'George' 'Frank'
#  'Joseph' 'Thomas' 'Henry' 'Robert' 'Annie' 'Edward' 'Clara' 'Florence'
#  'Ethel' 'Bessie' 'Harry' 'Helen' 'Ruth' 'Marie' 'Lillian' 'Mildred'
#  'Dorothy' 'Frances' 'Walter' 'Evelyn' 'Virginia' 'Richard' 'Betty'
#  'Donald' 'Doris' 'Shirley' 'Barbara' 'Patricia' 'Joan' 'Nancy' 'Carol'
#  'David' 'Ronald' 'Judith' 'Linda' 'Sandra' 'Carolyn' 'Sharon' 'Michael'
#  'Susan' 'Donna' 'Larry' 'Kathleen' 'Deborah' 'Gary' 'Karen' 'Debra'
#  'Pamela' 'Cynthia' 'Mark' 'Steven' 'Lisa' 'Jeffrey' 'Lori' 'Kimberly'
#  'Tammy' 'Angela' 'Michelle' 'Jennifer' 'Melissa' 'Christopher' 'Brian'
#  'Amy' 'Laura' 'Tracy' 'Julie' 'Jason' 'Scott' 'Stephanie' 'Heather'
#  'Nicole' 'Matthew' 'Rebecca' 'Jessica' 'Amanda' 'Daniel' 'Kelly' 'Joshua'
#  'Crystal' 'Ashley' 'Megan' 'Brittany' 'Andrew' 'Justin' 'Samantha'
#  'Lauren' 'Emily' 'Brandon' 'Tyler' 'Taylor' 'Nicholas' 'Jacob' 'Hannah'
#  'Austin' 'Alexis' 'Rachel' 'Madison' 'Abigail' 'Olivia' 'Ethan' 'Anthony'
#  'Isabella' 'Ava' 'Sophia' 'Chloe' 'Alexander' 'Mia' 'Jayden' 'Noah'
#  'Aiden' 'Mason' 'Liam' 'Charlotte' 'Harper' 'Benjamin' 'Elijah' 'Amelia'
#  'Logan' 'Oliver' 'Lucas']
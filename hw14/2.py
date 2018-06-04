from collections import Counter
import re

l = []


with open('txt.txt',encoding='utf-8') as f:
    text = f.read()
    text = re.split(r'[.!?]', text)
    for x in text:
        txt = re.sub(r'[^а-яА-ЯёЁ ]','',x)
        l.append(txt)

for x in l:
    xx = x.split(' ')
    c = Counter(xx)
    keys = c.keys()
    values = c.values()
    d = dict(zip(keys, values))
    for k, v in d.items():
        if v > 1:
            print('{} {} {}'.format(k,'    ', v))
    

#   не смогла избавиться от "", из-за этого есть такие ответы:
#   ''  2
    
        
        
         
    
    

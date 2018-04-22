import re
from collections import Counter


with open ('mystem.xml', encoding='utf-8') as f:
    text = f.read()

    gr = re.findall(r'gr="(.*?)"',text)
    c = Counter(gr)
    keys = c.keys()
    values = c.values()
    d = dict(zip(keys, values))
        
        
with open('text2.txt','w', encoding='utf-8') as f:
    d = str(d)
    d = d.replace(", '","\n'")
    f.write(d)
    
    
        
    

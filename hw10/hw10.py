
import re

with open('ht.html',encoding='utf-8') as f:
    ht = f.read()
    f = re.findall('<a rel="nofollow" class="external text" href="(.*?)">(.*?)</a>',ht)
    t = f[0]
    s = t[1]
    
    print('трёхбуквенный код:', s)



import re

with open('mystem.xml', encoding='utf-8') as f:
    text = f.read()
    find = re.findall(r'<w>.*?</w>',text)
    n = len(find)*4
    print(n)

    with open ('text.txt', 'w', encoding = 'utf-8') as t:
        n = str(n)
        t.write(n)
    

#<w> 2 строки </w> == 1 тег <w>.*?</w> это 4 строки
    

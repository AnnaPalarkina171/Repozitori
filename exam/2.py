import os
import re

def list_lex():
    l = []
    name = os.getcwd()
    files = os.listdir(name)
    for x in files:
        if '.html' in x:
            with open(x,'r',encoding="utf-8") as f:
                txt = f.read()
                lex = re.findall(r'lex="([А-ЯЁа-яё]+)"',txt)
                for x in lex:
                    if x.isupper():
                        break
                    else:
                        if x[0].isupper():
                            l.append(x)
    return l

def freq(l):
    freq = {}
    for w in l:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

def write(freq):                
    with open('table.csv','w',encoding='utf-8') as t:
        for k,v in freq.items():
                t.write('{}{}{}{}'.format(k,'\t',v,'\n'))
    
def main():
        print(write(freq(list_lex())))
main()

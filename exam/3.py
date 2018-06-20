#Найдите в текстах все биграммы вида «число (NUM) + существительное в родит. падеже (gen)».
#Создайте csv-таблицу (используйте в качестве разделителя «;» и кодировку «cp1251») со следующими полями:
#«doc_id»; найденная биграмма; «topic» (см. тег meta). Повторяющиеся биграммы убирать не надо.
import os
import re

name = os.getcwd()
files = os.listdir(name)
for x in files:
    if '.html' in x:
        with open(x,'r',encoding="utf-8") as f:
            with open('table2.csv','a',encoding='cp1251') as t:
                txt = f.read()
                topic = re.findall(r'<meta content="(.*?)" name="topic">',txt)
                doc_id = re.findall(r'<meta content="(.*?)" name="docid">',txt)
                phrases = re.split(r'<se>',txt)
                phrases = phrases[1:]
                for phrase in phrases:
                    words = phrase.split('\n')
                    num_w = enumerate(words)
                    for num,w in num_w:
                        numbers = re.findall(r'gr="NUM.*?"',w)
                        if numbers != []:
                            d_n ={}
                            num_n = num
                            no = re.findall(r'</ana>(.*?)</w>',w)
                            for x in no:
                                d_n[x] = num_n
                        s = re.findall(r'gr="S,.*?,gen"',w)
                        if s != []:
                            d_s = {}
                            num_s = num
                            s_lex = re.findall(r'</ana>(.*?)</w>',w)
                            for x in s_lex:
                                d_s[x] = num_s
                                if num_s == num_n +1:
                                    t.write('{}{}{}{}'.format(no,';',s_lex,'\n'))
                                    print('{}{}{}'.format(no,';',s_lex))

                            
            

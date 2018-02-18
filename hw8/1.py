import random
with open('text.txt',encoding='utf-8')as t:
    text = t.read()
    text = text.splitlines()
    print('Вставьте вместо многоточия существительное')
    d = {}
    l=[]
    s = []
    i = 1

with open('table - table.csv', encoding = 'utf-8') as f:
    for line in f:
        w = line.split(',')
        value = w[1:]
        value[len(value)-1] = value[len(value)-1].replace('\n','')
        value[len(value)-1] = value[len(value)-1].replace('"','')
        w[0] = w[0].replace('"','')
        key = w[0]
        l.append(key)
        keys = d.setdefault(key,value)
        k = list(d.keys())
        r = random.choice(k)
    if r in d.keys():
        hint = d[r]

while s == []:
        if len(hint) == i:
                print('К сожалению, Вы использовали все попытки')
                break
        print(hint[i])
        n = input('Слово: ')
        if r == n:
            print(random.choice(text))
            s.append(r)
        if r != n:
            print('Увы, нет. Вот Вам ещё одна подсказка: ')
            i += 1
        
        
            
    
   
        


    
      

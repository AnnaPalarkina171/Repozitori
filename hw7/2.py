def input_n():
    n = input('Введите название файла: ')
    return n

def open_n(n):
    with open (n, encoding='utf-8') as f:
        t = f.read()
        text = t.split()
    return text
        
def words(text):
    l = []
    for i in text:
        if i.startswith('un'):
            l.append(i)
    print('Количество слов, начинающихся на un: ', len(l))
    return l


def percentage(l):
    m = []
    k = int(input('Введите число: '))
    for j in l:
        if len(j) >= k:
            m.append(j)
            num = (len(m) * 100)/ len(l)
            number = round(num)
    return number

def main():
    print('Процент слов, имеющих длину больше этого числа: ', percentage(words(open_n(input_n()))))
          
main()
    
    
    

        
    

        



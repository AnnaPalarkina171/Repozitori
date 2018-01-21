import random
#эта программа генерирует стихотворение танка

def adj1():
    with open('one.txt','r', encoding='utf-8') as f:
        adjectives = f.readlines()
    adjective = random.choice(adjectives)
#функция возвращает случайное прилагателное, состоящее из 2х слогов
#первое слово в первой строке
    return adjective.replace('\n','')

def noun1():
    with open('two.txt','r', encoding='utf-8') as f:
        nouns = f.readlines()
    noun = random.choice(nouns)
#функция возвращает случайное существительное(агенс), состоящее из 3з слогов
#второе слово в первой строке
    return noun.replace('\n','')


def verb1():
    with open('three.txt','r', encoding='utf-8') as f:
        verbs = f.readlines()
    verb = random.choice(verbs)
#ункция возвращает случайный глагол, состоящий из 2х слогов
#первое слово во второй строке
    return verb.replace('\n','')

def adj2():
    with open('four.txt','r', encoding='utf-8') as f:
        adjectives = f.readlines()
    adjective = random.choice(adjectives)
#функция возвращает случайное прилагателное, состоящее из 2х слогов
#второе слово во второй строке
    return adjective.replace('\n','')
 
def noun2():
        with open('five.txt','r', encoding='utf-8') as f:
            nouns = f.readlines()
        noun = random.choice(nouns)
#функция возвращает случайное существительное(пациенс), состоящее из 3з слогов
#третье слово во второй строке
        return noun.replace('\n','')
    
def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)
#функция возвращает случайный знак препинания
#конец 2й строки


def participe1():
    with open('six.txt','r', encoding='utf-8') as f:
        participels = f.readlines()
    participel = random.choice(participels)  
#функция возвращает случайное причастие, состоящее из 3з слогов
#первое слово в третьей строке
    return participel.replace('\n','')

def noun3():
    with open('seven.txt','r', encoding='utf-8') as f:
        nouns = f.readlines()
        noun = random.choice(nouns)
#функция возвращает случайное существительное, состоящее из 3х слогов
#второе слово в третьей строке
    return noun.replace('\n','')

def verb2():
    with open('eight.txt','r', encoding='utf-8') as f:
        verbs = f.readlines()
        verb = random.choice(verbs)
#функция возвращает случайный глагол, состоящий из 2х слогов
#первое слово в четвертой строке
    return verb.replace('\n','')

def verb3():
    with open('nine.txt','r', encoding='utf-8') as f:
        verbs = f.readlines()
    verb = random.choice(verbs)
#функция возвращает случайный глагол, состоящий из 3х слогов
#второе слово в четвертой строке
    return verb.replace('\n','')

def interjections():
    with open('ten.txt','r', encoding='utf-8') as f:
        interjections =  f.readlines()
    interjector = random.choice(interjections)
#функция возвращает случайное междометие из 1го слога
#третье слово в четвертой строке
    return interjector.replace('\n','')


def adj3():
    with open('eleven.txt','r', encoding='utf-8') as f:
        adjs = f.readlines()
    adj = random.choice(adjs)
#функция возвращает случайное прилагательное из 3х слога
#второе слово в пятой строке
    return adj.replace('\n','')

def noun4():
    with open('twelve.txt','r', encoding='utf-8') as f:
        nouns = f.readlines()
    noun = random.choice(nouns)
#функция возвращает случайное существительное из 2х слогов
#третье слово в пятой строке
    return noun.replace('\n','')



def vers1():
    return adj1() + noun1()
print(vers1())

def vers2():
    return verb1() + ' ' + adj2() +  ' ' + noun2() + punctuation()
print(vers2())

def vers3():
    return participe1() + ' ' + noun3() + ','
print(vers3())

def vers4():
    return verb2() + '. ' + verb3() + ' ' + interjections() + ' ' + 'ты'
print(vers4())

def vers5():
    return 'Этот' + ' ' + adj3() + ' ' + noun4() + punctuation()
print(vers5())
    










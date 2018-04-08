import re

def file_from():
    with open('birds.html', encoding='utf-8') as f:
        text = f.read()
    return text

def sub(text):
    #тут не знаю, как по-другому сделать(чтобы птицЕй заменял на рыбОй)
    text = re.sub('птицей','рыбой',text)
    text = re.sub('Птицей','Рыбой',text)
    
    text = re.sub(
        r'(\b|\W)птиц([аыеу]?[м,й,х]?[и]?)(\W|\b)',
        r'\1рыб\2\3',
        text)
    text = re.sub(
        r'(\b|\W)Птиц([аыеу]?[м,й,ми,х]?[и]?)(\W|\b)',
        r'\1Рыб\2\3',
        text)
    return text

    
    
def file_in(text):
    with open('fish.txt','w',encoding='utf-8') as f:
        end = f.write(text)
    return end

def main(): file_in(sub(file_from()))

main()

        





import re

name= input('Введите название файла: ') 

def file(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
        return text
        
def match(text):
        text = re.sub(r'[^а-яА-Я]',' ',text)
        l = []
        match = re.findall(r'\bси[жд][уияе][ш,т,м,те,ть,л,щ,вш,в,ч]*[е,ий,а,и,о,ая,ее,ь,ей]*[го,му,м]*\b', text, flags = re.IGNORECASE)
        for x in match:
            if x not in l:
                l.append(x)
        l = str(l)[1:-1]
        return l         
        
def main():
    print('Все формы слова "Сидеть": ', match(file(name)))
    

main()


#сижу сидел сидела сидишь сиди сидит сидело сидим сидели сидите сидят сидячий сидевший сидя сидев сидевши сидящего сидящей сидящему сидящую сидящим сидящем сидевшая сидевшего сидевшей сидевшему сидевшую сидевшим сидевшей сидевшем сидевшей  

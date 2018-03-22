import re

def file():
    with open('dovlatov1.txt', encoding='utf-8') as f:
        text = f.read()
        return text
        
def match(text):

        match = re.findall(r'\bси[жд][уияе][ш,т,м,те,ть,л,щ,вш,в,ч]*[ий,а,и,о,ая,ее,ь]*\b', text, flags = re.IGNORECASE)
        l = ', '.join(match)
        return l
        
        
        
def main():
    print(match(file()))
    
main()

#\bси[жд]*[уияе]*[ш,т,м,те,ть,л,щ,вш,в,ч]*[ий,а,и,о,ая,ее,ь]*

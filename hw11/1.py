import re

with open('birds.html', encoding='utf-8') as f:
    text = f.read()
    text = re.sub('птица','рыба',text)
    text = re.sub('птицы','рыбы',text)
    text = re.sub('птиц','рыб',text)
    text = re.sub('птице','рыбе',text)
    text = re.sub('птицам','рыбам',text)
    text = re.sub('птицу','рыбу',text)
    text = re.sub('птицей','рыбой',text)
    text = re.sub('птицами','рыбами',text)
    text = re.sub('птицах','рыбах',text)

    text = re.sub('Птица','Рыба',text)
    text = re.sub('Птицы','Рыбы',text)
    text = re.sub('Птиц','Рыб',text)
    text = re.sub('Птице','Рыбе',text)
    text = re.sub('Птицам','Рыбам',text)
    text = re.sub('Птицу','Рыбу',text)
    text = re.sub('Птицей','Рыбой',text)
    text = re.sub('Птицами','Рыбами',text)
    text = re.sub('Птицах','Рыбах',text)

    with open('fish.txt','w',encoding='utf-8') as f:
        f.write(text)


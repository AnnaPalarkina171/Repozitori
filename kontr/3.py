with open('Extinct_languages.tsv', encoding='utf-8') as f:
    lines = f.readlines()
    lang = input('Введите название языка: ')
    all_langs = []
    while lang != '':
        all_langs.append(lang)
        lang = input('Введите название языка: ')
    parts = []
    for line in lines:
        lineline = line.strip()
        parts.append(lineline.split('\t'))
    for lang in all_langs:
        arg = True
    for row in parts:
        if lang == row[0]:
            print('Название языка:',lang,'Число говорящих: ', row[1], 'Статус языка: ', row[2])
            arg = False
    if arg == True:
        print('Языка списке нет')

    
    
 

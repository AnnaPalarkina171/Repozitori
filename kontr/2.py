a = []
with open ('Extinct_languages.tsv', encoding='utf-8') as f:
    for line in f:
        row = line.split('\t')
        if row[2] == 'Critically endangered\n':
            a.append(row[2])
            
            
print(len(a))
            

n = input('Enter sth: ')
alf = 'аеёиоуэюя'
for i in n:
    if i in alf:
        i = i + 'с' + i
        print(i, end='')
    else:
        print(i, end='')
    
    
    











  

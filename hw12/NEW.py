import os
import re

def cwd():
    name = os.getcwd()
    files = os.listdir(name)
    if files == []:
        return 'Нет файлов'
    else:
        return files

def all_dirs(files):
    d = []
    for x in files:
        if os.path.isdir(x):
            d.append(x)
    if d == []:
        return 'нет папок'
    else:
        return d
    


def needed_dirs(d):
    l = []
    for i in d:
        if re.findall(r'[а-яёА-ЯЁ]', i):
            if re.findall(r'[a-zA-Z]', i):
                l.append(i)
    need_dirs_num = len(l)
    if need_dirs_num == 0:
        return 'нет таких папок'
    else:
        return need_dirs_num 
        
    



def main():
    print('Все файлы: ',cwd())
    print('Все папки:', all_dirs(cwd()))
    print('Количество папок, названия которых содержат и кириллические, и латинские символы: ',needed_dirs(all_dirs(cwd())))
    
main()

    
        




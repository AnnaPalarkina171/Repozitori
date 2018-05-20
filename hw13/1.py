import os
l = []

def cwd():
    main_name = os.getcwd()
    folders = os.listdir(main_name)
    if folders == []:
        return 'No folders' 
    else:
        return main_name

def lens(main_name):
    l = []
    for name, folders, files in os.walk(main_name):
        len_f = len(files)
        k = name, len_f
        l.append(k)
    return l
    
def big(l):
    val = []
    needed_folders = []
    for x in l:
        v = x[1]
        val.append(v)
    m = max(val)
    for x in l:
        if x[1] == m:
            needed_folders.append(x[0])     
    return needed_folders
          

def main():
    print('Папка, в которой больше всего файлов',big(lens(cwd())))
main()
    


    


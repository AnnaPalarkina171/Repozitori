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
    for x in l:
        v = x[1]
        val.append(v)
    m = max(val)
    for x in l:
        if x[1] == m:
            return x[0]
          

def main():
    print(big(lens(cwd())))
main()
    
    



    


#for name, folders, files in os.walk(main_name):
    #len_f = len(files)
    #print('In %s: %s files' % (name, len_f))
    #l.append(len_f)


    
#if len_f == max(l):
    #print(name)

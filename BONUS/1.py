n =input('Enter sth:')
l = []
a = []
l.append(n)
while n != '':
    n = input('Enter sth: ')
    l.append(n)
l.pop() 
for i in l:
    a.append(int(i))
print('Max: ', max(a))
print('Min: ', min(a))
print('Sum: ', sum(a))
average = sum(a)/len(a)
print('Average: ', average)
    
    

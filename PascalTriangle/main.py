print('Pascal Triangle')
num = int(input('Enter a number == > '))
print()
listed = []  
for i in range(num):  
  listed.append([])  
  listed[i].append(1)  
  for j in range(1, i):  
    listed[i].append(listed[i - 1][j - 1] + listed[i - 1][j])  
  if(num != 0):  
    listed[i].append(1) 
listed[0].remove(1)
for i in range(num):
    text = (num-i) * ' ' 
    for j in range(0, i+1):
        text +=  str(listed[i][j]) + '  '
    print(text)
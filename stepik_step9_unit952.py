start = input()
searchValue = input()
start = start.split(" ")
result = ''
k = 0
for i in range(len(start)):
    if start[i] == searchValue:
        print(i, end=' ')
        k += 1
if k == 0:
    print('Отсутствует')

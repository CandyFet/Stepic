start = ''
matrix = []
while True:
    start = input()
    if start == 'end':
        break
    matrix.append([int(i) for i in start.split()])
li, lj = len(matrix), len(matrix[0])
result_matrix = [[sum([matrix[i-1][j], matrix[(i+1)%li][j], matrix[i][j-1], matrix[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
for i in range(li):
    for j in range(lj):
        print(result_matrix[i][j], end=' ')
    print()

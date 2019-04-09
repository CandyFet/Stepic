def spiral(input):
    dx, dy = 1, 0
    x, y = 0, 0
    myarray = [[None] * input for j in range(input)]
    for i in range(1, input ** 2 + 1):
        myarray[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < input and 0 <= ny < input and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray


def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=' ')
        print()


start = int(input())
printspiral(spiral(start))
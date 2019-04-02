start = input().split()
int_array = [int(i) for i in start]
ind = 0
for elements in int_array:
    if len(int_array) == 1:
        print(elements)
    elif len(int_array) == 2:
        print(int_array[ind-1]*2)
        ind += 1
    elif len(int_array) > 2 and ind != len(int_array) - 1:
        sum_of = int_array[ind-1] + int_array[ind+1]
        ind += 1
        print(sum_of)
    elif ind == len(int_array) - 1 and len(int_array) > 2:
        sum_of = int_array[ind-1] + int_array[0]
        print(sum_of)

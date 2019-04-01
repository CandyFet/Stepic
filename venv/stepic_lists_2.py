start = '11 2 3 3 3  1 23 41 2'
int_array = [int(i) for i in start]
if len(int_array) == 1:
    print(int_array[0])
else:
    for element in int_array:
        ind = int_array.index(element)
        sum_array = []
        if ind != 0 and len(int_array) != 2:
            sum_array.append(int_array[ind-1]+int_array[ind+1])
        elif ind == 0 and len(int_array) != 2:
            sum_array.append(int_array[-1] + int_array[1])
        elif len(int_array) == 2:
            sum_array.append(int_array[0] + int_array[1])
print(sum_array)

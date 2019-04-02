start = input().split()
int_array = [int(i) for i in start]
res_arr = []
for element in int_array:
    if int_array.count(element) > 1:
        res_arr.append(element)
    else:
        continue
res_arr = list(set(res_arr))
for element in res_arr:
    print(element, end=" ")
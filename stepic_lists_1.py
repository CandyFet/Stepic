start = input().split()
int_array = [int(i) for i in start]
result = 0
for element in int_array:
    result = result + element
print(result)
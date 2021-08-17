src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num_first = src[0]
result=[]

for num_second in src[1:]:
    if num_second > num_first:
        result.append(num_second)
    num_first=num_second

print(result)
def my_gen(n):
    for num in range(1, n+1, 2):
        yield num

nums = my_gen(int(input('Enter your n number: ')))
print(*nums)
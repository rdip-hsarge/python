n = int(input('Enter your n number: '))
my_gen = (num for num in range(1, n+1, 2))
print(*my_gen)
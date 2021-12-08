input_num = input()
(multiply, sum) = (1, 0)

for digit in input_num:
    multiply *= int(digit)
    sum += int(digit)

print(sum, multiply)
import sys

from task_4_3 import currency_rates

if not sys.argv:
  result = input('Enter your currency: ')
else:
  result = sys.argv[1]
print(currency_rates(result))

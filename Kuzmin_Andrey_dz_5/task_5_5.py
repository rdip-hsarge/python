from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
now=perf_counter()
result = [num for num in src if src.count(num) == 1]
print(result, perf_counter()-now) #1.33*10e-5

# now = perf_counter()
# repit = set()
# orig = set()
# for num in src:
#     if num in repit:
#         orig.discard(num)
#     else:
#         orig.add(num)
#     repit.add(num)
#
# result = [num for num in src if num in orig]
# print(result, perf_counter()-now) #1.89*10e-5
# https://projecteuler.net/problem=16

count = 0
value = str(2**1000)
for i in value:
  count = count + int(i)
print(count)
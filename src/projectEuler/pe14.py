# https://projecteuler.net/problem=14

def chain(n):
  if n == 1:
    return 1
  
  count = 1
  while n > 1:
    if n % 2 == 0:
      n = n/2
      count = count + 1
    else:
      n = (3*n) + 1
      count = count + 1
  return count

largest = 1
pair = []
for n in range(500000, 1000000):
  value = chain(n)
  if value > largest: 
    largest = value
    pair = [largest, n]

print(pair[1])
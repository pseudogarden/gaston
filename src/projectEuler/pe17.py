# https://projecteuler.net/problem=17

import inflect
import re
p = inflect.engine()

total = 0

for x in range(1, 1001):
  word = p.number_to_words(x)
  word = re.sub('[ -]', '', word)
  total = total + len(word)
print(total)
# https://projecteuler.net/problem=15

'''
If we want to go from (0,0) to (20,20) then we already know that we have to go right 20 times
and down 20 times. So we can rephrase the question from "How many different ways can you 
go to (20,20)?" to "In how many different ways can you go 20 times right and 20 times down?".
The second question is now purely a basic binomial coefficient calculation. The answer to it is
          (40 20) = 40!/(40−20)!20!
'''
res = 1
for i in range(20):
  res = res * (40-i) / (i+1)
print(res)
from factorial import fact

print(fact(5))

e = 1
for i in  range(1, 10):
   e += 1 / fact(i)

print(e)
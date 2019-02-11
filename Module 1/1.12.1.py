a = int(input())
b = int(input())
c = int(input())
import math

p = (a + b + c) / 2
result = p * (p - a) * (p - b) * (p - c)
s = math.sqrt(result)
print(s)

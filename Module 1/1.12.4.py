figure = input()
import math

if figure == "треугольник":
    b = int(input())
    c = int(input())
    d = int(input())
    p = (d + b + c) / 2
    s = p * (p - d) * (p - b) * (p - c)
    res = math.sqrt(s)
    print(res)
elif figure == "прямоугольник":
    a = int(input())
    b = int(input())
    res1 = a * b
    print(res1)
elif figure == "круг":
    r = int(input())
    res3 = r * r * 3.14
    print(res3)

a = int(input())
if a % 10 == 1 and a % 100 != 11:
    print(str(a) + " программист")
elif a % 10 == 2 and a % 100 != 12 or a % 10 == 3 and a % 100 != 13 or a % 10 == 4 and a % 100 != 14:
    print(str(a) + " программиста")
else:
    print(str(a) + " программистов")

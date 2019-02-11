lst = [int(i) for i in input().split()]
x = int(input())
a = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=" ")
        a += 1
if a < 1:
    print("Отсутствует")

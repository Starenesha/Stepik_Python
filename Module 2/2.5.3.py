a = input().split()
result = []
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
k = 0
ab = []
for j in range(len(a)):
    if (a.count(a[j]) > 1):
        if ((a[j] in ab) == 0):
            ab.append(a[j])
for k in ab:
    print(k, end=" ")

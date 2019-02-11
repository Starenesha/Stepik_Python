a = input().split()
result = []
for i in range(0, len(a)):
    if (len(a) == 1):
        result.append(int(a[i]))
    elif (len(a) == 0):
        result.append(int(a[i - 1]) + int(a[i + 1]))
    elif (i == len(a) - 1):
        result.append(int(a[0]) + int(a[i - 1]))
    else:
        result.append(int(a[i - 1]) + int(a[i + 1]))
for j in result:
    print(j, end=" ")

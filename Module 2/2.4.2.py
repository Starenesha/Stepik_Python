str1 = str(input())
c = 1
p = 1
str_n = str1[p:p + 1]
for i in str1:
    if i in str_n:
        c += 1
    else:
        print(i, end=" ")
        print(c, end=" ")
        c = 1
    p += 1
    str_n = str1[p:p + 1]

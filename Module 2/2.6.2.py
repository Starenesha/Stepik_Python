num = int(input())
i = 1  # счетчик сколько вывело чисел
j = 1
n = 0  # число что нужно вывести на экран
br = 0  # переменная сравнивает num=br если равно выходит
while i <= num:
    j = 1
    n += 1
    while j <= n:
        if br == num:
            break
        print(n, end=" ")
        br += 1
        j += 1
    i += 1

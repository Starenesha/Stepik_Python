a = [str(i).lower() for i in input().split()]
cr = 0
fullnum = set(a)  # множества несодержат повторяющихся элементов
for i in fullnum:
    cr = a.count(i)
    print(str(i), cr)

a = input()
a = a.lower()
p_G = 'g'  #
p_C = 'c'
count_C = a.count(p_C)  # Подсчитывает в "а" количество букв "g"(который передан параметром)
count_G = a.count(p_G)

add = count_C + count_G
result = add / len(a) * 100
print(result)

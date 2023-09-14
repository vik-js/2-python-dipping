# 1. Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_elem = [2, 5, 90, 14, 4, 2, 14, 5, 9, 90, 8, 16, 2, 4, 5]

res_lst = []

for i in set(list_elem):
    if list_elem.count(i) != 1:
        res_lst.append(i)

print(*res_lst, sep=', ')
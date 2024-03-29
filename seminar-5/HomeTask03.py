# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

lst1 = ['Александра', 'Виктория', 'Вероника']
lst2 = [10_000, 20_000, 5_000]
lst3 = ['10.25%', '20.11%', '5.75%']

dictionary = {l1: l2 * float(l3[:-1]) / 100 for l1, l2, l3 in zip(lst1, lst2, lst3)}  # размер премии
#dictionary = {l1: l2 * float(l3[:-1]) / 100 + l2 for l1, l2, l3 in zip(lst1, lst2, lst3)}  # полная сумма с премией
print(dictionary)

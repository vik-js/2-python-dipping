# 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные
# варианты комплектации рюкзака.

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

weight_backpack = int(input('Укажите грузоподъёмность рюкзака в кг: '))

sum_f = 0
sum_all = 0
lst = []

for key, value in things.items():
    sum_all = sum_all + value
    if sum_f < weight_backpack * 1000:
        sum_f = sum_f + value
        lst.append(key)

if sum_f < sum_all:
    sum_f = sum_f - things.get((lst[-1]))
    lst.pop()

print(f"В рюкзак грузоподъёмностью {weight_backpack} кг влезет {len(lst)} вещей: ")
print(*lst, sep=", ")

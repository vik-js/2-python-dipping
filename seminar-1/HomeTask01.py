# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10
# как на школьной тетрадке.

for j in range(2, 11):
    for i in range(2, 10):
        if i < 6:
            if j == 10:
                print(f'{i:>0} x {j} = {i * j : <9}', end='')
            else:
                print(f'{i} x {j} = {i * j : <10}', end='')
    print('')
print('')
for j in range(2, 11):
    for i in range(2, 10):
        if i > 5:
            if j == 10:
                print(f'{i:>0} x {j} = {i * j : <9}', end='')
            else:
                print(f'{i} x {j} = {i * j : <10}', end='')
    print('')

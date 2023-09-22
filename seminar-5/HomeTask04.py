# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

n = int(input("Номер элемента ряда Фибоначчи: "))


def feb_generator(m):
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


fib = feb_generator(n)
result = [next(fib) for i in range(n)]
print(*result)

# 2. Напишите следующие функции:
# 3. Нахождение корней квадратного уравнения
# 4. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# 5. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# 6. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 7. Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import json
import math
import csv
import random


# 3. Нахождение корней квадратного уравнения
def find_quadratic_roots(a, b, c):
	discriminant = b ** 2 - 4 * a * c
	if discriminant > 0:
		root1 = (-b + math.sqrt(discriminant)) / (2 * a)
		root2 = (-b - math.sqrt(discriminant)) / (2 * a)
		return root1, root2
	elif discriminant == 0:
		root = -b / (2 * a)
		return root
	else:
		return "No real roots"


# 4. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv_file(filename, num_rows):
	with open(filename, mode='w', newline='') as file:
		writer = csv.writer(file)
		for _ in range(num_rows):
			row = [random.randint(1, 1000) for _ in range(3)]
			writer.writerow(row)


# 5. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def quadratic_equation_decorator(func):
	def wrapper(filename):
		with open(filename, mode='r') as file:
			reader = csv.reader(file)
			for row in reader:
				a, b, c = map(int, row)
				result = func(a, b, c)
				print(f"Equation: {a}x^2 + {b}x + {c} = 0")
				print(f"Roots: {result}")

	return wrapper


# 6. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def json_file_saver_decorator(func):
	def wrapper(filename):
		results = {}
		with open(filename, mode='r') as file:
			reader = csv.reader(file)
			for row in reader:
				a, b, c = map(int, row)
				result = func(a, b, c)
				results[(a, b, c)] = result
		with open('results.json', mode='w') as json_file:
			json.dump(results, json_file)

	return wrapper
a = input("A: ")
b = input("B: ")
c = input("C: ")


if (a+b>c and a+c>b and b+c>a):
	print("Да")
else:
	print("Нет")

# print('ДА'if is_triangle(*[int(input(i))for i in'abc'])else'НЕТ')
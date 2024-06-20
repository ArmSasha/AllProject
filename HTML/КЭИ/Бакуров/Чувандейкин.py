x = int(input("Введите число: "))
i = 1
spisok = []
while (x % i) == 0:
	spisok.append(i)
	i+=1
else:
	print(spisok)

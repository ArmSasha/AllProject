stroka = input("Введите шаблон, в который будут подставляться данные: ")

data = input("Введите фамилию и через пробел имя: ").split()

def conclusion(data, stroka):
	result = (stroka).replace('%F%', str(data[0])).replace('%N%', str(data[1]))
	print (result)


conclusion(data, stroka)

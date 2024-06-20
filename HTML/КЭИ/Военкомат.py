student = input("Вы студент? ")

number_of_children = int(input("Введите количество детей: "))

age = int(input("Введите полный возраст: "))

height = int(input("Введите свой рост в сантиметрах: "))


if (student == "Да" or student == "да"):
	student = 0

else:
	student = 1


if student == 0:
	print("Учись студент")
	exit()

else:

	if (number_of_children > 1):
		print("Стирай пелёнки")
		exit()

	else:

		if age < 18 or age > 27:
			print("Не подходишь по возрасту")
			exit()
		else:

			if (height <= 170):
				print("Танковые войска")

			elif (height > 170 and height < 181):
				print("Мотострелковые войска")

			elif (height > 180 and height < 190):
				print("Десантные войска")

			elif (height > 190):
				print("Другие войска")









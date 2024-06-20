things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300}
d = []

s = 1

while s:
	items = input('Введите данные в формате "предмет вес": ').split()
	if items == '':
		s = 0
	d.append(items)

print(d)

# sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))
# for k, v in sorted_things.items():
#     if v <= ves:
#         print(k, end=' ')
#         ves -= v
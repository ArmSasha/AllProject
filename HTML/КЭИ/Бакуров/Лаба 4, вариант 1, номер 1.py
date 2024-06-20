chis = int(input())
i = 1
dif = []
while (i <= chis):
	if (chis % i == 0):
		dif.append(i)
	i += 1
print(dif)
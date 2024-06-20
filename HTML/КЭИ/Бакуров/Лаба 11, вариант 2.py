f = filter(lambda x: len(x) > 5, input().split())
for i in range(3):
	print(next(f))
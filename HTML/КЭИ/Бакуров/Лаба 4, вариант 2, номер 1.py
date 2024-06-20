num = input("Введите число:")
x = 0
i = 0
while i<len(num):
    for a in num:
        x+= int(a)
        i+=1
print(x)

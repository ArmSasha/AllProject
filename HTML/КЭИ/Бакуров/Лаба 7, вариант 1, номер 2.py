N = int(input('N:'))


for i in range(N):
	if i<N:
		print(i)
	else:
		N+=1
print(N)

# def F(i,N):return None if i>N else(print(i),F(i+1,N))
# F(1,int(input('N:')))
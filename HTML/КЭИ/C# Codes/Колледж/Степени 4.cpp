#include <stdio.h>
#include <math.h>


int main()
{

	int i;
	long stepen;
	int N;
	printf("N=");
	scanf_s("%d", &N);


	stepen = 1;
	i = 0;

	do {
		printf("4^%d = %li\n ", i, stepen);
		i += 1;
		stepen = stepen * 2;
	} while (i <= N);

}
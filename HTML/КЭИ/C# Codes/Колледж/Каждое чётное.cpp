#include <stdio.h>
#include <math.h>


void main()
{


	int a;
	int i;
	int N;

	printf("N= ");
	scanf_s("%d", &N);

	i = 2;
	a = 0;
	do {
		printf("%d", i);
		a += 1;
		i = i + 2;
	} while (a < N);

}
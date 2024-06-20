#include <stdio.h>
#include <math.h>

void main()
{
	int N, K, i, sum;
	printf("Number of months: ");
	scanf_s("%d", &N);

	printf("Percent: ");
	scanf_s("%d", &K);

	i = 0;
	sum = 1000;
	do {
		printf("In %i month - %d\n", i, sum);
		i += 1;
		sum += 1000;
		int p = K / 100;
		printf("%d", K );
		sum = sum * (K / 100);
	} while (i <= N);

}
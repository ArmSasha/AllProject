#include <stdio.h>
#include <math.h>


int main()
{

	int a, b, c, N, i;
	printf("N=");
	scanf_s("%d", &N);

	a = 0;
	b = 1;
	i = 0;
	c = 0;


	do {
		printf("%d %d", a, b);
		i += 1;
		c = a + b;
		a = b;
		b = c;
	} while (i <= N);

}
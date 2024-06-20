#include <stdio.h>
#include <math.h>


void main()
{


	float v;
	float g;
	printf("Weight: ");
	scanf_s("%f", &v);

	g = 9.8;

	float gravity = (v * g);

	printf("Gravity: %f ", gravity);

}
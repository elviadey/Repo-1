#include <stdio.h>

int main(void)
{
	int a;
	int *aptr;

	a = 10;
	aptr = &a;

	printf("The address of a is %p"
		"\n The value of aptr is %p", &a, aptr);
	printf("\n\n The value pf a is %d"
		"\n\n The value of *aptr is %d", a, *aptr);
	printf("\n\n Showing that * and & are complements of each other\n&*apt = %p"
		"\n*&aptr = %p\n", &*aptr, *&aptr);
}

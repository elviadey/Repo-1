#include <stdio.h>
#include <stdlib.h>

int naive(int k);
int interesting(int k);
void main()
{
	int n,j,l;
	printf("Enter the value of n :");
	scanf("%d", &n);
	if (n<0)
	{
		printf("Input is erroneous\n");
		exit(0);
	}
	j = naive(n);
	l = interesting(n);
	printf("Naive : %d\n", j);
	printf("Interesting : %d\n", l);
}
int naive(int k)
{
	int s=0, i;
	for (i = 1; i<=k; i++)
	{s = s + (i*i);}
	return s;
}
int interesting(int k)
{
	int s=0;
	s = (k*(k+1)*((2*k)+1))/6;
	return s;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char S[1000];
	printf("%s", "Enter a String: ");
	gets(S);
	if (strlen(S)>50)
	{	
		printf("Invalid Input");
		exit(0);
	}
	int f = S[0];
	int l = S[strlen(S)-1];
	char S1[1000];
	if (f==32)
	{
		char *S1 = S+1;
		for (int i=0; i<strlen(S1);i++)
		{
			S[i]=S1[i];
		}
		S[strlen(S)-1] = '\0';
	}
	if (l==32)
	{
		S[strlen(S)-1] = '\0';
	}
	char* A = S;
	char* B = S;
	for (int i=0; i<strlen(S);i++)
	{
		int k = S[i];
		if ( k<65 || (k>90 && k<97) || k>122)
		{
			if (k!=32)
			{
				printf("Invalid Input");
				exit(0);
			}
		}
	}
	while (*B != 0)
	{
		B = B+1;
	}
	B = B-1;
	while(A<B)
	{
		int a = *A;
		int b = *B;
		if (a!=b)
		{
			if (a+32!=b && a-32!=b)
			{
				printf("No, the string is not a palindrome.");
				exit(0);
			}
		}
		A = A + 1;
		B = B - 1;
	}
	printf("Yes, the string is a palindrome.");
}
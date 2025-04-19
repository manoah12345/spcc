%{
#include<stdio.h>
#include<string.h>
int i = 0;
int j = 0;
%}

%%
[aeiouAEIOU] {i++;}
[a-zA-Z] {j++;}
"\n" {printf("\nVowels: %d \nConsonants: %d\n", i,j);}
%%

int yywrap(void){}

int main()
{
yylex();
return 0;
}
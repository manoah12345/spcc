%{
#include<stdio.h>
#include<string.h>
int i = 0;
int j = 0;
%}
%%
[a-z] {i++;}
[A-Z] {j++;}
"\n" {printf("Lowercase: %d \nUppercase: %d\n", i,j);}
%%
int yywrap(void){}
int main()
{
yylex();
return 0;
}
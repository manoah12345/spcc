%{
#include<stdio.h>
#include<stdlib.h>
void yyerror();
int yylex();
int i = 0;
int j = 0;
%}
%token a b NL
%%
Statement: S NL {
if(i+1==j)
printf("Valid String\n a = %d b = %d", i,j);
else
printf("Invalid string \n a = %d b = %d", i,j);
exit(0); };
S: A B;
A: A a {i++;}| ;
B: B b {j++;}| ;
%%
void main()
{
printf("\nEnter String: ");
yyparse();
}
void yyerror()
{
printf("Invalid String");
exit(0);
}
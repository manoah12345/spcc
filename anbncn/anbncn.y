%{
#include<stdio.h>
#include<stdlib.h>
void yyerror();
int yylex();
int i = 0;int j = 0;int k = 0;
%}
%token a b c NL
%%
Statement: S NL {
if(i==j && i==k) printf("Valid String\n a = %d b = %d c = %d", i,j,k);
else printf("Invalid string \n a = %d b = %d c = %d", i,j,k); exit(0); };
S: A B C;
A: A a {i++;}| ;
B: B b {j++;}| ;
C: C c {k++;}| ;
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
%{
#include<stdio.h>
#include<string.h>
int keywords = 0;
int identifiers = 0;
int operators = 0;
int numbers = 0;
int special = 0;
%}
%%
"while"|"if"|"else"|"int"|"float"|"printf" {keywords++;printf("\nKeyword :");ECHO;}
[a-zA-Z_][a-zA-Z0-9_]* {identifiers++;printf("\nIdentifier :");ECHO;}
"<="|"=="|"="|"++"|"-"|"*"|"+" {operators++;printf("\nOperator :");ECHO;}
[0-9]+ {numbers++;printf("\nNumber :");ECHO;}
([(){}|,;"]) {special++;printf("\nSpecial Symbol :");ECHO;}
"\n" {printf("\nTotal Tokens: %d", keywords+identifiers+operators+numbers+special);}
%%
int yywrap(void){}
int main()
{
yylex();
return 0;
}
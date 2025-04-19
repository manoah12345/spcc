%{
#include<stdio.h>
#include<stdlib.h>
void yyerror(char *s);
int yylex();
int i = 0;
int j = 0;
%}

%token a b NL

%%
Statement: S NL {
    if(i == 2 * j)
        printf("Valid String\n a = %d b = %d\n", i, j);
    else
        printf("Invalid String\n a = %d b = %d\n", i, j);
    exit(0);
};

S: A B;
A: A a { i++; } | ;
B: B b { j++; } | ;
%%

int main()
{
    printf("\nEnter String: ");
    yyparse();
    return 0;
}

void yyerror(char *s)
{
    printf("Invalid String\n");
    exit(0);
}

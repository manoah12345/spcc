%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
[0-9]+  {
            int num = atoi(yytext);
            if (num % 2 == 0)
                printf("%d is Even\n", num);
            else
                printf("%d is Odd\n", num);
        }
.|\n    { /* Ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a number: ");
    yylex();
    return 0;
}

%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
[0-9]{10}    { printf("Valid Mobile Number: %s\n", yytext); }
[0-9]+       { printf("Invalid Mobile Number: %s (Not 10 digits)\n", yytext); }
.|\n         { /* Ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter Mobile Number: ");
    yylex();
    return 0;
}

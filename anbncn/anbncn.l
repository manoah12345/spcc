%{
#include<stdio.h>
#include "demo.tab.h"
%}
%%
[a] {return a;}
[b] {return b;}
[c] {return c;}
\n {return NL;}
. {return yytext[0];}
%%
int yywrap()
{
return 1;
}

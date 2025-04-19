%{
#include "y.tab.h"
%}

%%
a   { return a; }
b   { return b; }
\n  { return NL; }
.   { /* Ignore any other character */ }
%%

int yywrap() {
    return 1;
}

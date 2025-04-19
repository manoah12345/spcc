%{
#include "y.tab.h"
%}

%%
a   { return a; }
b   { return b; }
\n  { return NL; }
.   { /* ignore any other character */ }
%%

int yywrap() {
    return 1;
}

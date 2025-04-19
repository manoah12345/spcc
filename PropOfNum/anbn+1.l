%{
#include "y.tab.h"
%}

%%
a { return a; }
b { return b; }
\n { return NL; }
.  { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}

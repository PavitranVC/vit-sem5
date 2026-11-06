%{
#include "y.tab.h"
#include <stdio.h>
#include <string.h>
%}

%%
"int"|"float"|"char"|"double"|"void"|"if"|"else"|"while"|"for"|"return"|"include"|"print" ;
[a-zA-Z_][a-zA-Z0-9_]* { 
    strcpy(yylval.str, yytext); 
    return IDENTIFIER; 
}
[ \t\n]+               ;
.                      ;
%%

int yywrap() {
    return 1;
}

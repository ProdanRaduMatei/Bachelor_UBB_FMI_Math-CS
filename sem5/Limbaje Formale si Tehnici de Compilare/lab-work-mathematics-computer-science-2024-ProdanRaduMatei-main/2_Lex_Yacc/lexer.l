%{
#include "y.tab.h"
#include <stdio.h>
#include <string.h>

int yywrap(void) { return 1; }
%}

%%

int             { return INT; }
float           { return FLOAT; }
struct          { return STRUCT; }
if              { return IF; }
else            { return ELSE; }
while           { return WHILE; }
print           { return PRINT; }
input           { return INPUT; }
cin             { return CIN; }
cout            { return COUT; }
break           { return BREAK; }

"=="|"!="|"<="|">="|"<"|">"    { return RELOP; }
"+"|"-"                        { return ADDOP; }
"*"|"/"|"%"                    { return MULOP; }
"="                            { return ASSIGN; }
">>"                           { return SHIFTIN; }
"<<"                           { return SHIFTOUT; }

";"                            { return SEMICOLON; }
","                            { return COMMA; }
"{"                            { return LBRACE; }
"}"                            { return RBRACE; }
"("                            { return LPAREN; }
")"                            { return RPAREN; }

[0-9]+"."[0-9]+                { yylval.sval = strdup(yytext); return FLOAT_CONSTANT; }
[0-9]+                         { yylval.sval = strdup(yytext); return INTEGER_CONSTANT; }
[a-zA-Z_][a-zA-Z0-9_]*          { yylval.sval = strdup(yytext); return IDENTIFIER; }

[ \t\n\r]+                     { /* ignore whitespace */ }
.                              { fprintf(stderr, "Unknown character: %s\n", yytext); }

%%
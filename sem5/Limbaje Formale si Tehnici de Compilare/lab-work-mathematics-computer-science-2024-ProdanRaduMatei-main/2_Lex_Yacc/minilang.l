%{
#include "y.tab.h"
%}

%%
"int"           { return INT; }
"float"         { return FLOAT; }
"struct"        { return STRUCT; }
"if"            { return IF; }
"else"          { return ELSE; }
"while"         { return WHILE; }
"print"         { return PRINT; }
"input"         { return INPUT; }

"=="            { return EQ; }
"!="            { return NE; }
"<"             { return LT; }
">"             { return GT; }
"<="            { return LE; }
">="            { return GE; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"*"             { return MUL; }
"/"             { return DIV; }
"="             { return ASSIGN; }

"("             { return LPAREN; }
")"             { return RPAREN; }
"{"             { return LBRACE; }
"}"             { return RBRACE; }
";"             { return SEMICOLON; }
","             { return COMMA; }

[0-9]+\.[0-9]+  { yylval = atof(yytext); return FLOAT_CONSTANT; }
[0-9]+          { yylval = atoi(yytext); return INTEGER_CONSTANT; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval = strdup(yytext); return IDENTIFIER; }

[ \t\n\r]+      ; // Ignore whitespace
.               { printf("Unknown character: %s\n", yytext); return yytext[0]; }
%%
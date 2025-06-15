%{
#include <stdio.h>
#include <stdlib.h>

typedef char* YYSTYPE;

// External declarations
extern int yylex();
extern int yylineno;
void yyerror(const char* s);

void print_production(const char* production) {
    printf("Production used: %s\n", production);
}
%}

// Tokens
%token PLUS MINUS MUL DIV
%token EQ NE LT GT LE GE
%token IDENTIFIER INTEGER_CONSTANT FLOAT_CONSTANT

%start program

%%

program
    : statement_list { printf("Program syntactic correct.\n"); }
    ;

statement_list
    : statement
    | statement statement_list
    ;

statement
    : assignment_statement
    | input_statement
    ;

assignment_statement
    : IDENTIFIER '=' expression ';'
    ;

input_statement
    : "input" IDENTIFIER ';'
    ;

expression
    : term
    | expression add_op term { print_production("<expression> -> <expression> <add_op> <term>"); }
    ;

term
    : factor
    | term mul_op factor { print_production("<term> -> <term> <mul_op> <factor>"); }
    ;

factor
    : IDENTIFIER
    | INTEGER_CONSTANT
    | FLOAT_CONSTANT
    ;

add_op
    : PLUS { print_production("<add_op> -> '+'"); }
    | MINUS { print_production("<add_op> -> '-'"); }
    ;

mul_op
    : MUL { print_production("<mul_op> -> '*'"); }
    | DIV { print_production("<mul_op> -> '/'"); }
    ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s at line %d\n", s, yylineno);
    exit(1);
}
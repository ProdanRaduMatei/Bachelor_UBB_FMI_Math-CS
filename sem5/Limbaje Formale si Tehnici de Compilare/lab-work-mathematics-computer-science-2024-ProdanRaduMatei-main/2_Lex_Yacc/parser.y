%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char *s);

int syntax_correct = 1;

/* We will track productions: */
#define MAX_PRODUCTIONS 1000
int productions_used[MAX_PRODUCTIONS];
int productions_count = 0;
int last_production = 0;

/* Helper function to record a production number */
void record_production(int p) {
    if (productions_count < MAX_PRODUCTIONS) {
        productions_used[productions_count++] = p;
        last_production = p;
    }
}
%}

%union {
    char *sval;
}

%token <sval> IDENTIFIER INTEGER_CONSTANT FLOAT_CONSTANT
%token INT FLOAT STRUCT IF ELSE WHILE PRINT INPUT
%token CIN COUT BREAK
%token RELOP ADDOP MULOP ASSIGN SEMICOLON COMMA
%token SHIFTIN SHIFTOUT
%token LPAREN RPAREN LBRACE RBRACE

%%

program : statement_list
    {
        record_production(1);
        if (syntax_correct) {
            printf("Program syntactic correct\n");
            // Print the productions used
            for (int i = 0; i < productions_count; i++) {
                printf("%d ", productions_used[i]);
            }
            printf("\n");
        }
    }
;

statement_list : statement
    {
        record_production(2);
    }
    | statement statement_list
    {
        record_production(3);
    }
;

statement : assignment_statement
    {
        record_production(4);
    }
    | input_statement
    {
        record_production(5);
    }
    | output_statement
    {
        record_production(6);
    }
    | conditional_statement
    {
        record_production(7);
    }
    | loop_statement
    {
        record_production(8);
    }
    | declaration_statement
    {
        record_production(9);
    }
    | BREAK SEMICOLON
    {
        record_production(10);
    }
    | struct_definition
    {
        record_production(32); /* New production for struct_definition as a statement */
    }
;

declaration_statement : type IDENTIFIER SEMICOLON
    {
        record_production(11);
    }
;

assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON
    {
        record_production(12);
    }
;

input_statement : CIN SHIFTIN IDENTIFIER SEMICOLON
    {
        record_production(13);
    }
;

output_statement : COUT SHIFTOUT expression SEMICOLON
    {
        record_production(14);
    }
;

conditional_statement : IF LPAREN expression RPAREN block
    {
        record_production(15);
    }
    | IF LPAREN expression RPAREN block ELSE block
    {
        record_production(16);
    }
;

loop_statement : WHILE LPAREN expression RPAREN block
    {
        record_production(17);
    }
;

block : LBRACE statement_list RBRACE
    {
        record_production(18);
    }
;

expression : term
    {
        record_production(19);
    }
    | term operation expression
    {
        record_production(20);
    }
;

term : factor
    {
        record_production(21);
    }
    | factor MULOP term
    {
        record_production(22);
    }
;

factor : IDENTIFIER
    {
        record_production(23);
    }
    | INTEGER_CONSTANT
    {
        record_production(24);
    }
    | FLOAT_CONSTANT
    {
        record_production(25);
    }
    | LPAREN expression RPAREN
    {
        record_production(26);
    }
;

operation : ADDOP
    {
        record_production(27);
    }
    | RELOP
    {
        record_production(28);
    }
;

type : INT
    {
        record_production(29);
    }
    | FLOAT
    {
        record_production(30);
    }
    | STRUCT IDENTIFIER
    {
        record_production(31);
    }
;

struct_definition : STRUCT IDENTIFIER LBRACE struct_field_list RBRACE SEMICOLON
    {
        record_production(33);
    }
;

struct_field_list : struct_field
    {
        record_production(34);
    }
    | struct_field struct_field_list
    {
        record_production(35);
    }
;

struct_field : type IDENTIFIER SEMICOLON
    {
        record_production(36);
    }
;

%%

void yyerror(const char *s) {
    syntax_correct = 0;
    fprintf(stderr, "Error: %s\n", s);
    // Print error and the last production where parsing was successful
    printf("Error %d\n", last_production);
}

int main() {
    if (yyparse() != 0 && !syntax_correct) {
        // In case yyparse returns non-zero
        // We already printed in yyerror the error and last production
    }
    return 0;
}
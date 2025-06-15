%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int symbolTableIndex = 0;
    int lineNumber = 1;

    // Structure for Symbol Table Entries
    typedef struct {
        char symbol[100];
        int index;
    } SymbolTableEntry;

    // Symbol Table and File Pointers for PIF, ST, and Error logs
    SymbolTableEntry symbolTable[1000];  
    FILE *pifFile, *stFile, *errorFile;  

    // Insert into Symbol Table (ST) if not already present
    int insertIntoSymbolTable(char *symbol) {
        for(int i = 0; i < symbolTableIndex; i++) {
            if(strcmp(symbolTable[i].symbol, symbol) == 0) {
                return symbolTable[i].index;  // Already in the table
            }
        }
        // Add new symbol
        strcpy(symbolTable[symbolTableIndex].symbol, symbol);
        symbolTable[symbolTableIndex].index = symbolTableIndex;
        symbolTableIndex++;
        return symbolTableIndex - 1;
    }

    // Add token to Program Internal Form (PIF)
    void addToPIF(char *token, int stIndex) {
        fprintf(pifFile, "%s %d\n", token, stIndex);
    }

%}

%option noyywrap

DIGIT     [0-9]
LETTER    [a-zA-Z]
ID        {LETTER}({LETTER}|{DIGIT}|_)*
NUM       {DIGIT}+

%%

"int"      { addToPIF("int", -1); }
"float"    { addToPIF("float", -1); }
"struct"   { addToPIF("struct", -1); }
"if"       { addToPIF("if", -1); }
"else"     { addToPIF("else", -1); }
"while"    { addToPIF("while", -1); }
"cin"      { addToPIF("cin", -1); }
"cout"     { addToPIF("cout", -1); }

"+"        { addToPIF("+", -1); }
"-"        { addToPIF("-", -1); }
"*"        { addToPIF("*", -1); }
"/"        { addToPIF("/", -1); }
"="        { addToPIF("=", -1); }
"=="       { addToPIF("==", -1); }
"!="       { addToPIF("!=", -1); }
"<"        { addToPIF("<", -1); }
">"        { addToPIF(">", -1); }
"<="       { addToPIF("<=", -1); }
">="       { addToPIF(">=", -1); }

";"        { addToPIF(";", -1); }
","        { addToPIF(",", -1); }
"{"        { addToPIF("{", -1); }
"}"        { addToPIF("}", -1); }
"("        { addToPIF("(", -1); }
")"        { addToPIF(")", -1); }

{ID}       { int index = insertIntoSymbolTable(yytext); addToPIF("ID", index); }
{NUM}      { int index = insertIntoSymbolTable(yytext); addToPIF("NUM", index); }
[ \t\r\n]+ { /* Ignore whitespace */ }

\n         { lineNumber++; }

.          { fprintf(errorFile, "Lexical error at line %d: Unknown symbol %s\n", lineNumber, yytext); }

%%

int main(int argc, char **argv) {
    if(argc != 2) {
        printf("Usage: %s <source_file>\n", argv[0]);
        return 1;
    }

    FILE *inputFile = fopen(argv[1], "r");
    if(!inputFile) {
        printf("Error: Cannot open source file.\n");
        return 1;
    }

    // Open output files
    pifFile = fopen("pif.out", "w");
    stFile = fopen("st.out", "w");
    errorFile = fopen("errors.out", "w");

    yyin = inputFile;  // Set input file for Lex

    // Run the scanner
    yylex();

    // Output Symbol Table
    for(int i = 0; i < symbolTableIndex; i++) {
        fprintf(stFile, "%d %s\n", symbolTable[i].index, symbolTable[i].symbol);
    }

    // Close all files
    fclose(inputFile);
    fclose(pifFile);
    fclose(stFile);
    fclose(errorFile);

    return 0;
}
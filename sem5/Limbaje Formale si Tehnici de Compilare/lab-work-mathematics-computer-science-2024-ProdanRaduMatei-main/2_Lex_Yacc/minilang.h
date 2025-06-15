/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IF = 258,
     ELSE = 259,
     MINUS = 260,
     PLUS = 261,
     DIV = 262,
     MUL = 263,
     GE = 264,
     LE = 265,
     GT = 266,
     LT = 267,
     NE = 268,
     EQ = 269,
     INT = 270,
     FLOAT = 271,
     STRUCT = 272,
     WHILE = 273,
     PRINT = 274,
     INPUT = 275,
     IDENTIFIER = 276,
     INTEGER_CONSTANT = 277,
     FLOAT_CONSTANT = 278,
     ASSIGN = 279,
     LPAREN = 280,
     RPAREN = 281,
     LBRACE = 282,
     RBRACE = 283,
     SEMICOLON = 284,
     COMMA = 285
   };
#endif
/* Tokens.  */
#define IF 258
#define ELSE 259
#define MINUS 260
#define PLUS 261
#define DIV 262
#define MUL 263
#define GE 264
#define LE 265
#define GT 266
#define LT 267
#define NE 268
#define EQ 269
#define INT 270
#define FLOAT 271
#define STRUCT 272
#define WHILE 273
#define PRINT 274
#define INPUT 275
#define IDENTIFIER 276
#define INTEGER_CONSTANT 277
#define FLOAT_CONSTANT 278
#define ASSIGN 279
#define LPAREN 280
#define RPAREN 281
#define LBRACE 282
#define RBRACE 283
#define SEMICOLON 284
#define COMMA 285




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;


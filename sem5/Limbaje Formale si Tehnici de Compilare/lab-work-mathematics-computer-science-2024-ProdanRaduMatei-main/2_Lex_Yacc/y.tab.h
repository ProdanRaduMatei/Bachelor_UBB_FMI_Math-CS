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
     IDENTIFIER = 258,
     INTEGER_CONSTANT = 259,
     FLOAT_CONSTANT = 260,
     INT = 261,
     FLOAT = 262,
     STRUCT = 263,
     IF = 264,
     ELSE = 265,
     WHILE = 266,
     PRINT = 267,
     INPUT = 268,
     CIN = 269,
     COUT = 270,
     BREAK = 271,
     RELOP = 272,
     ADDOP = 273,
     MULOP = 274,
     ASSIGN = 275,
     SEMICOLON = 276,
     COMMA = 277,
     SHIFTIN = 278,
     SHIFTOUT = 279,
     LPAREN = 280,
     RPAREN = 281,
     LBRACE = 282,
     RBRACE = 283
   };
#endif
/* Tokens.  */
#define IDENTIFIER 258
#define INTEGER_CONSTANT 259
#define FLOAT_CONSTANT 260
#define INT 261
#define FLOAT 262
#define STRUCT 263
#define IF 264
#define ELSE 265
#define WHILE 266
#define PRINT 267
#define INPUT 268
#define CIN 269
#define COUT 270
#define BREAK 271
#define RELOP 272
#define ADDOP 273
#define MULOP 274
#define ASSIGN 275
#define SEMICOLON 276
#define COMMA 277
#define SHIFTIN 278
#define SHIFTOUT 279
#define LPAREN 280
#define RPAREN 281
#define LBRACE 282
#define RBRACE 283




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 26 "parser.y"
{
    char *sval;
}
/* Line 1529 of yacc.c.  */
#line 109 "y.tab.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;


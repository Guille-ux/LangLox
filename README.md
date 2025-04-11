# ZynkPy
*Programming in your mother tongue*

ZynkPy is a programming language made by me while i read **Crafting Interpreters**

The Objective is have one ZynkPy for a lot of languages.

The Actual Objective is:

- AST
    - [x] Print
    - [x] Variables
    - [ ] Functions
    - [ ] Classes
    - [ ] Input
    - [ ] Import
- [x] Lexer
- [ ] Bytecode
- [ ] Castellano (Spanish)
- [ ] English
- [ ] Galego (Galician)

## What i have actually?
```bash
Input → 5 * (20 - 10 )
---------------------------------Tokens------------------------------
Token of the type TokenType.INT with the value 5 with the lexem 5 
Token of the type TokenType.MULTIPLY with the value None with the lexem *
Token of the type TokenType.LPAREN with the value None with the lexem (
Token of the type TokenType.INT with the value 20 with the lexem 20
Token of the type TokenType.MINUS with the value None with the lexem -
Token of the type TokenType.INT with the value 10 with the lexem 10
Token of the type TokenType.RPAREN with the value None with the lexem )
Token of the type TokenType.EOF with the value None with the lexem 
-------------------------------End Tokens----------------------------

-------------------Parsed------------------
[5] : [*] : [[20] : [-] : [10]]
-----------------End Parsed----------------
Result → 50
```

## Tests

### Function Definition Test
```bash
[line 1, column 11] Error: Unexpected Token:  
[line 1, column 12] Error: Unexpected Token: (
Lexer Passed
Parser Passed
Evaluating...
Evaluator Passed
Test case: func hola () { print "Hola" ; }
-----Tokens-----
Token of the type TokenType.FUNC with the value None with the lexem func
Token of the type TokenType.IDENTIFIER with the value None with the lexem hola 
Token of the type TokenType.LPAREN with the value None with the lexem (
Token of the type TokenType.RPAREN with the value None with the lexem )
Token of the type TokenType.LBRACE with the value None with the lexem {
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.STRING with the value Hola with the lexem "Hola"
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.RBRACE with the value None with the lexem }
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Function : hola  [] Block : [Print : Hola]]
-----Evaluated-----
None
-----End-----
Test case passed
[line 1, column 12] Error: Unexpected Token:  
[line 1, column 13] Error: Unexpected Token: (
Lexer Passed
Parser Passed
Evaluating...
Evaluator Passed
Test case: func adios () { print "Adios" ; }
-----Tokens-----
Token of the type TokenType.FUNC with the value None with the lexem func
Token of the type TokenType.IDENTIFIER with the value None with the lexem adios 
Token of the type TokenType.LPAREN with the value None with the lexem (
Token of the type TokenType.RPAREN with the value None with the lexem )
Token of the type TokenType.LBRACE with the value None with the lexem {
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.STRING with the value Adios with the lexem "Adios"
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.RBRACE with the value None with the lexem }
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Function : adios  [] Block : [Print : Adios]]
-----Evaluated-----
None
-----End-----
Test case passed
[line 1, column 11] Error: Unexpected Token:  
[line 1, column 12] Error: Unexpected Token: (
[line 1, column 15] Error: Unexpected Token:  
[line 1, column 27] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Evaluator Passed
Test case: func copy ( x ) { print x ; }
-----Tokens-----
Token of the type TokenType.FUNC with the value None with the lexem func
Token of the type TokenType.IDENTIFIER with the value None with the lexem copy 
Token of the type TokenType.LPAREN with the value None with the lexem (
Token of the type TokenType.IDENTIFIER with the value None with the lexem x 
Token of the type TokenType.RPAREN with the value None with the lexem )
Token of the type TokenType.LBRACE with the value None with the lexem {
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.IDENTIFIER with the value None with the lexem x 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.RBRACE with the value None with the lexem }
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Function : copy  [VarExpr : x ] Block : [Print : VarExpr : x ]]
-----Evaluated-----
None
-----End-----
Test case passed
```

### Var Test

```bash
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable hola  initialized with 3
Evaluator Passed
Test case: var hola = 1 + 2 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem hola 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 1 with the lexem 1 
Token of the type TokenType.PLUS with the value None with the lexem +
Token of the type TokenType.INT with the value 2 with the lexem 2 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : hola  = [1] : [+] : [2]]
-----Evaluated-----
Variable hola  initialized with 3
3
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable algo  initialized with hola
Evaluator Passed
Test case: var algo = "hola" ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem algo 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.STRING with the value hola with the lexem "hola"
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : algo  = hola]
-----Evaluated-----
Variable algo  initialized with hola
hola
-----End-----
Test case passed
[line 1, column 11] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable nose  initialized with adios
Evaluator Passed
Test case: var nose = "adios" ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem nose 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.STRING with the value adios with the lexem "adios"
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : nose  = adios]
-----Evaluated-----
Variable nose  initialized with adios
adios
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable chao  initialized with 50
Evaluator Passed
Test case: var chao = 10 * 5 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem chao 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 10 with the lexem 10
Token of the type TokenType.MULTIPLY with the value None with the lexem *
Token of the type TokenType.INT with the value 5 with the lexem 5 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : chao  = [10] : [*] : [5]]
-----Evaluated-----
Variable chao  initialized with 50
50
-----End-----
Test case passed
[line 1, column 9] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable uno  initialized with 1
Evaluator Passed
Test case: var uno = 1 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem uno 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 1 with the lexem 1 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : uno  = 1]
-----Evaluated-----
Variable uno  initialized with 1
1
-----End-----
Test case passed
[line 1, column 9] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable dos  initialized with 2
Evaluator Passed
Test case: var dos = 2 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem dos 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 2 with the lexem 2 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : dos  = 2]
-----Evaluated-----
Variable dos  initialized with 2
2
-----End-----
Test case passed
[line 1, column 11] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable tres  initialized with 3
Evaluator Passed
Test case: var tres = 3 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem tres 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 3 with the lexem 3 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : tres  = 3]
-----Evaluated-----
Variable tres  initialized with 3
3
-----End-----
Test case passed
[line 1, column 12] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable cuatro  initialized with 4
Evaluator Passed
Test case: var cuatro = 4 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem cuatro 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 4 with the lexem 4 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : cuatro  = 4]
-----Evaluated-----
Variable cuatro  initialized with 4
4
-----End-----
Test case passed
[line 1, column 11] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable cinco  initialized with 5
Evaluator Passed
Test case: var cinco = 5 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem cinco 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 5 with the lexem 5 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : cinco  = 5]
-----Evaluated-----
Variable cinco  initialized with 5
5
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable seis  initialized with 6
Evaluator Passed
Test case: var seis = 6 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem seis 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 6 with the lexem 6 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : seis  = 6]
-----Evaluated-----
Variable seis  initialized with 6
6
-----End-----
Test case passed
[line 1, column 11] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable siete  initialized with 7
Evaluator Passed
Test case: var siete = 7 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem siete 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 7 with the lexem 7 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : siete  = 7]
-----Evaluated-----
Variable siete  initialized with 7
7
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable ocho  initialized with 8
Evaluator Passed
Test case: var ocho = 8 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem ocho 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 8 with the lexem 8 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : ocho  = 8]
-----Evaluated-----
Variable ocho  initialized with 8
8
-----End-----
Test case passed
[line 1, column 12] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable nueve  initialized with 9
Evaluator Passed
Test case: var nueve = 9 ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem nueve 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 9 with the lexem 9 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : nueve  = 9]
-----Evaluated-----
Variable nueve  initialized with 9
9
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
[line 1, column 28] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable diez  initialized with 10
10
Evaluator Passed
Test case: var diez = 10 ; print diez ;
-----Tokens-----
Token of the type TokenType.VAR with the value None with the lexem var
Token of the type TokenType.IDENTIFIER with the value None with the lexem diez 
Token of the type TokenType.ASSIGN with the value None with the lexem =
Token of the type TokenType.INT with the value 10 with the lexem 10
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.IDENTIFIER with the value None with the lexem diez 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Var : diez  = 10, Print : VarExpr : diez ]
-----Evaluated-----
Variable diez  initialized with 10
10
10
10
-----End-----
Test case passed
```

### Print Test

```bash
Lexer Passed
Parser Passed
Evaluating...
3
Evaluator Passed
Test case: print 1 + 2 ;
-----Tokens-----
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.INT with the value 1 with the lexem 1 
Token of the type TokenType.PLUS with the value None with the lexem +
Token of the type TokenType.INT with the value 2 with the lexem 2 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Print : [1] : [+] : [2]]
-----Evaluated-----
3
3
-----End-----
Test case passed
Lexer Passed
Parser Passed
Evaluating...
hola
Evaluator Passed
Test case: print "hola" ;
-----Tokens-----
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.STRING with the value hola with the lexem "hola"
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Print : hola]
-----Evaluated-----
hola
hola
-----End-----
Test case passed
Lexer Passed
Parser Passed
Evaluating...
adios
Evaluator Passed
Test case: print "adios" ;
-----Tokens-----
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.STRING with the value adios with the lexem "adios"
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Print : adios]
-----Evaluated-----
adios
adios
-----End-----
Test case passed
Lexer Passed
Parser Passed
Evaluating...
50
Evaluator Passed
Test case: print 10 * 5 ;
-----Tokens-----
Token of the type TokenType.PRINT with the value None with the lexem print
Token of the type TokenType.INT with the value 10 with the lexem 10
Token of the type TokenType.MULTIPLY with the value None with the lexem *
Token of the type TokenType.INT with the value 5 with the lexem 5 
Token of the type TokenType.SEMICOLON with the value None with the lexem ;
Token of the type TokenType.EOF with the value None with the lexem 
-----Parsed-----
[Print : [10] : [*] : [5]]
-----Evaluated-----
50
50
-----End-----
Test case passed
```
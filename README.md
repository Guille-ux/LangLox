# ZynkPy
*Programming in your mother tongue*

ZynkPy is a programming language made by me while i read **Crafting Interpreters**

The Objective is have one ZynkPy for a lot of languages.

The Actual Objective is:

- [ ] AST
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

### Var Test

```bash
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable var initialized with 3
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
[Var : var = [1] : [+] : [2]]
-----Evaluated-----
Variable var initialized with 3
3
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable var initialized with hola
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
[Var : var = hola]
-----Evaluated-----
Variable var initialized with hola
hola
-----End-----
Test case passed
[line 1, column 11] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable var initialized with adios
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
[Var : var = adios]
-----Evaluated-----
Variable var initialized with adios
adios
-----End-----
Test case passed
[line 1, column 10] Error: Unexpected Token:  
Lexer Passed
Parser Passed
Evaluating...
Variable var initialized with 50
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
[Var : var = [10] : [*] : [5]]
-----Evaluated-----
Variable var initialized with 50
50
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
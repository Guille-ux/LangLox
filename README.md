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

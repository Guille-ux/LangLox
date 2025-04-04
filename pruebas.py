from src.frontend.lexer import ZynkLexer
from src.ast.parser import AlgebraicParser
from src.ast.eval import *

code = input("Algo para testear bro → ")
lexer = ZynkLexer(code, True)
tokens = lexer.scan_tokens()
print("---------------------------------Tokens------------------------------")
for token in tokens:
	print(token)
perse = AlgebraicParser(tokens)
print("-------------------------------End Tokens----------------------------")
print()
our = perse.parse()
print("-------------------Parsed------------------")
print(our)
print("-----------------End Parsed----------------")
evaler = ZynkEval()
result = evaler.visit(our)
print(f"Result → {result}")

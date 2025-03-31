from src.frontend.lexer import ZynkLexer

code = input("Algo para testear bro → ")
lexer = ZynkLexer(code, True)
tokens = lexer.scan_tokens()
for token in tokens:
	print(f"{token.type.value} {token.lexem} {token.value}")

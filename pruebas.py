# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# Copyright (c) 2025 Guillermo Leira Temes


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

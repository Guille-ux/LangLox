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

# Lexic Analyzer
from .. import errors
from .. import tokens


class ZynkLexer:
	def __init__(self, source_code, big_debug=False):
		self.source = source_code
		self.debug = big_debug
		self.tokens = []
		self.start = 0
		self.current = 0
		self.line = 1
		self.column = 1
		self.error = False
		self.var_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_" # set de caracteres que puede usar una variable
	def scan_tokens(self):
		while not self.is_at_end():
			self.start = self.current
			self.scan_token()
		self.add_token(tokens.TokenType.EOF)
		return self.tokens
	def is_at_end(self):
		return self.current >= len(self.source)
	def scan_token(self):
		trigger = False
		char = self.advance()
		#Scan
		if self.is_comment():
			trigger = True
		if self.scan_one(char):
			return True
		if self.scan_two(char):
			return True
		if self.scan_three(char):
			return True
		if self.scan_four():
			return True
		if self.lexe_var():
			return True
		#Error
		if trigger:
			pass
		else:
			#implementar manejo de error léxico para unexpected Token
			self.error = True
			error = errors.UnexpectedTokenError(self.line, self.column, self.source[self.current-1])
			error.print_error()
			if self.debug:
				raise error
	def is_comment(self):
		if self.source[self.current-1]=="#":
			self.skip_comment()
			return True
		return False
	def skip_comment(self):
		while not self.is_at_end():
			char = self.peek()
			if char == "\n":
				self.line += 1
				self.column = 1
				self.advance()
				break
			self.advance()
	def skip_string(self):
		while not self.is_at_end() and self.peek() != '"':
			self.advance()
		self.advance()
		if self.is_at_end():
			error = errors.ZynkPyError(self.line, self.column, "Unterminated string.")
			error.print_error()
			self.error = True
			if self.debug:
				raise error
			return False
		return True
	def peek(self):
		if self.is_at_end():
			return "\0"
		return self.source[self.current]
	def scan_four(self): # para otras expresiones
		if self.match_sequence("null"):
			self.add_token(tokens.TokenType.NULL, "null")
			return True
		elif self.match_sequence("new"):
			self.add_token(tokens.TokenType.NEW, "new")
			return True
		elif self.match_sequence("or"):
			self.add_token(tokens.TokenType.OR, "or")
			return True
		elif self.match_sequence("and"):
			self.add_token(tokens.TokenType.AND, "and")
			return True
		elif self.match_sequence("not"):
			self.add_token(tokens.TokenType.NOT, "not")
			return True
		elif self.match_sequence("print"):
			self.add_token(tokens.TokenType.PRINT, "print")
			return True
		elif self.match_sequence("call"):
			self.add_token(tokens.TokenType.CALL, "call")
			return True
		elif self.match_sequence("var"):
			self.add_token(tokens.TokenType.VAR, "var")
			return True
		elif self.match_sequence("this"):
			self.add_token(tokens.TokenType.THIS, "this")
			return True
		elif self.match_sequence("true"):
			self.add_token(tokens.TokenType.TRUE, "true", True)
			return True
		elif self.match_sequence("false"):
			self.add_token(tokens.TokenType.FALSE, "false", False)
			return True
		elif self.match_sequence("import"):
			self.add_token(tokens.TokenType.IMPORT, "import")
			return True
		elif self.match_sequence("class"):
			self.add_token(tokens.TokenType.CLASS, "class")
			return True
		elif self.match_sequence("func"):
			self.add_token(tokens.TokenType.FUNC, "func")
			return True
		elif self.match_sequence("return"):
			self.add_token(tokens.TokenType.RETURN, "return")
			return True
		elif self.match_sequence("if"):
			self.add_token(tokens.TokenType.IF, "if")
			return True
		elif self.match_sequence("else"):
			self.add_token(tokens.TokenType.ELSE, "else")
			return True
		elif self.match_sequence("extends"):
			self.add_token(tokens.TokenType.EXTENDS, "extends")
			return True
		elif self.match_sequence("input"):
			self.add_token(tokens.TokenType.INPUT, "input")
			return True
		elif self.match_sequence("for"):
			self.add_token(tokens.TokenType.FOR, "for")
			return True
		elif self.match_sequence("while"):
			self.add_token(tokens.TokenType.WHILE, "while")
			return True
		elif self.match_sequence("super"):
			self.add_token(tokens.TokenType.SUPER, "super")
			return True
	def scan_three(self, char): # Para los literales
		if char == '"':
			if self.skip_string():
				self.add_token(tokens.TokenType.STRING, self.source[self.start:self.current], self.source[self.start+1:self.current-1])
				return True
		if char.isdigit():
			result = self.num_lexer()
			if result:
				self.add_token(tokens.TokenType.FLOAT, self.source[self.start:self.current], float(self.source[self.start:self.current]))
				return True
			elif not result:
				self.add_token(tokens.TokenType.INT, self.source[self.start:self.current], int(self.source[self.start:self.current]))
				return True
	def scan_one(self, char): # scans one character symbols
		if char == " " or char == "\t" or char == "\r":
			return True
		elif char == "\n":
			self.line += 1
			self.column = 1
			return True
		elif char == "(":
			self.add_token(tokens.TokenType.LPAREN, "(")
		elif char == ")":
			self.add_token(tokens.TokenType.RPAREN, ")")
			return True
		elif char == "{":
			self.add_token(tokens.TokenType.LBRACE, "{")
			return True
		elif char == "}":
			self.add_token(tokens.TokenType.RBRACE, "}")
			return True
		elif char == ",":
			self.add_token(tokens.TokenType.COMMA, ",")
			return True
		elif char == ";":
			self.add_token(tokens.TokenType.SEMICOLON, ";")
			return True
		elif char == ".":
			self.add_token(tokens.TokenType.DOT, ".")
			return True
		elif char == "+":
			self.add_token(tokens.TokenType.PLUS, "+")
			return True
		elif char == "-":
			self.add_token(tokens.TokenType.MINUS, "-")
			return True
		elif char == "*":
			self.add_token(tokens.TokenType.MULTIPLY, "*")
			return True
		elif char == "/":
			self.add_token(tokens.TokenType.DIVIDE, "/")
			return True
	def scan_two(self, char): #scans 2 character tokens
		if char == "!":
			if self.match("="):
				self.add_token(tokens.TokenType.NOT_EQUAL, "!=")
				return True
			else:
				self.add_token(tokens.TokenType.NOT, "!")
				return True
		elif char == "=":
			if self.match("="):
				self.add_token(tokens.TokenType.EQUALS, "==")
				return True
			else:
				self.add_token(tokens.TokenType.ASSIGN, "=")
				return True
		elif char == "<":
			if self.match("="):
				self.add_token(tokens.TokenType.LESS_EQUAL, "<=")
				return True
			else:
				self.add_token(tokens.TokenType.LESS, "<")
				return True
		elif char == ">":
			if self.match("="):
				self.add_token(tokens.TokenType.GREATER_EQUAL, ">=")
				return True
			else:
				self.add_token(tokens.TokenType.GREATER, ">")
				return True
	def advance(self):
		self.current += 1
		self.column += 1
		return self.source[self.current-1]
	def retro(self):
		self.current -= 1
		self.column -= 1
		return self.source[self.current-1]
	def match(self, expected):
		if self.is_at_end() or self.source[self.current] != expected:
			return False
		self.current += 1
		self.column += 1
		return True
	def add_token(self, token_type, lexeme="", literal=None):

		self.tokens.append(tokens.Token(token_type, lexeme, literal, self.line, self.column))
	def num_lexer(self): #una utilidad para tokenizar números, se le llama cuando se encuentra un número
		consumed = False
		while not self.is_at_end():
			char = self.advance()
			if consumed == True:
				if not self.peek().isdigit():
					break #we have readed the complet number
			elif consumed == False:
				if char == ".":
					consumed = True
				elif self.peek().isdigit():
					pass
				else:
					break
		return consumed
	def get_actual(self):
		return self.source[self.current-1]
	def match_sequence(self, to_prove):
		ret_point = self.current
		first = self.get_actual()
		if first != to_prove[0]:
			return False
		i = 1
		while i < len(to_prove):
			if not self.match(to_prove[i]):
				self.current = ret_point
				return False
			i += 1
		if self.match(" "):
			return True
		else:
			self.current = ret_point
			return False
	def lexe_var(self):
		trigger = False
		char = self.get_actual()
		while not self.is_at_end():
			if char not in self.var_set:
				break
			else:
				trigger = True
				char = self.advance()
		if trigger:
			self.add_token(tokens.TokenType.IDENTIFIER, self.source[self.start:self.current])

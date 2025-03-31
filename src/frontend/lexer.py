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
import tokens

# Sintax Error
class ParseError(Exception):
	def __init__(self, line, column, additional, error_type):
		self.line = line
		self.column = column
		self.message = f"[line {self.line}, column {self.column}] Error: {error_type}: {additional}"
		super().__init__(self.message)
	def print_error(self):
		print(self.message, file=sys.stderr)
class UnexpectedTokenError(ParseError):
	def __init__(self, line, column, err_token):
		self.line = line
		self.type = "Unexpected Token"
		self.additional = err_token
		self.column = column
		super().__init__(self.line, self.column, self.additional, self.type)

class ZynkPyError(Exception):
	def __init__(self, line, column, error_msg):
		self.line = line
		self.column = column
		self.message = f"[line {self.line}, column {self.column}] Error: {error_msg}"
		super().__init__(self.message)
	def print_error(self):
		print(self.message, file=sys.stderr)

# Lexic Analyzer
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
		if self.scan_four(char):
			return True
		#Error
		if trigger:
			pass
		else:
			#implementar manejo de error léxico para unexpected Token
			self.error = True
			error = UnexpectedTokenError(self.line, self.column, self.source[self.current-1])
			error.print_error()
			if self.debug:
				raise error
	def is_comment(self):
		if self.source[self.current-1]=="#":
			self.skip_comment()
		return True
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
		if is_at_end():
			error = ZynkPyError(self.line, self.column, "Unterminated string.")
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
	def scan_four(self, char): # para otras expresiones
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
		elif self.match_sequence("call")
			self.add_token(tokens.TokenType.CALL, "call")
			return True
		elif self.match_sequence("var"):
			self.add_token(tokens.TokenType.VAR, "var")
			return True
		elif self.match_sequence("this"):
			self.add_token(tokens.TokenType.THIS, "this")
			return True
		elif self.match_sequence("true"):
			self.add_token(tokens.TokenType.TRUE, "true")
			return True
		elif self.match_sequence("false"):
			self.add_token(tokens.TokenType.FALSE, "false")
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
		# faltan for, while, super y nada más
		#añadiendolos ahora
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
				self.add_token(tokens.TokenType.FLOAT, self.source[self.start:self.current], self.source[self.start:self.current])
				return True
			elif not result:
				self.add_token(tokens.TokenType.INT, self.source[self.start:self.current], self.source[self.start:self.current])
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
				self.add_tokens(tokens.TokenType.NOT, "!")
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
	def match(self, expected):
		if self.is_at_end() or self.source[self.current] != expected:
			return False
		self.current += 1
		self.column += 1
		return True
	def add_token(self, token_type, lexeme="", literal=None):

		self.tokens.append(tokens.Token(token_type, lexeme, self.line, self.column))
	def num_lexer(self): #una utilidad para tokenizar números, se le llama cuando se encuentra un número
		consumed = False
		while not self.is_at_end():
			char = self.advance()
			if consumed == True:
				if not char.isdigit():
					break #we have readed the complet number
			elif consumed == False:
				if char == "." and consumed==False:
					consumed = True
				elif char.isdigit():
					pass
				else:
					#ERROR CARACTER NO ESPERADO
					error = UnexpectedTokenError(self.line, self.column, self.source[self.current-1])
					self.error = True
					error.print_error()
					if self.debug:
						raise error
		return consumed
		self.advance()
	def get_actual(self):
		return self.source[self.current-1]
	def match_sequence(self, to_prove)
		ret_point = self.current-1
		first = self.get_actual()
		if first != to_prove[0]:
			return False
		i = 1
		while i < len(to_prove):
			if not self.match(to_prove[i]):
				self.current = ret_point
				return False
		if self.match(" "):
			return True
		else:
			self.current = ret_point
			return False

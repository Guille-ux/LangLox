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

class LoxError(Exception):
	def __init__(self, line, column, error_msg):
		self.line = line
		self.column = column
		self.message = f"[line {self.line}, column {self.column}] Error: {error_msg}"
		super().__init__(self.message)
	def print_error(self):
		print(self.message, file=sys.stderr)

class Lexer:
	def __init__(self, source_code):
		self.source = source_code
		self.tokens = []
		self.start = 0
		self.current = 0
		self.line = 1
		self.column = 1
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
		#Error
		if trigger:
			pass
		else:
			#implementar manejo de error léxico para unexpected Token
		
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
			error = LoxError(self.line, self.column, "Unterminated string.")
			error.print_error()
			self.error = True
			return False
		return True
	def peek(self):
		if self.is_at_end():
			return "\0"
		return self.source[self.current]
	def scan_three(self, char): # More Complex Structures
		if char == '"':
			if self.skip_string():
				self.add_token(tokens.TokenType.STRING, self.source[self.start:self.current], self.source[self.start+1:self.current-1])
		return True
	def scan_one(self, char): # scans one character symbols
		if char == " " or char == "\t" or char == "\r":
			return
		elif char == "\n":
			self.line += 1
			self.column = 1
		elif char == "(":
			self.add_token(tokens.TokenType.LPAREN, "(")
		elif char == ")":
			self.add_token(tokens.TokenType.RPAREN, ")")
		elif char == "{":
			self.add_token(tokens.TokenType.LBRACE, "{")
		elif char == "}":
			self.add_token(tokens.TokenType.RBRACE, "}")
		elif char == ",":
			self.add_token(tokens.TokenType.COMMA, ",")
		elif char == ";":
			self.add_token(tokens.TokenType.SEMICOLON, ";")
		elif char == ".":
			self.add_token(tokens.TokenType.DOT, ".")
		elif char == "+":
			self.add_token(tokens.TokenType.PLUS, "+")
		elif char == "-":
			self.add_token(tokens.TokenType.MINUS, "-")
		elif char == "*":
			self.add_token(tokens.TokenType.MULTIPLY, "*")
		elif char == "/":
			self.add_token(tokens.TokenType.DIVIDE, "/")
		return True
	def scan_two(self, char): #scans 2 character tokens
		if char == "!":
			if self.match("="):
				self.add_token(tokens.TokenType.NOT_EQUAL, "!=")
			else:
				self.add_tokens(tokens.TokenType.NOT, "!")
		elif char == "=":
			if self.match("="):
				self.add_token(tokens.TokenType.EQUALS, "==")
			else:
				self.add_token(tokens.TokenType.ASSIGN, "=")
		elif char == "<":
			if self.match("="):
				self.add_token(tokens.TokenType.LESS_EQUAL, "<=")
			else:
				self.add_token(tokens.TokenType.LESS, "<")
		elif char == ">":
			if self.match("="):
				self.add_token(tokens.TokenType.GREATER_EQUAL, ">=")
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
	

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
		self.add_token(TokenType.EOF)
		return self.tokens
	def is_at_end(self):
		return self.current >= len(self.source)
	def scan_token(self):
		char = self.advance()
		self.is_comment()
		self.scan_one(char)
		self.scan_two(char)
	def is_comment(self):
		if self.source[self.current-1]=="#":
			self.skip_comment()
	def skip_comment(self):
		while not self.is_at_end():
			char = self.peek()
			if char == "\n":
				self.line += 1
				self.column = 1
				self.advance()
				break
			self.advance()
	def peek(self):
		if self.is_at_end():
			return "\0"
		return self.source[self.current]
	def scan_one(self, char): # scans one character symbols
		if char == " " or char == "\t" or char == "\r":
			return
		elif char == "\n":
			self.line += 1
			self.column = 1
		elif char == "(":
			self.add_token(TokenType.LPAREN)
		elif char == ")":
			self.add_token(TokenType.RPAREN)
		elif char == "{":
			self.add_token(TokenType.LBRACE)
		elif char == "}":
			self.add_token(TokenType.RBRACE)
		elif char == ",":
			self.add_token(TokenType.COMMA)
		elif char == ";":
			self.add_token(TokenType.SEMICOLON)
		elif char == ".":
			self.add_token(TokenType.DOT)
		elif char == "+":
			self.add_token(TokenType.PLUS)
		elif char == "-":
			self.add_token(TokenType.MINUS)
		elif char == "*":
			self.add_token(TokenType.MULTIPLY)
		elif char == "/":
			self.add_token(TokenType.DIVIDE)
	def scan_two(self, char): #scans 2 character tokens
		if char == "!":
			if self.match("="):
				self.add_token(TokenType.NOT_EQUAL)
			else:
				self.add_tokens(TokenType.NOT)
		elif char == "=":
			if self.match("="):
				self.add_token(TokenType.EQUALS)
			else:
				self.add_token(TokenType.ASSIGN)
		elif char == "<":
			if self.match("="):
				self.add_token(TokenType.LESS_EQUAL)
			else:
				self.add_token(TokenType.LESS)
		elif char == ">":
			if self.match("="):
				self.add_token(TokenType.GREATER_EQUAL)
			else:
				self.add_token(TokenType.GREATER)
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
	def add_token(self, token_type, literal=None):
		if literal is not None:
			if token_type in (TokenType.INT, TokenType.FLOAT):
				self.tokens.append(NumberToken(literal, self.line, self.column))
			else:
				self.tokens.append(Token(token_type, literal, self.line, self.column))
		else:
			self.tokens.append(NullToken(token_type, self.line, self.column))


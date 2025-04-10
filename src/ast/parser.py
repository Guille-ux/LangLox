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

from .. import tokens
from .. import errors
from . import expressions as zexpr
from . import sentences as zsent
from . import memory as zmem

class AlgebraicParser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.pos = 0
	def parse(self):
		return self.expr()
	def expr(self):
		term1 = self.term()
		while self.match(tokens.TokenType.PLUS) or self.match(tokens.TokenType.MINUS):
			if self.peek().type == tokens.TokenType.SEMICOLON:
				return term1
			op = self.prev().lexem
			term2 = self.term()
			term1 = zexpr.Binary(term1, op, term2)
		return term1
	def term(self):
		factor1 = self.factor()
		while self.match(tokens.TokenType.MULTIPLY) or self.match(tokens.TokenType.DIVIDE):
			if self.peek().type == tokens.TokenType.SEMICOLON:
				return factor1
			op = self.prev().lexem
			factor2 = self.factor()
			factor1 = zexpr.Binary(factor1, op, factor2)
		return factor1
	def factor(self):
		if self.match(tokens.TokenType.MINUS) or self.match(tokens.TokenType.NOT):
			op = self.prev().lexem
			right = self.factor()
			return zexpr.Unary(op, right)
		if self.match(tokens.TokenType.INT):
			return zexpr.Literal(self.prev().value)
		elif self.match(tokens.TokenType.FLOAT):
			return zexpr.Literal(self.prev().value)
		elif self.match(tokens.TokenType.LPAREN):
			expr = self.expr()
			self.match_or_error(tokens.TokenType.RPAREN)
			return expr
		elif self.match(tokens.TokenType.IDENTIFIER):
			expr = zsent.VarExpr(self.prev().lexem)
			return expr
		elif self.match(tokens.TokenType.STRING):
			return zexpr.Literal(self.prev().value)
		elif self.match(tokens.TokenType.TRUE):
			return zexpr.Literal(self.prev().value)
		elif self.match(tokens.TokenType.FALSE):
			return zexpr.Literal(self.prev().value)
		elif self.match(tokens.TokenType.NULL):
			return zexpr.Literal(self.prev().value)
		raise SyntaxError(f"Unexpected Token: {self.peek().type}")
	def peek(self):
		if self.pos < len(self.tokens):
			return self.tokens[self.pos]
	def match(self, expected_type):
		if self.pos < len(self.tokens) and self.tokens[self.pos].type == expected_type:
			self.pos += 1
			return True
		return False
	def prev(self):
		return self.tokens[self.pos-1]
	def match_or_error(self, expected):
		if not self.match(expected):
			raise SyntaxError(f"Expected Token {expected}, but found {self.peek().type}")
		return self.prev()
class ZynkParser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.pos = 0
		self.token_begin = 0
	def parse(self):
		exprs = []
		while not self.is_at_end():
			stmt = self.parse_expr()
			self.advance()
			if stmt is None:
				continue
			else:
				exprs.append(stmt)
		return exprs
	def parse_expr(self):
		self.token_begin = self.pos
		if self.match(tokens.TokenType.SECURITY): # security token
			return None
		if self.check(tokens.TokenType.PRINT): # funcionalidad para imprimir
			arguments = []
			while not self.is_at_end():
				if self.match(tokens.TokenType.SEMICOLON):
					break
				elif self.match(tokens.TokenType.EOF): # importante para el caso de EOF
					raise SyntaxError("Unexpected EOF")
				arguments.append(self.advance())
			if arguments and arguments[-1].type in (tokens.TokenType.SEMICOLON, tokens.TokenType.EOF):
				arguments.pop()
			parsed = self.algebraic(arguments)
			return zsent.PrintStmt(parsed)
		elif self.match(tokens.TokenType.VAR): # variable declaration, increiblemente funciona
			name = self.prev().lexem
			self.match_or_error(tokens.TokenType.IDENTIFIER)
			self.check(tokens.TokenType.ASSIGN)
			arguments = []
			while not self.is_at_end():
				if self.match(tokens.TokenType.SEMICOLON):
					break
				elif self.match(tokens.TokenType.EOF):
					raise SyntaxError("Unexpected EOF")
				arguments.append(self.advance())
			if arguments and arguments[-1].type in (tokens.TokenType.SEMICOLON, tokens.TokenType.EOF):
				arguments.pop()
			parsed = self.algebraic(arguments)
			if not parsed:
				self.error("Expected expression after '='")
			return zsent.VarStmt(name, parsed)
		else:
			raise SyntaxError(f"Unexpected Token : {self.peek().type}")
	def algebraic(self, tokens):
		return AlgebraicParser(tokens).parse()
	def advance(self):
		if not self.is_at_end():
			self.pos += 1
		return self.peek()
	def is_at_end(self):
		return self.pos >= len(self.tokens)
	def match(self, expected_type):
		if self.is_at_end():
			return False
		if self.tokens[self.pos].type == expected_type:
			self.pos += 1
			return True
		return False
	def check(self, expected_type):
		if self.is_at_end():
			return False
		return self.tokens[self.pos].type == expected_type
	def prev(self):
		if not self.is_at_end() and self.pos > 0:
			return self.tokens[self.pos - 1]
	def match_or_error(self, expected):
		if not self.match(expected):
			raise SyntaxError(f"Expected Token {expected}, but found {self.peek().type}")
		return self.prev()
	def peek(self):
		if self.is_at_end():
			return tokens.Token(tokens.TokenType.SECURITY, "", None, -1, -1)
		return self.tokens[self.pos]
	def error(self, message):
		line, column = self.peek().get_pos()
		raise errors.ZynkError(f"Error at line {line}, column {column}: {message}")
	def get_pos(self):
		return self.peek().get_pos()
	def get_line(self):
		return self.peek().line
	def get_column(self):
		return self.peek().column
	def get_token(self):
		return self.peek().type
	def get_value(self):
		return self.peek().value
	def get_lexem(self):
		return self.peek().lexem
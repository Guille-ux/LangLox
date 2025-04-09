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
			expr = zsent.VarExpr()
			return expr
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
		statements = []
		while not self.is_at_end():
			statements.append(self.statement())
		return statements
	def statement(self):
		self.token_begin = self.pos
		if self.match(tokens.TokenType.RETURN):
			expression = self.expression()
			self.match_or_error(tokens.TokenType.SEMICOLON)
			return zsent.ReturnStmt(expression)
		elif self.match(tokens.TokenType.IMPORT):
			name = self.match_or_error(tokens.TokenType.IDENTIFIER)
			self.match_or_error(tokens.TokenType.SEMICOLON)
			return zsent.ImportStmt(name.lexem)
		elif self.match(tokens.TokenType.CALL):
			callee = self.expression()
			self.match_or_error(tokens.TokenType.SEMICOLON)
			return zsent.CallStmt(callee)
		elif self.match(tokens.TokenType.NEW):
			class_name = self.match_or_error(tokens.TokenType.IDENTIFIER)
			self.match_or_error(tokens.TokenType.LPAREN)
			arguments = []
			while not self.is_at_end() and not self.check(tokens.TokenType.RPAREN):
				arguments.append(self.expression())
			self.match_or_error(tokens.TokenType.RPAREN)
			return zsent.NewStmt(class_name.lexem, arguments)
		elif self.match(tokens.TokenType.FUNC):
			func_name = self.match_or_error(tokens.TokenType.IDENTIFIER)
			self.match_or_error(tokens.TokenType.LPAREN)
			params = []
			while not self.is_at_end() and not self.check(tokens.TokenType.RPAREN):
				params.append(self.match_or_error(tokens.TokenType.IDENTIFIER))
				if self.match(tokens.TokenType.COMMA):
					continue
			self.match_or_error(tokens.TokenType.RPAREN)
			self.match_or_error(tokens.TokenType.LBRACE)
			body = []
			while not self.is_at_end() and not self.check(tokens.TokenType.RBRACE):
				body.append(self.statement())
			self.match_or_error(tokens.TokenType.RBRACE)
			return zsent.FunctionStmt(func_name.lexem, params, body)
		elif self.match(tokens.TokenType.CLASS):
			name = self.match_or_error(tokens.TokenType.IDENTIFIER)
			superclass = None
			if self.match(tokens.TokenType.EXTENDS):
				superclass = self.match_or_error(tokens.TokenType.IDENTIFIER)
			self.match_or_error(tokens.TokenType.LBRACE)
			methods = []
			while not self.is_at_end() and not self.check(tokens.TokenType.RBRACE):
				methods.append(self.statement())
			self.match_or_error(tokens.TokenType.RBRACE)
			return zsent.ClassStmt(name.lexem, superclass, methods)
		elif self.match(tokens.TokenType.PRINT):
			return self.print_stmt()
		elif self.match(tokens.TokenType.VAR):
			return self.var_stmt()
		elif self.match(tokens.TokenType.IF):
			return self.if_stmt()
		elif self.match(tokens.TokenType.WHILE):
			return self.while_stmt()
		elif self.match(tokens.TokenType.FOR):
			return self.for_stmt()
		elif self.match(tokens.TokenType.LBRACE):
			return zsent.BlockStmt(self.block())
		elif self.match(tokens.TokenType.THIS):
			self.match_or_error(tokens.TokenType.SEMICOLON)
			return zsent.ThisStmt(self.prev())
		elif self.check(tokens.TokenType.IDENTIFIER):
			name = self.match_or_error(tokens.TokenType.IDENTIFIER)
			if self.match(tokens.TokenType.ASSIGN):
				expression = self.expression()
				self.match_or_error(tokens.TokenType.SEMICOLON)
				return zsent.VarStmt(name.lexem, expression)
			else:
				return zsent.VarExpr(name.lexem)
		elif self.match(tokens.TokenType.SEMICOLON):
			return None
		else:
			return zsent.ExprStmt(self.expression())
	def print_stmt(self):
		expression = self.expression()
		self.match_or_error(tokens.TokenType.SEMICOLON)
		return zsent.PrintStmt(expression)
	def var_stmt(self):
		tokenVar = self.match_or_error(tokens.TokenType.IDENTIFIER)
		if self.match(tokens.TokenType.ASSIGN):
			if self.match(tokens.TokenType.STRING):
				expression = zexpr.Literal(self.prev().value)
			elif self.match(tokens.TokenType.INT):
				expression = zexpr.Literal(self.prev().value)
			elif self.match(tokens.TokenType.FLOAT):
				expression = zexpr.Literal(self.prev().value)
			elif self.match(tokens.TokenType.IDENTIFIER):
				expression = zexpr.Literal(self.prev().value)
			elif self.match(tokens.TokenType.TRUE):
				expression = zexpr.Literal(True)
			elif self.match(tokens.TokenType.FALSE):
				expression = zexpr.Literal(False)
			elif self.match(tokens.TokenType.NULL):
				expression = zexpr.Literal(None)
			elif self.match(tokens.TokenType.LPAREN):
				expression = self.expression()
				self.match_or_error(tokens.TokenType.RPAREN)
		else:
			expression = None
		self.match_or_error(tokens.TokenType.SEMICOLON)
		return zsent.VarStmt(tokenVar.lexem, expression)
	def if_stmt(self):
		self.match_or_error(tokens.TokenType.LPAREN)
		condition = self.expression()
		self.match_or_error(tokens.TokenType.RPAREN)
		then_branch = self.statement()
		else_branch = None
		if self.match(tokens.TokenType.ELSE):
			else_branch = self.statement()
		return zsent.IfStmt(condition, then_branch, else_branch)
	def while_stmt(self):
		self.match_or_error(tokens.TokenType.LPAREN)
		condition = self.expression()
		self.match_or_error(tokens.TokenType.RPAREN)
		body = self.statement()
		return zsent.WhileStmt(condition, body)
	def for_stmt(self):
		self.match_or_error(tokens.TokenType.LPAREN)
		init = None
		if self.match(tokens.TokenType.VAR):
			init = self.var_stmt()
		else:
			init = self.expression()
		self.match_or_error(tokens.TokenType.SEMICOLON)
		condition = self.expression()
		self.match_or_error(tokens.TokenType.SEMICOLON)
		change = self.expression()
		self.match_or_error(tokens.TokenType.RPAREN)
		body = self.statement()
		return zsent.ForStmt(init, condition, change, body)
	def block(self):
		statements = []
		while not self.is_at_end() and not self.check(tokens.TokenType.RBRACE):
			statements.append(self.statement())
		self.match_or_error(tokens.TokenType.RBRACE)
		return statements
	def expression(self):
		return self.algebraic()
	def algebraic(self):
		return AlgebraicParser(self.token_begin).parse()
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
		return self.tokens[self.pos - 1]
	def match_or_error(self, expected):
		if not self.match(expected):
			raise SyntaxError(f"Expected Token {expected}, but found {self.peek().type}")
		return self.prev()
	def peek(self):
		if self.is_at_end():
			return None
		return self.tokens[self.pos]
	def error(self, message):
		line, column = self.peek().get_pos()
		raise errors.ZynkError(f"Error at line {line}, column {column}: {message}")
	def synchronize(self):
		while not self.is_at_end():
			if self.prev().type == tokens.TokenType.SEMICOLON:
				return
			if self.peek().type in (tokens.TokenType.CLASS, tokens.TokenType.FUNC, tokens.TokenType.VAR,
									tokens.TokenType.IF, tokens.TokenType.WHILE, tokens.TokenType.PRINT,
									tokens.TokenType.RETURN):
				return
			self.pos += 1
		self.pos += 1
		return None
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
	def get_included(self):
		return self.peek().included
	def get_included_tokens(self):
		return self.peek().included
	def get_included_lexems(self):
		return [token.lexem for token in self.peek().included]
	def get_included_values(self):
		return [token.value for token in self.peek().included]
	def get_included_types(self):
		return [token.type for token in self.peek().included]
	def get_included_lines(self):
		return [token.line for token in self.peek().included]
	def get_included_columns(self):
		return [token.column for token in self.peek().included]
	def get_included_pos(self):
		return [token.pos for token in self.peek().included]
	def get_included_pos(self):
		return [token.pos for token in self.peek().included]
	def get_included_pos(self):
		return [token.pos for token in self.peek().included]
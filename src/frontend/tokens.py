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

from enum import Enum

class TokenType(Enum):
	# Literales
	INT = "INT"
	FLOAT = "FLOAT"
	NULL = "NULL"
	STRING = "STRING"
	BOOL = "BOOL"
	
	#IDENTIFICADORES
	IDENTIFIER = "IDENTIFIER"
	
	#KEYWORDS
	CLASS = "CLASS"
	ELSE = "ELSE"
	FALSE = "FALSE"
	FUN = "FUN"
	FOR = "FOR"
	IF = "IF"
	PRINT = "PRINT"
	RETURN = "RETURN"
	SUPER = "SUPER"
	THIS = "THIS"
	TRUE = "TRUE"
	VAR = "VAR"
	WHILE = "WHILE"
	
	#operands
	PLUS = "+"
	MINUS = "-"
	MULTIPLY = "*"
	DIVIDE = "/"
	EQUALS = "=="
	ASSIGN = "="
	GREATER = ">"
	GREATER_EQUAL = ">="
	LESS_EQUAL = "<="
	LESS = "<"
	OR = "or"
	NOT = "!"
	XOR = "^"
	AND = "and"
	NOT_EQUAL = "!="
	
	
	#delimitadores
	LPAREN = "("
	RPAREN = ")"
	LBRACE = "{"
	RBRACE = "}"
	COMMA = ","
	SEMICOLON = ";"
	
	#Otros tipos
	EOF = "EOF"
	DOT = "."

class Token:
	def __init__(self, tipo, valor, line, column):
		self.line = line
		self.column = column
		self.type = tipo
		self.value = valor
		self.included = []
	def include(self, token):
		self.included.append(token)
	def __repr__(self):
		return f"Token(type={self.type}, value={self.value})"
	def __str__(self):
		return f"Token of the type {self.type} with the value {self.value}"
	def __eq__(self, other):
		return self.type == other.type and self.value == other.value
	def get_pos(self):
		return (self.line, self.column)
class NullToken(Token):
	def __init__(self, tipo, line, column):
		super().__init__(tipo, None, line, column)
	def __repr__(self):
		return f"NullToken(type={self.type})"
	def __str__(self):
		return f"A null token with type {self.type}"
	def __eq__(self, other):
		return self.type == other.type

class NumberToken(Token):
	def __init__(self, value, line, column):
		tipo = TokenType.INT if isinstance(value, int) else TokenType.FLOAT
		super().__init__(tipo, value, line, column)
	def __str__(self):
		return str(self.value)


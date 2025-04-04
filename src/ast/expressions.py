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

class Expr:
	def accept(self, visitor):
		raise NotImplementedError()
class Literal(Expr):
	def __init__(self, value):
		self.value = value
	def accept(self, visitor):
		return visitor.visit_literal(self)
class Binary(Expr):
	def __init__(self, left, operator, right):
		self.left = left
		self.operator = operator
		self.right = right
	def accept(self, visitor):
		return visitor.visit_binary(self)
class Unary(Expr):
	def __init__(self, operator, right):
		self.operator = operator
		self.right = right
	def accept(self, visitor):
		return visitor.visit_unary(self)
	
class Grouping(Expr):
	def __init__(self, expr):
		self.expr = expr
	def accept(self, visitor):
		return visitor.visit_grouping(self)
	
class Visitor:
	def visit_literal(self, expr):
		raise NotImplementedError()
	def visit_binary(self, expr):
		raise NotImplementedError()
	def visit_unary(self, expr):
		raise NotImplementedError()
	def visit_grouping(self, expr):
		raise NotImplementedError()

class ZynkEval(Visitor):
	def visit_literal(self, expr):
		return expr.value
	def visit_binary(self, expr):
		left = expr.left.accept(self)
		right = expr.right.accept(self)
		try:
			#lógica
			if expr.operator == "+":
				return left + right
			elif expr.operator == "and":
				return left and right
			elif expr.operator == "or":
				return left or right
			elif expr.operator == "^":
				return left ^ right
			elif expr.operator == "<":
				return left < right
			elif expr.operator == "==":
				return left == right
			elif expr.operator == "!=":
				return left != right
			elif expr.operator == "<=":
				return left <= right
			elif expr.operator == ">":
				return left > right
			elif expr.operator == ">=":
				return left >= right
			elif expr.operator == "-":
				return left - right
			elif expr.operator == "*":
				return left * right
			elif expr.operator == "/":
				return left / right
			else:
				raise ValueError(f"¡Operator : {expr.operator} isn't recognized!")
		except Exception as e:
			raise Exception(f"¡Invalid Calc : {expr.left} {expr.operator} {expr.right} !")
	def visit_unary(self, expr):
		sign = expr.right.accept(self)
		
		#logic
		if expr.operator == "-":
			return -sign
		elif expr.operator == "!":
			return not sign
		else:
			raise ValueError(f"¡Operator : {expr.operator} isn't recognized!")
	def visit_grouping(self, expr):
		return expr.expr.accept(self)

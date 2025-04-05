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

#Visitor pattern (it is very helpful)

from . import expressions as zexpr
from . import sentences as zsent

class Visitor:
	def visit_literal(self, expr):
		raise NotImplementedError()
	def visit_binary(self, expr):
		raise NotImplementedError()
	def visit_unary(self, expr):
		raise NotImplementedError()
	def visit_grouping(self, expr):
		raise NotImplementedError()
	def visit_print_stmt(self, stmt):
		raise NotImplementedError
	def visit_expression_stmt(self, stmt):
		raise NotImplementedError
	def visit(self, expr):
		raise NotImplementedError

class ZynkEval(Visitor):
	def visit(self, expr):
		if isinstance(expr, zexpr.Literal):
			return self.visit_literal(expr)
		elif isinstance(expr, zexpr.Binary):
			return self.visit_binary(expr)
		elif isinstance(expr, zexpr.Unary):
			return self.visit_unary(expr)
		elif isinstance(expr, zexpr.Grouping):
			return self.visit_grouping(expr)
		elif isinstance(expr, zsent.PrintStmt):
			return self.visit_print_stmt(expr)
		elif isinstance(expr, zsent.ExprStmt):
			return self.visit_expression_stmt(expr)
		else:
			raise ValueError(f"¡Unknow Expression type : {type(expr)}")
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
	def visit_print_stmt(self, stmt):
		value = self.evaluate(expr.expression)
		print(value)
	def evaluate(self, expr):
		return expr.accept(self)
	def visit_expression_stmt(self, stmt):
		return self.evaluate(stmt.expression)

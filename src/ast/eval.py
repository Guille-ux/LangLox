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
from . import memory as zmem

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
	def visit_var_stmt(self, stmt):
		raise NotImplementedError
	def visit_block_stmt(self, stmt):
		raise NotImplementedError
	def visit_if_stmt(self, stmt):
		raise NotImplementedError
	def visit_while_stmt(self, stmt):
		raise NotImplementedError
	def visit_for_stmt(self, stmt):
		raise NotImplementedError

class ZynkEval(Visitor):
	def __init__(self):
		self.memory = zmem.SymbolTable()
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
		elif isinstance(expr, zsent.VarStmt):
			return self.visit_var_stmt(expr)
		elif isinstance(expr, zsent.BlockStmt):
			return self.visit_block_stmt(expr)
		elif isinstance(expr, zsent.IfStmt):
			return self.visit_if_stmt(expr)
		elif isinstance(expr, zsent.WhileStmt):
			return self.visit_while_stmt(expr)
		elif isinstance(expr, zsent.ForStmt):
			return self.visit_for_stmt(expr)
		elif isinstance(expr, zsent.VarExpr):
			return self.visit_var_expr(expr)
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
		value = self.evaluate(stmt.expression)
		print(value)
	def evaluate(self, expr):
		return expr.accept(self)
	def visit_expression_stmt(self, stmt):
		return self.evaluate(stmt.expression)
	def visit_var_stmt(self, stmt):
		value = self.evaluate(stmt.initializer)
		print(f"Variable {stmt.name} initialized with {value}")
		self.memory.add(stmt.name, value)
		return value
	def visit_block_stmt(self, stmt):
		for statement in stmt.statements:
			self.evaluate(statement)
		return None
	def visit_if_stmt(self, stmt):
		if self.evaluate(stmt.condition):
			return self.evaluate(stmt.then_branch)
		elif stmt.else_branch:
			return self.evaluate(stmt.else_branch)
		return None
	def visit_while_stmt(self, stmt):
		while self.evaluate(stmt.condition):
			self.evaluate(stmt.body)
		return None
	def visit_for_stmt(self, stmt):
		self.evaluate(stmt.init)
		while self.evaluate(stmt.condition):
			self.evaluate(stmt.body)
			self.evaluate(stmt.change)
		return None
	def visit_call_stmt(self, stmt):
		callee = self.evaluate(stmt.callee)
		args = [self.evaluate(arg) for arg in stmt.arguments]
		return callee(*args)
	def visit_new_stmt(self, stmt):
		class_name = self.evaluate(stmt.class_name)
		args = [self.evaluate(arg) for arg in stmt.arguments]
		return class_name(*args)
	def visit_import_stmt(self, stmt):
		module_name = self.evaluate(stmt.module_name)
		return module_name
	def visit_this_stmt(self, stmt):
		return self.evaluate(stmt.this)
	def visit_func_stmt(self, stmt):
		func_name = stmt.func_name
		params = stmt.params
		body = stmt.body
		return func_name, params, body
	def visit_return_stmt(self, stmt):
		if stmt.value:
			return self.evaluate(stmt.value)
		return None
	def visit_var_expr(self, expr):
		value = self.memory.get(expr.name)
		if value is None:
			raise ValueError(f"¡Variable {expr.name} not defined!")
		return value
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
	def __repr__(self):
		return f"{self.value}"
class Binary(Expr):
	def __init__(self, left, operator, right):
		self.left = left
		self.operator = operator
		self.right = right
	def accept(self, visitor):
		return visitor.visit_binary(self)
	def __repr__(self):
		return f"[{self.left}] : [{self.operator}] : [{self.right}]"
class Unary(Expr):
	def __init__(self, operator, right):
		self.operator = operator
		self.right = right
	def accept(self, visitor):
		return visitor.visit_unary(self)
	def __repr__(self):
		return f"[{self.operator}] : [{self.right}]"
	
class Grouping(Expr):
	def __init__(self, expr):
		self.expr = expr
	def accept(self, visitor):
		return visitor.visit_grouping(self)
	def __repr__(self):
		return f"[{self.expr}]"

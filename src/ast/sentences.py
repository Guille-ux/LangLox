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


# Visitor Pattern is very useful

class Sntc: # sentence class
    def accept(self, visitor):
        raise NotImplementedError

class Stmt: # Statements
    def accept(self, visitor):
        raise NotImplementedError

class PrintStmt(Stmt): # Print statement
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visit_print_stmt(self)
class ExprStmt(Sntc): # Expression statement
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visit_expression_stmt(self)
class VarStmt(Stmt):
    def __init__(self, name, initializer): # name is the variable name, initializer is the value
        self.name = name
        self.initializer = initializer
    def accept(self, visitor):
        return visitor.visit_var_stmt(self)
class BlockStmt(Stmt): # Block statement
    def __init__(self, statements):
        self.statements = statements
    def accept(self, visitor):
        return visitor.visit_block_stmt(self)
class IfStmt(Stmt): # If statement
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def accept(self, visitor): 
        return visitor.visit_if_stmt(self)
class WhileStmt(Stmt): # While statement
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def accept(self, visitor):
        return visitor.visit_while_stmt(self)
class ForStmt(Stmt): # For statement
    def __init__(self, init, condition, change, body):
        self.init = init
        self.condition = condition
        self.change = change
        self.body = body
    def accept(self, visitor):
        return visitor.visit_for_stmt(self)
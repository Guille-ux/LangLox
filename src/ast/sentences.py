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


class Stmt: # Statements
    def accept(self, visitor):
        raise NotImplementedError

class PrintStmt(Stmt): # Print statement
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visit_print_stmt(self)
    def __repr__(self):
        return f"Print : {self.expression}"
class ExprStmt(Stmt): # Expression statement
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visit_expression_stmt(self)
    def __repr__(self):
        return f"Expr : {self.expression}"
class VarStmt(Stmt):
    def __init__(self, name, initializer): # name is the variable name, initializer is the value
        self.name = name
        self.initializer = initializer
    def accept(self, visitor):
        return visitor.visit_var_stmt(self)
    def __repr__(self):
        return f"Var : {self.name} = {self.initializer}"
class BlockStmt(Stmt): # Block statement
    def __init__(self, statements):
        self.statements = statements
    def accept(self, visitor):
        return visitor.visit_block_stmt(self)
    def __repr__(self):
        return f"Block : {self.statements}"
class IfStmt(Stmt): # If statement
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def accept(self, visitor): 
        return visitor.visit_if_stmt(self)
    def __repr__(self):
        return f"If : {self.condition} {self.then_branch} {self.else_branch}"
class WhileStmt(Stmt): # While statement
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def accept(self, visitor):
        return visitor.visit_while_stmt(self)
    def __repr__(self):
        return f"While : {self.condition} {self.body}"
class ForStmt(Stmt): # For statement
    def __init__(self, init, condition, change, body):
        self.init = init
        self.condition = condition
        self.change = change
        self.body = body
    def accept(self, visitor):
        return visitor.visit_for_stmt(self)
    def __repr__(self):
        return f"For : {self.init} {self.condition} {self.change} {self.body}"
class CallStmt(Stmt): # Call statement
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments
    def accept(self, visitor):
        return visitor.visit_call_stmt(self)
    def __repr__(self):
        return f"Call : {self.callee} {self.arguments}"
class NewStmt(Stmt): # New statement
    def __init__(self, class_name, arguments):
        self.class_name = class_name
        self.arguments = arguments
    def accept(self, visitor):
        return visitor.visit_new_stmt(self)
    def __repr__(self):
        return f"New : {self.class_name} {self.arguments}"
class ReturnStmt(Stmt): # Return statement
    def __init__(self, value):
        self.value = value
    def accept(self, visitor):
        return visitor.visit_return_stmt(self)
    def __repr__(self):
        return f"Return : {self.value}"
class ClassStmt(Stmt): # Class statement
    def __init__(self, name, superclass, methods):
        self.name = name
        self.superclass = superclass
        self.methods = methods
    def accept(self, visitor):
        return visitor.visit_class_stmt(self)
    def __repr__(self):
        return f"Class : {self.name} {self.superclass} {self.methods}"
class ImportStmt(Stmt): # Import statement
    def __init__(self, module_name):
        self.module_name = module_name
    def accept(self, visitor):
        return visitor.visit_import_stmt(self)
    def __repr__(self):
        return f"Import : {self.module_name}"
class FunctionStmt(Stmt): # Function statement
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def accept(self, visitor):
        return visitor.visit_function_stmt(self)
    def __repr__(self):
        return f"Function : {self.name} {self.params} {self.body}"
class ThisStmt(Stmt): # This statement
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        return visitor.visit_this_stmt(self)
    def __repr__(self):
        return f"This : {self.name}"
class SuperStmt(Stmt): # Super statement
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        return visitor.visit_super_stmt(self)
    def __repr__(self):
        return f"Super : {self.name}"
class VarExpr(Stmt):
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        return visitor.visit_var_expr(self)
    def __repr__(self):
        return f"VarExpr : {self.name}"
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

class PrintStmt(Stmt):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visit_print_stmt(self)
class ExprStmt(Sntc):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visit_expression_stmt(self)

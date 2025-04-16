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

from src.ast.eval import ZynkEval
from src.frontend.lexer import ZynkLexer
from src.ast.parser import ZynkParser
from src.errors import ZynkPyError
from zynktest import tprint as print_test
from zynktest import tvar as var_test
from zynktest import tfunc as func_test
from zynktest import tif as if_test
import sys

def test(test_cases):
    for test_case in test_cases:
        try:
            lexer = ZynkLexer(test_case)
            tokens = lexer.scan_tokens()
            print("Lexer Passed")
            parser = ZynkParser(tokens)
            parsed = parser.parse()
            print("Parser Passed")
            print("Evaluating...")
            evaluator = ZynkEval()
            for todo in parsed:
                evaluator.visit(todo)
            print("Evaluator Passed")
            print(f"Test case: {test_case}")
            print("-----Tokens-----")
            for token in tokens:
                print(token)
            print("-----Parsed-----")
            print(parsed)
            print("-----Evaluated-----")
            for todo in parsed:
                print(evaluator.visit(todo))
            print("-----End-----")
            print("Test case passed")
        except Exception as e:
            print(f"Error: {e}")
            print(f"Test case: {test_case}")
            print("-----Tokens-----")
            for token in tokens:
                print(token)
            print("-----Parsed-----")
            print(parsed)
            print("-----Evaluated-----")
            continue

if sys.argv[1] == "print":
    test_cases = print_test.test_cases
    test(test_cases)
elif sys.argv[1] == "var":
    test_cases = var_test.test_cases
    test(test_cases)
elif sys.argv[1] == "func":
    test_cases = func_test.test_cases
    test(test_cases)
elif sys.argv[1] == "if":
    test_cases = if_test.test_cases
    test(test_cases)
else:
    print("No test cases found")
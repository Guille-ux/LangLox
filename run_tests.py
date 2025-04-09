from test import print_test
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
            print(f"Parsed: {parsed}")
            print(f"Tokens: {tokens}")
            print("Test passed")
        except Exception as e:
            print(f"Error: {e}")
            continue


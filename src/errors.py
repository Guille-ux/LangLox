import sys
# Sintax Error
class ParseError(Exception):
	def __init__(self, line, column, additional, error_type):
		self.line = line
		self.column = column
		self.message = f"[line {self.line}, column {self.column}] Error: {error_type}: {additional}"
		super().__init__(self.message)
	def print_error(self):
		print(self.message, file=sys.stderr)
class UnexpectedTokenError(ParseError):
	def __init__(self, line, column, err_token):
		self.line = line
		self.type = "Unexpected Token"
		self.additional = err_token
		self.column = column
		super().__init__(self.line, self.column, self.additional, self.type)

class ZynkPyError(Exception):
	def __init__(self, line, column, error_msg):
		self.line = line
		self.column = column
		self.message = f"[line {self.line}, column {self.column}] Error: {error_msg}"
		super().__init__(self.message)
	def print_error(self):
		print(self.message, file=sys.stderr)

